from django.shortcuts import render
from django.views.generic import CreateView


class CreateService(CreateView):
    template_name = 'new_service.html'
    # model = Service
