from django.urls import path, include
from rest_framework.routers import DefaultRouter
from legislatives.api.views import ParlamentViewSet, CommissionViewSet

# extends DefaultRouter in polity/urls.py
# define router for parlament viewset
router = DefaultRouter()
router.register(r'parlaments', ParlamentViewSet)
router.register(r'commissions', CommissionViewSet)

"""
router will create following urls:
    * /parlaments/
    * /parlaments/<pk>/
    * /commissions
    * /commissions/<pk>/
"""