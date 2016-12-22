from .models import Goal, Entry
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

def index(request):
    latest_goals = Goal.objects.order_by('-year')[:1] # there must be an obviously better way
    if len(latest_goals) > 0:
        return render(request, 'goal/index.html', {'goal' : latest_goals[0]})
    return render(request, 'goal/new-goal.html')

def log(request, goal_id):
    log = request.POST['log']
    hours_worked = request.POST['hours_worked']
    print(goal_id + " - " + log + " - " + hours_worked);
    goal = get_object_or_404(Goal, pk=goal_id)
    entry = Entry()
    entry.entry_date = timezone.now()
    entry.goal = goal
    entry.description = log
    entry.save()
    return HttpResponseRedirect(reverse('goal:index'))

def new_goal(request):
    goal_name = request.POST['goal_name']
    goal_year = request.POST['goal_year']
    goal = Goal()
    goal.name = goal_name
    goal.year = goal_year
    goal.save()
    return HttpResponseRedirect(reverse('goal:index'))

