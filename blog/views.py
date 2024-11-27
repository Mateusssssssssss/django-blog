from django.core.paginator import Paginator
from django.shortcuts import render
from site_setup.models import SiteSetup

posts = list(range(1000))


def index(request):
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    site_setup = SiteSetup.objects.first() #lógica correta para buscar o objeto

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'site_setup': site_setup,
        }
    )


def page(request):
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    site_setup = SiteSetup.objects.first() #lógica correta para buscar o objeto

    return render(
        request,
        'blog/pages/page.html',
        {
            'site_setup': site_setup,
            # 'page_obj': page_obj,
        }
    )


def post(request):
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    site_setup = SiteSetup.objects.first() #lógica correta para buscar o objeto

    return render(
        request,
        'blog/pages/post.html',
        {
            'site_setup': site_setup
            # 'page_obj': page_obj,
        }
    )