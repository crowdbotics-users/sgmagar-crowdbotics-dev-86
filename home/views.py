from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'spirit', 'url': 'http://pypi.python.org/pypi/spirit/1.7.0'},
	{'name':'askbot', 'url': 'http://pypi.python.org/pypi/askbot/0.10.2'},
	{'name':'django-guardian', 'url': 'http://pypi.python.org/pypi/django-guardian/1.4.9'},
	{'name':'django-allauth', 'url': 'http://pypi.python.org/pypi/django-allauth/0.34.0'},
    ]
    context = {
        'title': 'sgmagar-crowdbotics-dev-86',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
