from django.urls import path
from . import views
app_name='base'

urlpatterns=[
	path('',views.IndexView.as_view(),name='index'),
	path('info/',views.get_info,name='info'),
	path('proceed/<int:order_id>/<int:amount>/<int:cust_id>',views.proceed,name='proceed'),
	path('callback/',views.callback,name='callback')
]