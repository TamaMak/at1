from django.core import serializers
from django.shortcuts import render
from .models import Question
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

@login_required
def index(request):
    # Randomly select two questions
    questions = Question.objects.order_by('?')[:3]
    
    # Serialize the questions to JSON
    questions_json = serializers.serialize('json', questions)

    # Extracting categories from the Question model (assuming you have defined a category field)
    categories = Question.objects.values_list('category', flat=True).distinct()

    return render(request, 'eduprod/index.html', {
        'questions_json': questions_json,
        'categories': categories
    })

def submit_answer(request):
    if request.method == 'POST':
        user_answer = request.POST.get('answer')
        # Process the user's answer here
        return HttpResponse(f'Your answer: {user_answer}')
    else:
        return HttpResponse('Method not allowed')
