from django.shortcuts import render
from random import randint, choice
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def dice(request):
    result = randint(1, 6)
    logger.info(result)
    return HttpResponse(result)


def coin(request):
    result = choice(('Head', 'Tails'))
    logger.info(result)
    return HttpResponse(result)


def hundred(request):
    result = randint(1, 100)
    logger.info(result)
    return HttpResponse(result)
