from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def print_hello(request):
    dict = {"movies_list": [
        {'title': "Godfather",
            'year': 2000,
            'summary': "Oru cinema",
            'success': False
        },
        {'title': "6 aam thamburan",
            'year': 2002,
            'summary': "boom chika waw",
            'success': True
        },
        {'title': "ninte achanum achappavum",
         'year': 2005,
         'summary': "myr padam",
         'success': False
         },
        {'title': "mera dhosth mandan",
         'year': 1998,
         'summary': "potti potti potti",
         'success': False
         },
        {'title': "kazhinjille",
         'year': 2009,
         'summary': "paniu niruthunathaaakum budhi",
         'success': True
         }]}
    return render(request, 'hello.html', dict)
