from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from guide import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^journeys', views.JourneyList.as_view()),
    url(r'^routes', views.RouteList.as_view()),
    url(r'^waypoints', views.WaypointList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
