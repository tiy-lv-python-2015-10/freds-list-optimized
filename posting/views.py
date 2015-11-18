from django.core.urlresolvers import reverse_lazy
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView
from posting.forms import PostForm
from posting.models import City, Post, State, Favorite


class ListCity(ListView):
    model = City
    queryset = City.objects.order_by('name')
    template_name = "posting/state_list.html"

    def get_context_data(self, **kwargs):
        context = super(ListCity, self).get_context_data(**kwargs)
        context['state'] = State.objects.all()
        return context


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('list_post')
    template_name = 'posting/post_create.html'


class ListTop50(ListView):
    queryset = Post.objects.annotate(favorite_count=Count('favorite')).order_by('-favorite_count')[:50]
    model = Post
    template_name = "posting/top50_list.html"