from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .models import Masseur, MassageProduct, PostDetail
from .forms import PLFormCV

# Create your views here.
def home(request):
    query_masseur = Masseur.objects.all()[:3] # zabezpiecz do 3 uzytkownikow
    query_post_title = PostDetail.objects.all()[:4]
    massage_products = MassageProduct.objects.all()[:6]

    context = {'query_masseur': query_masseur,
               'massage_products': massage_products,
               'query_post_title': query_post_title}
    return render(request, 'home.html', context)

def masseur_detail(request, masseur_id):
    masseur = get_object_or_404(Masseur, pk=masseur_id)
    remainder_masseur = Masseur.objects.exclude(pk=masseur_id)
    query_masseur = Masseur.objects.all()[:3]  # zabezpiecz do 3 uzytkownikow
    query_post_title = PostDetail.objects.all()[:4]

    context = {'masseur': masseur,
               'remainder_masseur': remainder_masseur,
               'query_masseur': query_masseur,
               'query_post_title': query_post_title}
    return render(request, 'masseur_detail.html', context)

def blog_list(request):
    query_post = PostDetail.objects.all()
    query_post_title = PostDetail.objects.all()[:4]
    query_masseur = Masseur.objects.all()[:3]  # zabezpiecz do 3 uzytkownikow
    context = {'query_post': query_post,
               'query_masseur': query_masseur,
               'query_post_title': query_post_title}
    return render(request, 'blog_list.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(PostDetail, pk=post_id)
    query_masseur = Masseur.objects.all()[:3]  # zabezpiecz do 3 uzytkownikow
    query_post_title = PostDetail.objects.all()[:4]
    context = {'post': post,
               'query_post_title':query_post_title,
               'query_masseur':query_masseur}
    return render(request, 'post_detail.html', context)

def order_massage(request):
    massage_products = MassageProduct.objects.all()[:6]
    query_post_title = PostDetail.objects.all()[:4]
    query_masseur = Masseur.objects.all()[:3]  # zabezpiecz do 3 uzytkownikow
    context = {'massage_products':massage_products,
               'query_post_title':query_post_title,
               'query_masseur':query_masseur}
    return render(request, 'order_massage.html', context)

def polish_form_application(request):
    query_post_title = PostDetail.objects.all()[:4]
    query_masseur = Masseur.objects.all()[:3]  # zabezpiecz do 3 uzytkownikow
    if request.method == 'POST':
        pl_cv_form = PLFormCV(request.POST, request.FILES)
        if pl_cv_form.is_valid():
            pl_cv_form.save()
            return HttpResponseRedirect(reverse('app:thank_you_page_pl'))
    else:
        pl_cv_form = PLFormCV()

    context = {'pl_cv_form': pl_cv_form,
               'query_post_title': query_post_title,
               'query_masseur': query_masseur}
    return render(request, 'polish_form_application.html', context)

def thank_you_page_pl(request):
    return render(request, 'thank_you_page_pl.html')