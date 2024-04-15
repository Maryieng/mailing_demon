from typing import Any

from django.views.generic import DetailView, ListView

from blog.models import Blog


class BlogListView(ListView):
    """ Displaying a list of news """
    model = Blog
    template_name = "blog/index.html"


class BlogDetailView(DetailView):
    """ News card output """
    model = Blog

    def get_object(self, queryset=None) -> Any:
        """ function - view counter """
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object
