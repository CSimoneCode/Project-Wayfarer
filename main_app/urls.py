from django.urls import path
from . import views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Static urls
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Profile/User urls
    path('profile/', views.profile, name='profile'),
    path('profile/add_profile/', views.add_profile, name='add_profile'),
    path('profile/update_profile/', views.update_profile, name='update_profile'),
    # Cities urls
    path('cities/', views.cities_index, name='cities_index'),
    path('cities/<int:city_id>/', views.cities_detail, name='cities_detail'),
    # Post urls
    path('cities/<int:city_id>/posts/add_post/', views.add_post, name='add_post'),
    path('posts/<int:posts_id>/', views.posts_detail, name='posts_detail'),
    path('posts/<int:posts_id>/delete_post/', views.delete_post, name='delete_post'),
    path('posts/<int:posts_id>/edit_post/', views.edit_post, name='edit_post'),
    # Comments urls
    path('cities/<int:city_id>/posts/<int:posts_id>/comments/add_comment', views.add_comment, name='add_comment'),
    path('cities/<int:city_id>/posts/<int:posts_id>/comments/<int:comment_id>/update_comment/', views.update_comment, name='update_comment'),
    path('posts/<int:posts_id>/comments/<int:comment_id>/delete_comment/', views.delete_comment, name='delete_comment'),
    # Auth
    path('registration/signup/', views.signup, name='signup'),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
