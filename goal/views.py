from .models import Goal, Entry
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


@login_required(login_url="/?unauthorized=True")
def index(request):
    latest_goals = Goal.objects.filter(user_id=request.user.id).order_by('-year')[:1]  # there must be an obviously
    # better way
    if len(latest_goals) > 0:
        goal = latest_goals[0]
        entries = Entry.objects.filter(goal=goal)
        return render(request, 'goal/index.html', {'goal': goal, "entries": entries})
    return render(request, 'goal/new-goal.html')


@login_required(login_url="/?unauthorized=True")
def log(request, goal_id):
    log = request.POST['log']
    hours_worked = request.POST['hours-worked']
    goal = get_object_or_404(Goal, pk=goal_id)
    entry = Entry(
        entry_date=timezone.now(),
        goal=goal,
        description=log,
        hours_worked=hours_worked
    )
    entry.save()
    return HttpResponseRedirect(reverse('goal:index'))


@login_required(login_url="/?unauthorized=True")
def new_goal(request):
    if request.method == "GET":
        return render(request, 'goal/new-goal.html', {'simple_new': True})
    goal_name = request.POST['goal-name']
    goal_year = request.POST['goal-year']
    goal = Goal(
        name=goal_name,
        year=goal_year,
        user_id=request.user.id
    )
    goal.save()
    return HttpResponseRedirect(reverse('goal:index'))


def home(request):
    return render(request, 'goal/home.html')


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('goal:home'))
