from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.contrib import auth


# Create your views here.
def homepage(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['photo'] = auth.get_user(request).photo

    # if request.user.is_authenticated():
    #    args['nickname'] = auth.get_user(request).nickname
    # args['form'] = UserCreationForm()
    return render_to_response('index.html', args)
