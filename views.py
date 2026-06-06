from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Favourite


def home(request):
    new_products = Product.objects.filter(is_new=True)
    products = Product.objects.all()
    return render(request, 'home.html', {
        'new_products': new_products,
        'products': products
    })


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    is_favourite = False
    if request.user.is_authenticated:
        is_favourite = Favourite.objects.filter(
            user=request.user,
            product=product
        ).exists()

    return render(request, 'product_detail.html', {
        'product': product,
        'is_favourite': is_favourite
    })


@login_required
def add_favourite(request, id):
    product = get_object_or_404(Product, id=id)

    fav, created = Favourite.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        fav.delete()

    return redirect('product_detail', id=id)


@login_required
def favourite_list(request):
    favourites = Favourite.objects.filter(user=request.user)
    return render(request, 'favourites.html', {'favourites': favourites})


from django.shortcuts import render, redirect

def contact(request):
    if request.method == "POST":
        return redirect('message_sent')

    return render(request, 'contact.html')


def message_sent(request):
    return render(request, 'message_sent.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def register_view(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    return render(request, 'register.html', {'form': form})