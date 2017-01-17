import json

from django.http import JsonResponse
from django.views.generic import View, TemplateView

from .generator import gen

class IndexView(TemplateView):
    template_name = 'index.html'

class GeneratorView(View):
    def get(self, request, *args, **kwargs):
        response_data = {'data': gen()}
        return JsonResponse(response_data)
