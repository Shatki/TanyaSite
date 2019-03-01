from django.contrib import auth
from django.shortcuts import render, render_to_response
from .models import Album, Photo

# Create your views here.

# Create your views here.
from django.template.context_processors import csrf


def gallery_list(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['photo'] = auth.get_user(request).photo
    albums = []
    for _object in Album.objects.all():
        album = dict(
            id=_object.id,
            name=_object.name,
            url=_object.url(),
            photo=Photo.objects.get(album_id=_object.id, label=True).photo
        )
        albums.append(album)

    args['albums'] = albums
    print(albums)
    # if request.user.is_authenticated():
    #    args['nickname'] = auth.get_user(request).nickname
    # args['form'] = UserCreationForm()
    return render_to_response('gallery_list.html', args)
