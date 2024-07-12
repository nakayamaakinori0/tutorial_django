from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from .models import Question, Choice
from django.views import generic


# Create your views here.

"""
# the most basic view
# def index(request):
#   return HttpResponse("Hello, world, You're at the polls index.")

# the view that displays the latest 5 poll questions in the system, separated by commas, according to publication date
# def index(request):
#   latest_question_list = Question.objects.order_by("-pub_date")[:5]
#   print("latest_question_list: ", latest_question_list)
#   output = ", ".join([q.question_text for q in latest_question_list])
#   return HttpResponse(output)

# the view that uses the template system
# def index(request):
#   latest_question_list = Question.objects.order_by("-pub_date")[:5]
#   print("latest_question_list: ", latest_question_list)
#   template = loader.get_template("polls/index.html")
#   context = {
#     "latest_question_list": latest_question_list,
#   }
#   return HttpResponse(template.render(context, request))

# the view with render() function
def index(request):
  latest_question_list = Question.objects.order_by("-pub_date")[:5]
  print("latest_question_list: ", latest_question_list)
  context = {"latest_question_list": latest_question_list}
  return render(request, "polls/index.html", context)

# mock detail view
# def detail(request, question_id):
#   return HttpResponse("You're looking at question %s. " % question_id)

# simple detaile view
# def detail(request, question_id):
#   try:
#     question = Question.objects.get(pk=question_id)
#   except Question.DoesNotExist:
#     raise Http404("Question does not exist")
#   return render(request, "polls/detail.html", {"question": question})

# detail view with get_object_or_404() function
def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, "polls/detail.html", {"question": question})


# def results(request, question_id):
#   response = "You're looking at the results of question %s."
#   return HttpResponse(response % question_id)

def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, "polls/results.html", {"question": question})

# def vote(request, question_id):
  # return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST["choice"])
  except (KeyError, Choice.DoesNotExist):
    return render(
      request, "polls/detail.html",
      {
        "question": question,
        "error_message": "You didn't select a choice.",
      },
    )
  else:
    selected_choice.votes = F("votes") + 1
    selected_choice.save()
    print("question.id: ", question.id)
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
"""


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        print("question.id: ", question.id)
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
