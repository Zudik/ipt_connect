import unittest
from django.contrib.auth.models import User
from django.test import Client
from parser import list_url

l_url = list_url()
#c = Client()
#for i in range(len(ur)):
#    c.get(ur[i])

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        print self.client.get('IPTdev/teams/', {'name':'Brazil'}, follow=True).status_code
        for i in l_url:
            response = self.client.get(i)
            # Print url and status code
            #if (response.status_code != 200):
            print i, response.status_code

            # Check that the response is 200 OK.
            #self.assertEqual(response.status_code, 200)

