from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    context = {
    "date": now.strftime('%A %d, %Y'),
    "time": now.strftime('%I:%M %p'),

    }
    return render(request, 'time_app/index.html', context)
