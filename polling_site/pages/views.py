from django.shortcuts import render

# Simply rendering our landing page here for our bare url/home page
def index(request):
    return render(request, 'pages/index.html')
