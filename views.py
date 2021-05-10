from django.shortcuts import render




# Create your views here.
from django.shortcuts import render, redirect
from .models import Song
from .forms import SongCreate
from django.http import HttpResponse

def index(request):
    shelf = Song.objects.all()


    return render(request, 'l_app/library.html', {'shelf': shelf})


def upload(request):
    upload = SongCreate()
    if request.method == 'POST':
        upload = SongCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            #AType = upload.cleaned_data.get('audio_type')
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'l_app/upload_form.html', {'upload_form':upload})

def update_song(request, song_id):
    song_id = int(song_id)
    try:
        song_sel = Song.objects.get(id = song_id)
    except Song.DoesNotExist:
        return redirect('index')
    song_form = SongCreate(request.POST or None, instance = song_sel)
    if song_form.is_valid():
       song_form.save()
       return redirect('index')
    return render(request, 'l_app/upload_form.html', {'upload_form':song_form})

def delete_song(request, song_id):
    song_del=Song.objects.get(id=song_id)
    song_del.delete()
    shelf=Song.objects.all()
    return render(request, 'l_app/library.html', {'shelf': shelf})
    '''song_id = int(song_id)
    try:
        song_sel = Song.objects.get(id = song_id)
    except Song.DoesNotExist:
        return redirect('index')
    song_sel.delete()
    return redirect('index')'''
