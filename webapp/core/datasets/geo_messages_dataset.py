from django.core.serializers import serialize
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ..models import geoPointModel, geoCircleModel, geoPolygonModel

# Retrieve DAB dataset from the database (for the GIS/geomap)
@login_required
def geoPointDataset(request):
    all_objects = [*geoPointModel.objects.all()]
    geo_messages = serialize('geojson', all_objects)
    return HttpResponse(geo_messages, content_type='json')

@login_required
def geoCircleDataset(request):
    all_objects = [*geoCircleModel.objects.all()]
    geo_messages = serialize('geojson', all_objects)
    return HttpResponse(geo_messages, content_type='json')

@login_required
def geoPolygonDataset(request):
    all_objects = [*geoPolygonModel.objects.all()]
    geo_messages = serialize('geojson', all_objects)
    return HttpResponse(geo_messages, content_type='json')