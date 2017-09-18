from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse
from .models import Post


class Aktualnosci(ListView):
    template_name = 'aktualnosci/list.html'
    model = Post

    def get_queryset(self):
        object_list = Post.objects.filter(status='publish')
        return object_list


class AktualnosciDetail(DetailView):
    template_name = 'aktualnosci/detail.html'
    model = Post


def test(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    context = {'post': post}
    return render(request, 'aktualnosci/detail.html', context)
