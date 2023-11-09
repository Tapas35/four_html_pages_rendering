from django.shortcuts import render

# Create your views here.
def firstpage(request):
    return render(request,'page1.html')
def secondpage(request):
    return render(request,'page2.html')
def thirdpage(request):
    return render(request,'page3.html')
def fourthpage(request):
    return render(request,'page4.html')