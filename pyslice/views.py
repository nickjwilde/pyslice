from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View

import json

from .forms import ContactForm
from .models import Article

# Create your views here.
def home(request):
    return render(request, "pyslice/home.html", None)

def about(request):
    return render(request, "pyslice/about.html", None)

def learn(request):
    return render(request, "pyslice/learn.html", None)

def article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {'article': article}
    return render(request, "pyslice/article.html", context)

class ContactView(View):
    template_name = 'pyslice/contact.html'
    form_class = ContactForm
    
    def get(self, request):
        form = self.form_class(label_suffix='')
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, label_suffix='')
        response_data = {}
        if form.is_valid():
            response_data['status'] = 'success'
            response_data['html'] = "Thank you! Your response has been recorded. I will try to get back to you as soon as possible."
        else:
            response_data['status'] = 'failure'
            errors = []
            for key, error in form.errors.items():
                errors.extend(error.data)
            response_data['errors'] = "\n".join(str(x.message) for x in errors)
            print(response_data['errors'])
            #response_data['errors'] = form.errors.as_json(escape_html=True)
        return HttpResponse(json.dumps(response_data), content_type="application/json")
