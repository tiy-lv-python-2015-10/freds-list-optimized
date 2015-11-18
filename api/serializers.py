from django.contrib.auth.models import User
from rest_framework import serializers
from posting.models import Post, State, City, Category, SubCategory, Favorite


class UserSerializer(serializers.HyperlinkedModelSerializer):
    post_set = serializers.HyperlinkedRelatedField(many=True,
                                                    queryset=Post.objects.all(),
                                                    view_name='api_post_detail_update')
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'post_set')


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'user', 'subcategory', 'phone', 'price', 'location')


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Favorite
        fields = ('id', 'user', 'post', 'favorited_at')

class Top50Serializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'description', 'favorite_set')