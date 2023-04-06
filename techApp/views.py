from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, FormView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.contrib import messages



# Create your views here.
class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context
    
    
class PostDetailView(DetailView):
    template_name = 'detail.html'
    model = Post


class AddPostView(FormView):
    template_name = 'addpost.html'
    form_class = PostForm
    success_url = '/home'
    
    def dispatch(self, request,  *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        new_object = Post.objects.create(
            image = form.cleaned_data['image'],
            title = form.cleaned_data['title'],
            discriptions = form.cleaned_data['discriptions'],  )
        messages.add_message(self.request, messages.SUCCESS, 'content successfully uploaded')
        return super().form_valid(form)
    
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'discriptions', 'image']
    template_name = 'update.html'
    success_url = '/'
    
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = '/'

class ContactPageView(TemplateView):
    template_name = "contact.html"
    
class LandingPageView(TemplateView):
    template_name = "index.html"
    
class AboutPageView(TemplateView):
    template_name = "about.html"
    