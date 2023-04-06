from django.urls import path


from .views import  HomePageView, ContactPageView, AboutPageView, PostDetailView, AddPostView, PostDeleteView, PostUpdateView,LandingPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name = 'index'),
    path('home/', HomePageView.as_view(), name = 'home'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name = 'detail'),
    path('detail/<int:pk>/update/', PostUpdateView.as_view(), name = 'update'),
    path('detail/<int:pk>/delete/', PostDeleteView.as_view(), name = 'delete'),
    path('contact/', ContactPageView.as_view(), name = 'contact'),
    path('about/', AboutPageView.as_view(), name ='about'),
    path('post/', AddPostView.as_view(), name = 'post'),
    
    
]




