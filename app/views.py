from django.shortcuts import render
from .tasks import notify_customers


# Create your views he:re.
def say_hello(request):
    notify_customers.delay('hello')
   
    return render(request, 'hello.html', {'name': 'Richy'})