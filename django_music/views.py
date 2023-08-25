from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from .forms import AlbumForm

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'album_detail.html', {'album': album})


def album_new(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'album_new.html', {'form': form})


def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album.save()
            return redirect('album_list')
    else:
        form = AlbumForm(instance=album)
        return render(request, 'album_edit.html', {'form': form})


def album_remove(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('album_list')