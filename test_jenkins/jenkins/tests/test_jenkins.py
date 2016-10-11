from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TransactionTestCase

class TestJenkins(TransactionTestCase):
	reset_sequences = True 

	def test_jenkins(self):
		url = reverse('jenkins.views.index')
		print "url: ", type(url), url