from django.shortcuts import render
from .models import *
# Create your views here.
def info(request):
    posts = Posts.objects.all()
    feature = Featured.objects.all()
    silder = MainSilder.objects.all()
    starts = StartSlider.objects.all()
    popular = Main_Popular.objects.all()
    second_popular = Popular.objects.all()
    latest = Main_Latest.objects.all()
    latest_info = Latest.objects.all()
    follow = Follow.objects.all()
    newsletter = NewsLetter.objects.all()
    addstart = Addstart.objects.all()
    tranding = Tranding.objects.all()
    context = {
        'posts':posts,
        'feature':feature,
        'silder':silder,
        'starts':starts,
        'popular':popular,
        'second_popular':second_popular,
        'latest':latest,
        'latest_info':latest_info,
        'follow':follow,
        'newsletter':newsletter,
        'addstart':addstart,
        'tranding':tranding
    }
    return render (request, 'index.html', context)
