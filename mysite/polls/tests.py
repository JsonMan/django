"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import timezone
import datetime
from polls.models import Poll

class PollMethodTests(TestCase):
    
    def test_was_published_recently_with_future_poll(self):
        """
        was_published_recently() should return False for polls whose
        pub_date is in the future
        """
        future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_poll.was_published_recently(), False)

         
    def test_sum(self):
        self.assertEqual(1+1, 2)
        
    def test_aaaa(self):
        self.assertEqual(1+1+1, 3)
