import json
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Playlist


def entity_list(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlists/playlists_list.html', {'entities': playlists})


def entity_detail(request, id):
    playlist = get_object_or_404(Playlist, pk=id)
    return render(request, 'playlists/playlists_details.html', {'entity': playlist})


# {"name": "My Favorite Songs", "number_of_songs": 15}
@csrf_exempt
@require_http_methods(["POST"])
def entity_create(request):
    try:
        data = json.loads(request.body)
        playlist = Playlist.objects.create(**data)
        return JsonResponse({'id': playlist.id, 'status': 'Entity created successfully.'})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")
    except TypeError as e:
        return HttpResponseBadRequest(f"Error in input data: {e}")
    except ValidationError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except IntegrityError as e:
        return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def entity_delete(request, id):
    try:
        playlist = get_object_or_404(Playlist, pk=id)
        playlist.delete()
        return JsonResponse({'status': 'Entity deleted successfully.'})
    except Playlist.DoesNotExist:
        return JsonResponse({'error': 'Playlist not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
