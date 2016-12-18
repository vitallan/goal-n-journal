from .models import Goal, Entry
from django.shortcuts import render

def index(request):
    latest_goals = Goal.objects.order_by('-year')[:1] # there must be an obviously better way
    if len(latest_goals) > 0:
        latest_goal = latest_goals[0]
    else:
        latest_goal = None
    context = {
        'goal' : latest_goal
    }
    return render(request, 'goal/index.html', context)
