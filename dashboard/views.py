from django.shortcuts import render

# Create your views here.
def home(request):
    template_name = 'dashboard/index.html'
    context = {
        "title": 'title name'
    }
    return render(request, template_name, context)

