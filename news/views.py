from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from .models import News, Comment
from Tatyana.settings import NO_PHOTO
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
from django.template.context_processors import csrf


@csrf_protect
def comment(request, news_id):
    response = True
    try:
        news = Comment.objects.create(
            author=request.POST['form-news-reply-name'],
            email=request.POST['form-news-reply-email'],
            news_id=news_id,
            message='<p>%s</p>' % request.POST['form-news-reply-message'],
        )
        try:
            news.reply_id = request.POST['form-news-reply-comment']
        except:
            news.reply_id = None
        news.save()
    except:
        response = False

    return JsonResponse(response, safe=False)


@csrf_protect
def news_detail(request, news_id):
    args = {}
    args.update(csrf(request))
    args['result'] = True

    news = News.objects.get(id=news_id)
    # print(photos)
    args['news'] = news
    _comments = Comment.objects.filter(news_id=news_id, allowed=True)
    # добавка чтобы реплика была адресно
    for _comment in _comments:
        if _comment.reply:
            _comment.message = "%s<a href='#%s'>%s</a>, %s" \
                               % (_comment.message[:3], _comment.reply.id, _comment.reply.author, _comment.message[3:])

    args['comments'] = _comments
    return render_to_response('news__detail.html', args)


@csrf_protect
def news_list(request):
    args = {}
    args.update(csrf(request))
    args['result'] = True
    news = News.objects.all()
    paginator = Paginator(news, 1)

    page = request.GET.get('page')
    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news_list = paginator.page(paginator.num_pages)

    

    # print(photos)
    args['news_list'] = news_list
    return render_to_response('news__list.html', args)
