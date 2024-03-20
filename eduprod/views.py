from django.core import serializers
from django.shortcuts import render
from .models import Question
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    # Randomly select two questions
    questions = Question.objects.order_by('?')[:2]
    
    # Serialize the questions to JSON
    questions_json = serializers.serialize('json', questions)

    # Extracting categories from the Question model (assuming you have defined a category field)
    categories = Question.objects.values_list('category', flat=True).distinct()

    return render(request, 'eduprod/index.html', {
        'questions_json': questions_json,
        'categories': categories
    })