from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect

from website.views import menus
from users.models import User
from Tatyana.settings import MENU_DEFAULT, TEMPLATE_AWARDS
from .models import Award


# Create your views here.
@csrf_protect
def awards(request):
    args = {}
    args.update(csrf(request))
    if request.user.is_authenticated:
        args['username'] = auth.get_user(request).username
        args['profile'] = auth.get_user(request).photo

    args['photo'] = User.objects.get(is_superuser=True).photo
    # print(args['photo'])
    args['menus'] = menus()
    args['menu_default'] = MENU_DEFAULT

    args['awards'] = Award.objects.all().order_by('date')

    # if request.user.is_authenticated():
    #    args['nickname'] = auth.get_user(request).nickname
    # args['form'] = UserCreationForm()
    return render_to_response(TEMPLATE_AWARDS, args)
