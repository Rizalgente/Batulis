from django.shortcuts import render
from .models import Post, Kelompok
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from taggit.models import Tag

def post(request):
    if 'search'in request.GET:
        search=request.GET['search']
        post = Post.objects.filter(title__icontains=search)
    else:
        post = Post.objects.all()
    posts = Post.objects.all()[:3]
    paginator = Paginator(post,9)
    page = request.GET.get('page')

    try:
        post = paginator.page(page)

    except PageNotAnInteger:
        post = paginator.page(1)

    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    kelompok = Kelompok.objects.all()
    template = 'index.html'
    context = {
        'post': post,
        'page' : page,
        'posts' : posts,
        # 'paginator' : paginator,
        'kelompok' : kelompok,
    }
    return render(request, template, context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.all()[:3]
    kelompok = Kelompok.objects.all()
    template = 'detail.html'
    context = {
        'post': post,
        'posts' : posts,
        'kelompok' : kelompok,
     }
    return render(request, template, context)


# VIEW UNTUK KATEGORI
def kategori_filsafat(request):
    if 'search'in request.GET:
        search=request.GET['search']
        post = Post.objects.filter(title__icontains=search)
    else:
        post = Post.objects.filter(kategori__kelompok='Filsafat')
    posts = Post.objects.all()[:3]
    kelompok = Kelompok.objects.all()
    template = 'kategori_filsafat.html'

    paginator = Paginator(post,9)
    page = request.GET.get('page')

    try:
        post = paginator.page(page)

    except PageNotAnInteger:
        post = paginator.page(1)

    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    context = {
        'post' : post,
        'posts' : posts,
        'kelompok' : kelompok,
    }
    return render(request, template, context)

def kategori_sastra(request):
    if 'search'in request.GET:
        search=request.GET['search']
        post = Post.objects.filter(title__icontains=search)
    else:
        post = Post.objects.filter(kategori__kelompok='Sastra')
    posts = Post.objects.all()[:3]
    kelompok = Kelompok.objects.all()
    template = 'kategori_sastra.html'
    paginator = Paginator(post,9)
    page = request.GET.get('page')

    try:
        post = paginator.page(page)

    except PageNotAnInteger:
        post = paginator.page(1)

    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    context = {
        'post' : post,
        'posts' : post,
        'kelompok' : kelompok,
    }
    return render(request, template, context)

def kategori_sejarah(request):
    if 'search'in request.GET:
        search=request.GET['search']
        post = Post.objects.filter(title__icontains=search)
    else:
         post = Post.objects.filter(kategori__kelompok='Sejarah')
    posts = Post.objects.all()[:3]
    kelompok = Kelompok.objects.all()
    template = 'kategori_sejarah.html'
    paginator = Paginator(post,9)
    page = request.GET.get('page')

    try:
        post = paginator.page(page)

    except PageNotAnInteger:
        post = paginator.page(1)

    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    context = {
        'post' : post,
        'posts' : posts,
        'kelompok' : kelompok,
    }
    return render(request, template, context)
    

def kategori_politik(request):
    if 'search'in request.GET:
        search=request.GET['search']
        post = Post.objects.filter(title__icontains=search)
    else:
        post = Post.objects.filter(kategori__kelompok='Politik')
    posts = Post.objects.all()[:3]
    kelompok = Kelompok.objects.all()
    template = 'kategori_politik.html'
    paginator = Paginator(post,9)
    page = request.GET.get('page')

    try:
        post = paginator.page(page)

    except PageNotAnInteger:
        post = paginator.page(1)

    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    context = {
        'post' : post,
        'posts' : posts,
        'kelompok' : kelompok,
    }
    return render(request, template, context)

def kategori_opini(request):
    if 'search'in request.GET:
        search=request.GET['search']
        post = Post.objects.filter(title__icontains=search)
    else:
        post = Post.objects.filter(kategori__kelompok='Opini')
    posts = Post.objects.all()[:3]
    kelompok = Kelompok.objects.all()
    template = 'kategori_opini.html'
    paginator = Paginator(post,9)
    page = request.GET.get('page')

    try:
        post = paginator.page(page)

    except PageNotAnInteger:
        post = paginator.page(1)

    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    context = {
        'post' : post,
        'posts' : posts,
        'kelompok' : kelompok,
    }
    return render(request, template, context)

# FUNCTION SLUG KATEGORI

def kategori_slug(request, slug):
    post = Post.objects.all()
    kelompok = Kelompok.objects.get(slug=slug)
    template = 'kategori_slug.html'
    context = {
        'post': post,
        'kelompok' : kelompok,
     }
    return render(request, template, context)

# Tags
class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class ViewIndex(TagMixin, ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'post_list.html'
    context_object_name = 'post'

class TagIndex(TagMixin, ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'post'

    def get_tag(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('tag_slug'))
