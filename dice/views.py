from django.shortcuts import render
from random import randint, choice
from django.http import HttpResponse
import logging
from .models import CoinFlip

logger = logging.getLogger(__name__)


# Create your views here.


# def dice(request):
#     result = randint(1, 6)
#     logger.info(result)
#     return HttpResponse(result)
#
#
# def coin(request, amount_flips):
#     result = choice(('Head', 'Tails'))
#     logger.info(result)
#     CoinFlip(side=result).save()
#     last_results = CoinFlip.get_last_flips(amount_flips)
#     context = {
#         'current_flip': result,
#         'last_results': last_results
#     }
#     return render(request, 'dice/coin.html', context)
#
#
# def hundred(request):
#     result = randint(1, 100)
#     logger.info(result)
#     return HttpResponse(result)

def coin(request, amount_flips):

    # logger.info(result)
    #
    results = [choice(('Head', 'Tails')) for _ in range(amount_flips)]
    context = {
        'title': 'Монетка',
        'results': results
    }
    return render(request, 'dice/result.html', context)


def dice(request, amount_flips):
    results = [randint(1, 6) for _ in range(amount_flips)]

    # logger.debug(count)
    context = {'title': 'Кости', 'results': results}
    return render(request, 'dice/result.html', context)


def hundred(request, amount_gens):
    results = [randint(1, 100) for _ in range(amount_gens)]
    # logger.debug(count)
    context = {'title': 'Волшебная сотня', 'results': results}
    return render(request, 'dice/result.html', context)
