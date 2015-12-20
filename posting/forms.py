from django.forms import Textarea, ImageField
from posting.models import Post


class PostForm():
    class Meta:
        model = Post
        fields = ('title', 'description', 'phone', 'price', 'subcategory', 'images')
        widgets = {
            'description': Textarea(attrs={'rows': 2})
        }