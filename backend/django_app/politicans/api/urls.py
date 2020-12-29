from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from politicans.api.views import PoliticanViewSet

# extends DefaultRouter in polity/urls.py
# define router for politicans viewset
router = DefaultRouter()
router.register(r'politicans', PoliticanViewSet)

"""
router will create following urls:
    * /politicans/
    * /pliticans/<pk>/
"""
