
from django.test import TestCase
from twitter.views import userCanTweet, home
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
class SimpleTest(TestCase):

	def setUp(self):
		self.client = Client()

	def test_user_can_tweet(self):
		response = self.client.get(reverse("twitter:home"))
		self.assertEquals(response.status_code, 302)
		response = self.client.get(reverse("twitter:login"))
		self.assertEquals(response.status_code, 200)
		self.assertContains(response, "username")

	def test_login(self):
		user = User.objects.create_user(username='user', password='user')
		print user
		c = self.client.login(username='user', password='user')
		self.assertTrue(c)
		response = self.client.get(reverse("twitter:home"))
		self.assertEquals(response.status_code, 200)

