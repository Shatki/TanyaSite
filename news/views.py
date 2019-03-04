from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from .models import News, Comment
from Tatyana.settings import NO_PHOTO

# Create your views here.
from django.template.context_processors import csrf


@csrf_protect
def comment(request, news_id):
    response = True
    #try:
    news = Comment.objects.create(
        author=request.POST['form-news-reply-name'],
        email=request.POST['form-news-reply-email'],
        news_id=news_id,
        message=request.POST['form-news-reply-message'],
    )
    news.save()
    #except:
    #    response = False

    return JsonResponse(response, safe=False)


@csrf_protect
def news_list(request):
    args = {}
    args.update(csrf(request))
    args['result'] = True
    return render_to_response('news__list.html', args)


@csrf_protect
def news_detail(request, news_id):
    args = {}
    args.update(csrf(request))
    args['result'] = True

    news = News.objects.get(id=news_id)
    # print(photos)
    args['news'] = news
    args['comments'] = Comment.objects.filter(news_id=news_id, allowed=True)
    return render_to_response('news__detail.html', args)
