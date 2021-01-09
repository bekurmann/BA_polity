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
from politicans.api.views import PoliticanViewSet
from legislatives.api.views import ( ParlamentViewSet, ParlamentMembershipViewSet, ParlamentMembershipRoleViewSet,
                                    CommissionViewSet, CommissionMembershipViewSet, CommissionMembershipRoleViewSet )

# PARLAMENT ROUTER: create router
router = routers.SimpleRouter()
router.register(r'parlaments', ParlamentViewSet, basename='parlaments')
# /parlaments/
# /parlaments/<pk>/
parlament_membership_router = routers.NestedSimpleRouter(router, r'parlaments', lookup='parlament')
parlament_membership_router.register(r'memberships', ParlamentMembershipViewSet, basename='parlament-memberships')
# /parlaments/<pk>/memberships/
# /parlaments/<pk>/memberships/<pk>
parlament_membership_role_router = routers.NestedSimpleRouter(parlament_membership_router, r'memberships', lookup='parlament_membership')
parlament_membership_role_router.register(r'roles', ParlamentMembershipRoleViewSet, basename='parlament-memberships-roles')
# /parlaments/<pk>/members/<pk>/roles/
# /parlaments/<pk>/members/<pk>/roles/<pk>/
commission_router = routers.NestedSimpleRouter(router, r'parlaments', lookup='parlament')
commission_router.register(r'commissions', CommissionViewSet, basename='commissions')
# /parlaments/<pk>/commissions/
# /parlaments/<pk>/commissions/<pk>/
commission_membership_router = routers.NestedSimpleRouter(commission_router, r'commissions', lookup='commission')
commission_membership_router.register(r'members', CommissionMembershipViewSet, basename='commission-members')
# /parlaments/<pk>/commissions/<pk>/members/
# /parlaments/<pk>/commissions/<pk>/members/<pk>/
commission_membership_role_router = routers.NestedSimpleRouter(commission_membership_router, r'members', lookup='commission_membership')
commission_membership_role_router.register(r'roles', CommissionMembershipRoleViewSet, basename='commission-member-roles')
# /parlaments/<pk>/commissions/<pk>/members/<pk>/roles/
# /parlaments/<pk>/commissions/<pk>/members/<pk>/roles/<pk>/

router.register(r'politicans', PoliticanViewSet)
# /politicans/ 
# /politicans/<pk>/

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
    # nested routes /parlaments/members
    path('api/v1/', include(parlament_membership_router.urls)),
    path('api/v1/', include(parlament_membership_role_router.urls)),
    # nested commissions / ...
    path('api/v1/', include(commission_router.urls)),
    path('api/v1/', include(commission_membership_router.urls)),
    path('api/v1/', include(commission_membership_role_router.urls)),
]

# media files

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # admin look customization
# # obsolete with django-admin-interface
# admin.site.site_header = "polity Admin"
# admin.site.site_title = "polity Admin Portal"
# admin.site.index_title = "Welcome to polity Portal"