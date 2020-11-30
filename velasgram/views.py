""" velasgram views"""

# Django
from django.http import HttpResponse

# Utilitis
from datetime import datetime
import json


def hello_world(request):
    """ Return a greeting. """
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')  # %b => mes ex Nov
    return HttpResponse(f'Oh, hi!, Current server time is {now}.')


def sorted_integers(request):
    """
        Respondemos a una URL del tipo ?numbers=52,45,78,45,77,77,77,5,-5
        Return a JSON Response with sorted integer
    """
    numbersList = [int(i) for i in request.GET['numbers'].split(',')]  # List Comprehension
    numbersList.sort()
    # numbersList = sorted(numbersList)

    # para la ejecución y en la consola puedo ver el valor de las variables, c para salir
    # import pdb; pdb.set_trace()

    data = {
        'status': 'OK',
        'numbers': numbersList,
        'message': 'Integers sorted successfully'
    }

    # json.dumps() => traduce un diccionario a un json
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )


def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = (f'Sorry {name[:1].upper() + name[1:]}, you are not alloweb here!')
    else:
        message = (f'Hello {name[:1].upper() + name[1:]}, welcome to Velasgram!')

    return HttpResponse(message)
