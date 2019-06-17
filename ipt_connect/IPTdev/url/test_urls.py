from django.test import Client
from IPTdev.url.parser import *

list_urls = list_url()

for i in list_urls:
   print  i, Client().get(i).status_code