from django.shortcuts import render
from deployementapp.models import Article

# Create your views here.
def demo(request):
    post=Article.objects.all()
    context={
        'post':post,
    }
    return render(request,'demo.html',context)