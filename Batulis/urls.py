

from django.contrib import admin
from django.urls import path
from my_blog import views
from account.views import daftar, loginPage , logoutUser, kirim
from projectUser.views import dashboard
from my_blog.models import Post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post, name='index'),
    path('buku/<slug:slug>', views.post_detail, name='post_detail'),
    path('slug/<slug:tag_slug>/', views.TagIndex.as_view(), name='tag_index_by'),
    path('kategori/filsafat', views.kategori_filsafat, name='filsafat'),
    path('kategori/sejarah', views.kategori_sejarah, name='sejarah'),
    path('kategori/sastra', views.kategori_sastra, name='sastra'),
    path('kategori/politik', views.kategori_politik, name='politik'),
    path('kategori/opini', views.kategori_opini, name='opini'),
    
    path('account/create', daftar, name='create'),
    path('account/login', loginPage, name='login'),
    path('logout', logoutUser, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('account/activation', kirim, name='aktivasi'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


