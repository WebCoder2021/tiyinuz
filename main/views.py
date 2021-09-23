from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Category, NewsType, New
import datetime


def home(request):
    category = Category.objects.all()
    new_type = NewsType.objects.all()
    news = New.objects.all()
    peak_news = news.filter(news_type = new_type[0])
    article = news.filter(news_type = new_type[1])
    interesting_information = news.filter(news_type = new_type[2])
    read_manys = news.order_by('views')
    read_many1 = read_manys[0]
    read_many = read_manys[1:10]
    date = datetime.datetime.today()
    print(new_type)
    print(interesting_information)

   
    content = {
        'date':date,
        'ctg':category,
        'peak_news': peak_news,
        'article': article, 
        'interest_info': interesting_information,
        'read_many':read_many,
        'read_many1':read_many1,
        

    }

    return render(request, 'index.html', content)

