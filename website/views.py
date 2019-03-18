from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect

from users.models import User
from .models import Menu, Feedback
from experience.models import Course
from news.models import News, Comment, get_news
from gallery.models import Album, Photo
from pages.models import Document, Editor
from Tatyana.settings import MENU_CHOICES, MENU_DEFAULT, TEMPLATE_PAGE_DEFAULT, TEMPLATE_DOCUMENTS, TEMPLATE_NO_PAGE, \
    TEMPLATE_EDITOR, TEMPLATE_CONTACTS
from Tatyana.settings import DOCUMENT_PDF_MINIATURE, DOCUMENT_EXCEL_MINIATURE, DOCUMENT_POWERPOINT_MINIATURE, \
    DOCUMENT_WORD_MINIATURE, DOCUMENT_UNKNOWN_MINIATURE, NO_PHOTO
from Tatyana.settings import PPTX, PDF, PPT, XLS, XLSX, DOC, DOCX, UNKNOWN
from Tatyana.settings import DOCS, EDITOR, SPECIAL


def menus():
    menus = Menu.objects.all()
    _menu = []
    for menu in MENU_CHOICES:
        collect = []
        for submenu in menus:
            # print(submenu.menu, menu[0])
            if submenu.menu == menu[0]:
                # print(submenu.name)
                _choice = dict(
                    name=submenu.name,
                    url=submenu.get_url()
                )
                collect.append(_choice)
        elem = dict(
            name=menu[1][0].upper() + menu[1][1:],  # Увеличим первую букву
            menu=menu[0],
            choices=collect
        )
        _menu.append(elem)
    return _menu


# Create your views here.
@csrf_protect
def about(request):
    args = {}
    args.update(csrf(request))
    if request.user.is_authenticated:
        args['username'] = auth.get_user(request).username
        args['profile'] = auth.get_user(request).photo

    args['photo'] = User.objects.get(is_superuser=True).photo
    args['menus'] = menus()
    args['menu_default'] = MENU_DEFAULT
    args['news_list'] = []

    # Данные по курсам
    args['courses'] = Course.objects.all().order_by('begin_date')

    # Данные по новостям
    for news in get_news()[:3]:
        collect = dict(
            id=news.id,
            url=news.url,
            fix=news.fix,
            title=news.title,
            added=news.added,
            text=news.text,
            photo=news.photo,
            comments=0,
        )
        args['news_list'].append(collect)
    comments = Comment.objects.filter(allowed=True)
    for news in args['news_list']:
        for comment in comments:
            if news['id'] == comment.news.id:
                news['comments'] = news['comments'] + 1

    # Данные галлереи
    photos = []
    for _photo in Photo.objects.all().order_by('-added')[:6]:  # Нужно чтоб выдавал последние
        photo = dict(
            id=_photo.id,
            name=_photo.name,
            url=_photo.url(),
            photo=_photo,
            album=_photo.album.name,
        )
        photos.append(photo)
    args['photos'] = photos
    args['NO_PHOTO'] = NO_PHOTO

    # if request.user.is_authenticated():
    #    args['nickname'] = auth.get_user(request).nickname
    # args['form'] = UserCreationForm()
    return render_to_response(TEMPLATE_PAGE_DEFAULT, args)


def documents(args, url):
    args['documents'] = ""
    args['DOCUMENT_PDF_MINIATURE'] = DOCUMENT_PDF_MINIATURE
    args['DOCUMENT_EXCEL_MINIATURE'] = DOCUMENT_EXCEL_MINIATURE
    args['DOCUMENT_WORD_MINIATURE'] = DOCUMENT_WORD_MINIATURE
    args['DOCUMENT_POWERPOINT_MINIATURE'] = DOCUMENT_POWERPOINT_MINIATURE
    args['DOCUMENT_UNKNOWN_MINIATURE'] = DOCUMENT_UNKNOWN_MINIATURE
    args['PDF'] = PDF
    args['UNKNOWN'] = UNKNOWN
    args['PPT'] = PPT
    args['PPTX'] = PPTX
    args['XLS'] = XLS
    args['XLSX'] = XLSX
    args['DOC'] = DOC
    args['DOCX'] = DOCX
    template = TEMPLATE_DOCUMENTS
    try:
        docs = Document.objects.filter(page__url=url, allowed=True).order_by('-added')
        args['documents'] = docs
    except:
        return args, TEMPLATE_NO_PAGE
    # Вызов конструктор страниц
    return args, template


def editors(args, url):
    try:
        editor = Editor.objects.get(page__url=url, allowed=True)
        args['page'].text = editor.text
        args['page'].title = editor.title
        args['page'].header = editor.header.url
    except:
        return args, TEMPLATE_NO_PAGE
    return args, TEMPLATE_EDITOR


@csrf_protect
def page_dispatcher(request, menu, url):
    args = {}
    args.update(csrf(request))
    if request.user.is_authenticated:
        args['username'] = auth.get_user(request).username
        args['profile'] = auth.get_user(request).photo

    args['photo'] = User.objects.get(is_superuser=True).photo
    # общее меню
    args['menus'] = menus()
    args['menu_default'] = MENU_DEFAULT
    # переход с меню
    args['menu'] = menu
    args['page'] = ""
    try:
        page = Menu.objects.get(url=url)
        args['page'] = page
    except:
        pass

    template = TEMPLATE_NO_PAGE

    if args['page'].page == DOCS:
        args, template = documents(args, url)

    if args['page'].page == EDITOR:
        args, template = editors(args, url)

    return render_to_response(template, args)

@csrf_protect
def contacts(request):
    args = {}
    args.update(csrf(request))
    if request.user.is_authenticated:
        args['username'] = auth.get_user(request).username
        args['profile'] = auth.get_user(request).photo

    args['photo'] = User.objects.get(is_superuser=True).photo
    # общее меню
    args['menus'] = menus()

    return render_to_response(TEMPLATE_CONTACTS, args)


@csrf_protect
def feedback(request):
    message = Feedback.objects.create(
        name=request.POST['name'],
        email=request.POST['email'],
        subject=request.POST['subject'],
        message=request.POST['message'],
    )
    message.save()
    return JsonResponse(True, safe=False)
