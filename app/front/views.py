from django.shortcuts import render

# Create your views here.
def front_view(request):
    return render(request, "form.html")