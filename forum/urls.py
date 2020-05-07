from django.urls import path, include

from rest_framework.routers import DefaultRouter

from forum.views.user_views import VoterViewset
from forum.views.thread_views import ThreadViewset
from forum.views.poll_views import PollViewset

# Create a router and register our viewsets with it.
router = DefaultRouter()

router.register(r'voters', VoterViewset, base_name='voters')
router.register(r'threads', ThreadViewset, base_name='threads')
router.register(r'polls', PollViewset, base_name='polls')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]