from django.shortcuts import render
from .models import *
url = 'http://localhost:8000'
# Create your views here.
def index(request):
    projectdata = projectdetail.objects.all()
    certificatedata = certificate.objects.all()
    return render(request , 'index.html' ,{'projectdata': projectdata,'certificatedata': certificatedata, 'url': url})

def projectDetailPage(request, sid):
    pageData = projectdetail.objects.filter(id=sid).first()
    print(pageData)
    return render(request, 'detailpage.html' ,{'pageData': pageData, 'url': url})