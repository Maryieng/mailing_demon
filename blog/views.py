from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import DetailView, ListView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = "blog/index.html"


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object