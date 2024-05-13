from django.shortcuts import render
from .forms import FeedbackForm
from .models import Product


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def contact_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,
                          'catalog/thank_you.html')
    else:
        form = FeedbackForm()

    return render(request, 'catalog/contact_form.html', {'form': form})


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/product_list.html', context)
