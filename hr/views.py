import requests
from django.http import request
from django.shortcuts import get_object_or_404, reverse, redirect, render
from django.views import generic
from django.conf import settings 
from django.http import HttpResponse
from hr.forms import RecruitmentForm
from hr.models import Recruitment


def send_camunda(request):
    headers = { 'Accept': 'application/json', 'Content-Type': 'application/json' }
    json_data = {'a_key': 'a_value'}
    response = requests.post('http://localhost:8080/engine-rest/process-definition/key/Process_18r3szz/start', headers=headers, json=json_data)

class RecruitmentView(generic.FormView):
    
    form_class = RecruitmentForm
    template_name = "recruitment.html"

    def get_success_url(self):
        return reverse('hr:recruitment')

    def form_valid(self, form):
        recruitment = form.save(commit=True)
        user = self.request.user
        form.instance.user = user
        form.save()
        return super(RecruitmentView, self).form_valid(form)