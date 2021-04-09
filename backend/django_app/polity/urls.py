from django.contrib import admin
from django.urls import path, include

# for media files
from django.conf.urls.static import static
from django.conf import settings

# import view for account registration confirmation
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView

# **************************************************************************************
# Router
# **************************************************************************************
# import router from 3rd party nested-routes
from rest_framework_nested import routers
from core.api.views import (    ParlamentViewSet, SessionViewSet,
                                PoliticanViewSet,
                                ParlamentMembershipViewSet, CommissionViewSet,
                                CommissionMembershipViewSet,
                                FractionViewSet )

from locations.api.views import ( CountryViewSet, RegionViewSet, CantonViewSet, 
                                    MunicipalityViewSet, NestedMunicipalityViewSet )

# PARLAMENT ROUTER
# **************************************************************************************
router = routers.SimpleRouter()
router.register(r'parlaments', ParlamentViewSet, basename='parlaments')
# /parlaments/
# /parlaments/<pk>/
parlament_membership_router = routers.NestedSimpleRouter(router, r'parlaments', lookup='parlament')
parlament_membership_router.register(r'memberships', ParlamentMembershipViewSet, basename='parlament-memberships')
# /parlaments/<pk>/memberships/
# /parlaments/<pk>/memberships/<pk>
parlament_session_router = routers.NestedSimpleRouter(router, r'parlaments', lookup='parlament')
parlament_session_router.register(r'sessions', SessionViewSet, basename='parlament-sessions')
# /parlament/<pk>/sessions/
# /parlament/<pk>/sessions/<pk>/
commission_router = routers.NestedSimpleRouter(router, r'parlaments', lookup='parlament')
commission_router.register(r'commissions', CommissionViewSet, basename='commissions')
# /parlaments/<pk>/commissions/
# /parlaments/<pk>/commissions/<pk>/
commission_membership_router = routers.NestedSimpleRouter(commission_router, r'commissions', lookup='commission')
commission_membership_router.register(r'memberships', CommissionMembershipViewSet, basename='commission-memberships')
# /parlaments/<pk>/commissions/<pk>/memberships/
# /parlaments/<pk>/commissions/<pk>/memberships/<pk>/

fraction_router = routers.NestedSimpleRouter(router, r'parlaments', lookup='parlament')
fraction_router.register(r'fractions', FractionViewSet, basename='fractions')
# /parlaments/<pk>/fractions/
# /parlaments/<pk>/fractions/<pk>/


# POLITICAN ROUTER
# **************************************************************************************
router.register(r'politicans', PoliticanViewSet)
# /politicans/ 
# /politicans/<pk>/

# LOCATION ROUTER
# **************************************************************************************
router.register(r'locations/countries', CountryViewSet, basename='countries')
# /locations/countries/
# /locations/countries/<pk>/
router.register(r'locations/regions', RegionViewSet, basename='regions')
# /locations/regions/
# /locations/regions/<pk>
router.register(r'locations/cantons', CantonViewSet, basename='cantons')
# /locations/cantons/
# /locations/cantons/<pk>
canton_municipality_router = routers.NestedSimpleRouter(router, r'locations/cantons', lookup='kantonsnum')
canton_municipality_router.register(r'municipalities', NestedMunicipalityViewSet, basename='canton-municipalities')
# /locations/cantons/<pk>/municipalities/
# /locations/cantons/<pk>/municipalities/<pk>/
router.register(r'locations/municipalities', MunicipalityViewSet, basename='municipalities')
# /locations/municipalities/
# /locations/municipalities/<pk>
# **************************************************************************************
# urls patterns
# **************************************************************************************

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    
    # browsable api; only for dev
    path('api/api-auth/', include('rest_framework.urls')),
    
    # authentication & registration
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    path('api/v1/auth/registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view(),), # Needs to be defined before the registration path
    path('api/v1/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/v1/auth/registration/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),

    # nested routes /parlaments
    path('api/v1/', include(router.urls)),
    # nested routes /parlaments/sessions
    path('api/v1/', include(parlament_session_router.urls)),
    # nested routes /parlaments/memberships
    path('api/v1/', include(parlament_membership_router.urls)),
    # nested commissions / ...
    path('api/v1/', include(commission_router.urls)),
    path('api/v1/', include(commission_membership_router.urls)),
    # nested fractions 
    path('api/v1/', include(fraction_router.urls)),

    # nested municipalities / cantons
     path('api/v1/', include(canton_municipality_router.urls)),
]

# **************************************************************************************
# media files
# **************************************************************************************

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)