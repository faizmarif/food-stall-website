from django.db import models
from django import forms

class Food(models.Model):
	name=models.CharField(max_length=30,null=True)
	price=models.IntegerField(default=0)
	descrip=models.TextField(null=True)
	per=models.CharField(max_length=30,null=True)
	image=models.ImageField(upload_to='media',null=True)


	def __str__(self):
		return self.name


class Order(models.Model):
	order_id = models.AutoField(primary_key=True,editable=False)
	cust_id=models.IntegerField('Mobile No.',null=True,)
	name=models.CharField('Customer Name',max_length=50,default="",)
	biryani=models.IntegerField('No. of biryani plates',default=0,)
	chicken=models.IntegerField('No. of packet of fried chicken',default=0,)
	chatni=models.IntegerField('No. of packet of chatni',default=0,)
	salad=models.IntegerField('No. of packet of salad',default=0,)
	address=models.TextField('Full Address',default="")

	def get_amount(self):
		return (self.biryani)*50 + (self.chicken)*75 + (self.chatni)*5 + (self.salad)*5

	
	amount=property(get_amount)
	def __str__(self):
		return "{}'s order".format(self.name)



