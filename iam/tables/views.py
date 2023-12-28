from django.core.serializers import serialize
import json
from .models import DNISTable

# Create your views here.
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import JsonResponse, HttpResponse


class DNISEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        dnis_query_set = DNISTable.objects.filter(dnis=kwargs['dnis'])
        if len(dnis_query_set):
            dnis_serialize = json.loads(serialize('json', dnis_query_set))[0]["fields"]
            return JsonResponse(dnis_serialize)
        return HttpResponse(status=404)
        
