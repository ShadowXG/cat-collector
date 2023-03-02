from django.shortcuts import render

# Create your views here.
# view functions mathc urls to code (like controllers in Express)
# define our home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')