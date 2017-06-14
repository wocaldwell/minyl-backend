from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from miapi import views
from miapi.views import register_view, micollection_view

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'releases', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^register/', register_view.register_user),
    url(r'^micollection/', micollection_view.get_user_collection),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
