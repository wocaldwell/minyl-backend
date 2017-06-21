from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from miapi import views
from miapi.views import register_view, micollection_view, login_view, release_view, user_release_view, artist_view, track_view, track_release_view, search_track_view, miwants_view, update_user_release_view, release_details_view, delete_user_release_view, env_keys_view, arrivedry_env_view

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/', login_view.login_user),
    url(r'^register/', register_view.register_user),
    url(r'^release/', release_view.ReleaseView.as_view({'post': 'add_release'})),
    url(r'^userrelease/', user_release_view.AddUserReleaseView.as_view({'post': 'add_user_release'})),
    url(r'^trackrelease/', track_release_view.AddTrackReleaseView.as_view({'post': 'add_track_release'})),
    url(r'^track/', track_view.AddTrackView.as_view({'post': 'add_track'})),
    url(r'^artist/', artist_view.AddArtistView.as_view({'post': 'add_artist'})),
    url(r'^micollection/', micollection_view.CollectionView.as_view({'get': 'collection_list'})),
    url(r'^miwants/', miwants_view.MiWantsView.as_view({'get': 'wants_list'})),
    url(r'^searchtrack/', search_track_view.SearchTrackView.as_view({'post': 'get_release_with_track'})),
    url(r'^updateuserrelease/', update_user_release_view.UpdateUserReleaseView.as_view({'post': 'update_user_release'})),
    url(r'^deleteuserrelease/', delete_user_release_view.DeleteUserReleaseView.as_view({'delete': 'delete_user_release'})),
    url(r'^releasedetails/', release_details_view.ReleaseDetailsView.as_view({'post': 'get_release_details'})),
    url(r'^envkeys/', env_keys_view.EnvKeysView.as_view({'get': 'get_env_keys'})),
    url(r'^arrivedrycreds/', arrivedry_env_view.ArriveDryEnvView.as_view({'get': 'get_arrivedry_keys'})),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
