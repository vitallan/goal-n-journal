from django.http import HttpResponse
from .models import Goal, Entry
from django.template import loader

def index(request):
    latest_goal = Goal.objects.order_by('-year')[:1] # there must be an obviously better way
    template = loader.get_template('goal/index.html')
    context = {
        'goal' : latest_goal[0]
    }
    return HttpResponse(template.render(context, request))
