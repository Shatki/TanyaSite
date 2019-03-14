from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.contrib import auth
from .models import Menu
from experience.models import Course
from documents.models import Document
from Tatyana.settings import MENU_CHOICES, MENU_DEFAULT, TEMPLATE_PAGE_DEFAULT, TEMPLATE_DOCUMENTS, TEMPLATE_AWARDS, \
    TEMPLATE_NO_PAGE


def menu():
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
def about(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['photo'] = auth.get_user(request).photo
    # print(args['photo'])
    args['menus'] = menu()
    args['menu_default'] = MENU_DEFAULT

    args['courses'] = Course.objects.all().order_by('begin_date')

    # if request.user.is_authenticated():
    #    args['nickname'] = auth.get_user(request).nickname
    # args['form'] = UserCreationForm()
    return render_to_response(TEMPLATE_PAGE_DEFAULT, args)


def documents_dispatch(request, url):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['photo'] = auth.get_user(request).photo
    args['menus'] = menu()
    args['menu_default'] = MENU_DEFAULT
    template = TEMPLATE_DOCUMENTS
    args['page'] = ""
    args['documents'] = ""

    try:
        page = Menu.objects.get(url=url)
        docs = Document.objects.filter(page__url=url, allowed=True).order_by('-added')
        args['page'] = page
        args['documents'] = docs
    except:
        template = TEMPLATE_NO_PAGE
    # Вызов конструктор страниц

    return render_to_response(template, args)
