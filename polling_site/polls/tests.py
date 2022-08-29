import datetime
from time import time
from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.urls import reverse


class QuestionModelTests(TestCase):
    # To test the was_published_recently (polls/models.py) method, if it returns the correct answer, if the question is published in a future date
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    # To test the was_published_recently (polls/models.py) returns false for questions whose pub_date is oolder than 1 day
    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days =1, seconds=1 )
        old_question = Question(pub_date = time)
        self.assertIs(old_question.was_published_recently(), False)

    # To test if was_published_recently (polls/models.py) returns True for questions whose pub_date is within the last day.
    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

# To create a question wih the given "question_text" and published the given number of 'days' offset to now (negative for questions published in the past, positive for questions that have yet to be published).
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,pub_date=time)

class QuestionIndexViewTests(TestCase):
    # Tests, if no question exist, an appropriate message is displayed
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    # To test if questions with pub_date in the past are displayed on the index page.
    def test_past_question(self):
        question = create_question(question_text = "past question.", days = -30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['lastest_question_list'], [question],)

    # To test if questions with pub_date in the future are not displayed on the index page.
    def test_future_question(self):
        create_question(question_text = "future question.", days = 30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['lastest_question_list'], [],)

    # To test when both future and past questions exists but only past questions are displayed on the index page.
    def test_future_question_and_past_question(self):
        question = create_question(question_text = "past question.", days = -30)
        create_question(question_text = "future question.", days = 30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['lastest_question_list'], [question],)

    # To test if index page, displays multiple questions.
    def test_two_past_question(self):
        question1 = create_question(question_text = "past question 1.", days = -30)
        question2 = create_question(question_text = "past question 2.", days = -10)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['lastest_question_list'], [question2, question1],)