from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.contrib import auth
from .models import Menu
from .constants import MENU_CHOICES, MENU_DEFAULT


# Create your views here.
def homepage(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['photo'] = auth.get_user(request).photo
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
                    href=submenu.url
                )
                collect.append(_choice)
        elem = dict(
            name=menu[1][0].upper()+menu[1][1:],  # Увеличим первую букву
            menu=menu[0],
            choices=collect
        )
        _menu.append(elem)
    args['menus'] = _menu
    args['menu_default'] = MENU_DEFAULT

    # if request.user.is_authenticated():
    #    args['nickname'] = auth.get_user(request).nickname
    # args['form'] = UserCreationForm()
    return render_to_response('index.html', args)
