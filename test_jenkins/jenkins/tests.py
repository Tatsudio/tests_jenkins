from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse

# Create your tests here.
class TestJenkins(TestCase):

	def test_jenkins(self):
		url = reverse('jenkins.views.index')
		response = self.client.get(url,{})

		print "url: ", type(url), url
		print 'response: ', type(response.content), response
		print 'dasd ', response.content
		self.assertEquals(response.content, 'Test')