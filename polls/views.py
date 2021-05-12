from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Question, Choice, Realsimulation,Fandamental
from django.template import loader
from django.urls import reverse
from django.views import generic
from io import TextIOWrapper,StringIO
from django.db.models import F
import csv

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question

class ResultsView(generic.DetailView):
    model = Question
    template_name =  "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    
def realsimulation(request):
    
    stock = Realsimulation.objects.order_by("-date")[:12]

    condition = {
        'date':stock[0].date,
        'close__gt':F('bb'),
        'days150__gt':F('days200')
    }
    datas = Realsimulation.objects.all().filter(**condition)

    return render(request,"polls/real.html",{'datas': datas})

def fandamentals(request):

    condition = {
        'riekishihanki1__gt':100,
        'riekishihanki2__gt':100,
    }
    datas = Fandamental.objects.all().filter(**condition)

    return render(request,"polls/fanda.html",{'datas': datas})
