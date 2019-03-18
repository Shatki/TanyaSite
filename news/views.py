from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from .models import News, Comment
from Tatyana.settings import NO_PHOTO, PAGINATION_NEWS_ON_PAGE, PAGINATION_LIST_RANGE, MENU_DEFAULT
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from website.views import menus
from users.models import User

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
    if request.user.is_authenticated:
        args['username'] = auth.get_user(request).username
        args['profile'] = auth.get_user(request).photo

    args['photo'] = User.objects.get(is_superuser=True).photo
    args['menus'] = menus()
    args['menu_default'] = MENU_DEFAULT
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
    if request.user.is_authenticated:
        args['username'] = auth.get_user(request).username
        args['profile'] = auth.get_user(request).photo

    args['photo'] = User.objects.get(is_superuser=True).photo
    args['menus'] = menus()
    args['menu_default'] = MENU_DEFAULT
    args['result'] = True
    news = News.objects.all().order_by('-added')
    print(news)
    paginator = Paginator(news, PAGINATION_NEWS_ON_PAGE)

    page = request.GET.get('page')
    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news_list = paginator.page(paginator.num_pages)

    if paginator.num_pages > PAGINATION_LIST_RANGE * 2 + 1:
        list_start = news_list.number - PAGINATION_LIST_RANGE
        list_end = news_list.number + PAGINATION_LIST_RANGE

        if list_start < 1:
            list_start = 1
            list_end = PAGINATION_LIST_RANGE * 2 + 1

        if list_end > paginator.num_pages:
            list_start = paginator.num_pages - PAGINATION_LIST_RANGE * 2
            list_end = paginator.num_pages

        news_list.list_range = range(list_start, list_end + 1)
    else:
        news_list.list_range = range(1, paginator.num_pages + 1)

    args['news_list'] = news_list
    return render_to_response('news__list.html', args)
