from django.http import JsonResponse
from django.shortcuts import render


def health_check(request):
    return JsonResponse({'message': 'OK'}, status=200)