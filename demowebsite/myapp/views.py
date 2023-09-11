from django.shortcuts import render

# Create your views here.
def about_nj_view(request):
	return render(request, "myapp/about_nj.html")