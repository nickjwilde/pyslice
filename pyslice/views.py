from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

import json

from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, "pyslice/home.html", None)

def about(request):
    return render(request, "pyslice/about.html", None)

def learn(request):
    return render(request, "pyslice/learn.html", None)

class ContactView(View):
    template_name = 'pyslice/contact.html'
    form_class = ContactForm
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        response_data = {}
        if form.is_valid():
            response_data['status'] = 'success'
            response_data['html'] = '<h2>Thanks!<h2>'
        else:
            response_data['status'] = 'failure'
            response_data['html'] = form.errors.as_ul()
        return HttpResponse(json.dumps(response_data), content_type="application/json")
