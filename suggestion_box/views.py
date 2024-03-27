from django.shortcuts import render
from .models import Suggestion

# Create your views here.

def suggestion_box(request):
    suggestions = Suggestion.objects.all()
    return render(request, 'suggestion_box.html', {
        'suggestions': suggestions,
    })

def add_suggestion(request):
    if request.method == 'POST':
        suggestion_text = request.POST['suggestion']
        Suggestion.objects.create(text=suggestion_text)
    return render(request, 'suggestion_box.html', {
        'suggestions': Suggestion.objects.all(),
    })
