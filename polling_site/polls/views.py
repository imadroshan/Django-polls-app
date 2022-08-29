from time import timezone
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

# To get recently published questions from models and display them on the front-end

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


# To show specific question and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', { 'question': question })


# To get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


# To vote for a question choice
def vote(request, question_id):
    # print(request.POST['choice']), it is the value taken from form in details.html -> input tag value
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplaying the question voting form
        return render(request, 'polls/detail.html', {
            'question':  question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # A tip that I want to save for later use: Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back Button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

# Making an API End Point for displaying the charts
def resultsData(request, obj_id):
    vote_data = []
    question = Question.objects.get(id=obj_id)
    votes = question.choice_set.all()
    for i in votes:
        vote_data.append({i.choice_text:i.votes})
    print(vote_data)
    return JsonResponse(vote_data, safe=False)

