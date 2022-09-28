from django.shortcuts import render
from post.forms import *
from post.models import *
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, FormView, ListView
from django.views.generic.detail import SingleObjectMixin

# Create your views here.
class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['form'] = CommentForm(initial={
            'post': self.object
        })

        return context_data

class PostCommentsFormView(SingleObjectMixin, FormView):
    template_name = "post_detail.html"
    form_class = CommentForm
    model = Post

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super(PostCommentsFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})

class PostView(View):

    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostCommentsFormView.as_view()
        return view(request, *args, **kwargs)

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"