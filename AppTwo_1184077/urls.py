from django.conf.urls import url
from AppTwo_1184077 import views


urlpatterns =[
url (r'^$',views.help,name='help'),
]