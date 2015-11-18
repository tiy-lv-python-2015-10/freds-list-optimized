from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework import generics, permissions, filters
from rest_framework.pagination import PageNumberPagination
from api.serializers import UserSerializer, PostSerializer, FavoriteSerializer, Top50Serializer
from posting.models import Post, Favorite
from api.permissions import IsOwnerOrReadOnly


class ListUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SmallPagination(PageNumberPagination):
    page_size = 5


class ListCreatePost(generics.ListCreateAPIView):
    queryset = Post.objects.order_by('-posted_at')
    serializer_class = PostSerializer
    pagination_class = SmallPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'description')


    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    def get_queryset(self):
        qs = super().get_queryset()
        username = self.request.query_params.get('username', None)
        if username:
            qs = qs.filter(author__username=username)

        keyword = self.request.query_params.get('keyword', None)
        if keyword:
            qs = qs.filter(title__icontains=keyword)
        return qs


class DetailUpdatePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


class ListCreateFavorite(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListTop50(generics.ListAPIView):
    queryset = Post.objects.annotate(favorite_count=Count('favorite')).order_by('-favorite_count')[:50]
    serializer_class = Top50Serializer
