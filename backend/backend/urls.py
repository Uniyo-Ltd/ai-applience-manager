from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from appliances.models import Appliance

def appliance_list(request):
    appliances = list(Appliance.objects.values())
    return JsonResponse(appliances, safe=False)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/appliances/', appliance_list),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)