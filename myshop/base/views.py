from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Food,Order
from .forms import InfoForm
from . import Checksum
from django.views.decorators.csrf import csrf_exempt
# import checksum generation utility
# You can get this utility from https://developer.paytm.com/docs/checksum/


class IndexView(generic.ListView):
	model=Food
	template_name='base/index.html'

def get_info(request):
	form=InfoForm()
	if request.method=='POST':
		form=InfoForm(request.POST)

		if form.is_valid():
			temp=form.save()
			return HttpResponseRedirect(reverse('base:proceed',args=(temp.order_id,temp.amount,temp.cust_id)))
			

	
	return render(request,'base/info.html',{'form':form})

def proceed(request,order_id,amount,cust_id):
	
	

	# initialize dictionary with request parameters
	paytmParams = {

		# Find your MID in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
		"MID" : "UcmJZn78501805528055",

		# Find your WEBSITE in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
		"WEBSITE" : "WEBSTAGING",

		# Find your INDUSTRY_TYPE_ID in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
		"INDUSTRY_TYPE_ID" : "Retail",

		# WEB for website and WAP for Mobile-websites or App
		"CHANNEL_ID" : "WEB",

		# Enter your unique order id
		"ORDER_ID" : str(order_id),

		# unique id that belongs to your customer
		"CUST_ID" : str(cust_id),

		# customer's mobile number
		# "MOBILE_NO" : "CUSTOMER_MOBILE_NUMBER",

		# customer's email
		# "EMAIL" : "CUSTOMER_EMAIL",

		# Amount in INR that is payble by customer
		# this should be numeric with optionally having two decimal points
		"TXN_AMOUNT" : str(amount),

		# on completion of transaction, we will send you the response on this URL
		"CALLBACK_URL" : "http://127.0.0.1:8000/callback/",
	}

	# Generate checksum for parameters we have
	# Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
	checksum = Checksum.generate_checksum(paytmParams, '4&qx&s#LDfX9HRB8')
	paytmParams['CHECKSUMHASH']=(checksum)

	return render(request,'base/proceed.html',paytmParams)


@csrf_exempt
def callback(request):
	
	if request.method == 'POST':
		received_data = dict(request.POST)
		paytmParams = {}
		paytmChecksum = ""
		for key, value in received_data.items():
			if key == 'CHECKSUMHASH':
				paytmChecksum = value[0]
				# [0] is used because dict() returns dictionary like this -> {'key1':['value1'],'key2':['value2]}
			else:
				paytmParams[key] = value[0]
        # Verify checksum
		is_valid_checksum = Checksum.verify_checksum(paytmParams, "4&qx&s#LDfX9HRB8", str(paytmChecksum))
		if is_valid_checksum:
			received_data['message'] = "Checksum Matched"
		else:
			received_data['message'] = "Checksum Mismatched"
	return render(request, 'base/callback.html', context=received_data)

		


