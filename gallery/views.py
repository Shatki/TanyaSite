from django.contrib import auth
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect

from .models import Album, Photo
from Tatyana.settings import NO_PHOTO, MENU_DEFAULT
from website.views import menus
from users.models import User

# Create your views here.
from django.template.context_processors import csrf


@csrf_protect
def gallery_list(request):
    args = {}
    args.update(csrf(request))
    if request.user.is_authenticated:
        args['username'] = auth.get_user(request).username
        args['profile'] = auth.get_user(request).photo

    args['photo'] = User.objects.get(is_superuser=True).photo
    args['menus'] = menus()
    args['menu_default'] = MENU_DEFAULT
    args['result'] = True
    albums = []
    for _object in Album.objects.all():
        try:
            _photo = Photo.objects.get(album_id=_object.id, label=True)
        except:
            _photo = None
        else:
            _photo = _photo.photo.url
        album = dict(
            id=_object.id,
            name=_object.name,
            url=_object.url(),
            photo=_photo
        )
        albums.append(album)
    args['albums'] = albums
    args['NO_PHOTO'] = NO_PHOTO
    # if request.user.is_authenticated():
    #    args['nickname'] = auth.get_user(request).nickname
    # args['form'] = UserCreationForm()
    return render_to_response('gallery_list.html', args)


@csrf_protect
def gallery_detail(request, directory):
    args = {}
    args.update(csrf(request))
    if request.user.is_authenticated:
        args['username'] = auth.get_user(request).username
        args['profile'] = auth.get_user(request).photo

    args['photo'] = User.objects.get(is_superuser=True).photo
    args['menus'] = menus()
    args['menu_default'] = MENU_DEFAULT
    args['result'] = True
    try:
        album = Album.objects.get(directory=directory)
        photos = Photo.objects.filter(album=album)
        # print(photos)
        args['album'] = album
        args['photos'] = photos
    except:
        args['result'] = 'DB Query error: gallery'

    return render_to_response('gallery_detail.html', args)
