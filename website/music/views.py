
from django.shortcuts import render, get_object_or_404
from .models import Album, song

def index(request):
    # connecting database
    all_albums = Album.objects.all()
    #Creaing dictionary
    context = {
        'all_albums': all_albums
    }
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404('Album does not exist')
    album = get_object_or_404(Album, pk=album_id)
    context = {
        'album': album
    }
    return render(request, 'music/detail.html', context)

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, song.DoesNotExist):
        context = {
            'album': album,
            'error_message': "You didnot select a valid song"
        }
        return render(request, 'music/detail.html', context)
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})


