from django.conf.urls import url
from api.views import DetailUpdatePost, ListCreatePost, ListUser, ListCreateFavorite, ListTop50
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^posts/(?P<pk>\d+)', DetailUpdatePost.as_view(), name='api_chirp_detail_update'),
    url(r'^posts/', ListCreatePost.as_view(), name='api_chirp_list_create'),
    url(r'^users/', ListUser.as_view(), name='api_user_list'),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^favorites/', ListCreateFavorite.as_view(), name='api_favorite_list_create'),
    url(r'^top/', ListTop50.as_view(), name='top_50_list'),
]