from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.contrib import auth
from website.views import menu
from Tatyana.settings import MENU_DEFAULT, TEMPLATE_AWARDS


# Create your views here.
def awards(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['photo'] = auth.get_user(request).photo
    # print(args['photo'])
    args['menus'] = menu()
    args['menu_default'] = MENU_DEFAULT

    # if request.user.is_authenticated():
    #    args['nickname'] = auth.get_user(request).nickname
    # args['form'] = UserCreationForm()
    return render_to_response(TEMPLATE_AWARDS, args)
