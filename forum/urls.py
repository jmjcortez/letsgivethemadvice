from django.urls import path, include

from rest_framework.routers import DefaultRouter

from forum.views.user_views import VoterViewset
from forum.views.thread_views import ThreadViewset

# Create a router and register our viewsets with it.
router = DefaultRouter()

router.register(r'voters', VoterViewset, base_name='voters')
router.register(r'threads', ThreadViewset, base_name='threads')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]