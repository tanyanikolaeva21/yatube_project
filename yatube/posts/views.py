# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('Привет! я - Главная страница >:D')


def group_posts(request,slug):
    return HttpResponse('Группы')
