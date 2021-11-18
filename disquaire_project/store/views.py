from django.shortcuts import render
from .models import Album, Artist, Contact, Booking
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    # request albums
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    # then format the request.
    # note that we don't use album['name'] anymore but album.name
    # because it's now an attribute.
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
    template = loader.get_template('store/index.html')
    return HttpResponse(template.render(request=request))

def listing(request):
    albums = Album.objects.filter(available=True)
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
    return HttpResponse(message)

def detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    artists = " ".join([artist.name for artist in album.artists.all()])
    message = f"Le nom de l'album est {album.title}. Il a été écrit par {artists}"
    return HttpResponse(message)

def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        # title contains the query and query is not sensitive to case.
        albums = Album.objects.filter(title__icontains=query)

    if not albums.exists():
        albums = Album.objects.filter(artists__name__icontains=query)

    if not albums.exists():
        message = "Misère de misère, nous n'avons trouvé aucun résultat !"
    else:
        albums = [f"<li>{album.title}</li>" for album in albums]
        message = """
            Nous avons trouvé les albums correspondant à votre requête ! Les voici :
            <ul>
                {}
            </ul>
        """.format("</li><li>".join(albums))

    return HttpResponse(message)
