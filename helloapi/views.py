from django.http import JsonResponse
from .models import Api
from .serializers import ApiSerializer

def api_list(request):
  #get all the api
  #serialize them
  #return json
  helloapi = Api.objects.all()
  serializer = ApiSerializer(helloapi, many=True)
  return JsonResponse(serializer.data, safe=False)