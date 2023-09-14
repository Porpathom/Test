from web.models import Subj, Cate
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {}
    subjs = Subj.objects.all()
    context['subjs'] = subjs
    return render(request, 'index.html', context)

def details(request, id):
    context ={}
    subjs = Subj.objects.filter(id=id)
    
    for subj in subjs :
        context['subj'] = subj
    
    return render(request, 'details.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)


def details_cate(request, id):
    context = {}
    cates = Cate.objects.get(id=id)
    subj = Subj.objects.filter(cate=cates).order_by('year', 'semester')    
    context['subj'] = subj
            
    return render(request, 'details_cate.html', context)

def category(request):
    context = {}
    subjs = Subj.objects.all()
    context['subjs'] = subjs
    return render(request, 'category.html',context)


