from django.shortcuts import render,redirect
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Book,cart
def home(request):
    return render(request,'home.html')
def register_view(request):
    if request.method =='POST':
        First_Name = request.POST['name']
        Email=request.POST['Email']
        username =request.POST['username']
        password =request.POST['password']
        confirmation_password =request.POST['confirm_password']
        select_user=request.POST['select_user']
        if select_user == 'admin':
            select_user=True
        else :
            select_user=False
        if password == confirmation_password:
            user = User.objects.filter(username=username)
            if user:
                messages.error(request,'username already exist use different')
                return redirect('register')
            else:
                user=User.objects.create_user(
                    username=username,
                    password=password,
                    email=Email,
                    first_name=First_Name,is_staff=select_user)
                user.save()
                messages.success(request,'created account successfully')
                return redirect('login')
        else:
            messages.error(request,'password should same password twice')
            return redirect('register')
    return render(request,'register.html')
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
           messages.error(request,'please check the details properly')
           return redirect('login')
    return render(request,'user.html')
def admin_login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"sorry you'r not admin/staff")
                return redirect('login')
        else:
           messages.error(request,'please check password | username')
           return redirect('Admin')
    return render(request,'admin.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def Register_view(request):
    if request.method =='POST':
        First_Name = request.POST['name']
        Email=request.POST['Email']
        username =request.POST['username']
        password =request.POST['password']
        confirmation_password =request.POST['confirm_password']
        select_user=request.POST['select_user']
        if select_user == 'admin':
            select_user=True
        else :
            select_user=False
        if password == confirmation_password:
            user = User.objects.filter(username=username)
            if user:
                messages.error(request,'username already exist use different')
                return redirect('register')
            else:
                user=User.objects.create_user(
                    username=username,
                    password=password,
                    email=Email,
                    first_name=First_Name,is_staff=select_user)
                user.save()
                messages.success(request,'created account successfully')
                return redirect('login')
        else:
            messages.error(request,'password should same password twice')
            return redirect('register')
    return render(request,'register.html')
def books_view(request):
    books =Book.objects.all()
    return render(request,'book.html',{'books':books})
def cart_view(request):
    Cart=cart.objects.filter(user=request.user)
    return render(request,'cart.html',{'Cart':Cart})
def cart_Add(request,pk):
    book=Book.objects.get(id=pk)
    if cart.objects.filter(user=request.user,book=pk).exists():
        return redirect('cart')
    else:
        Cart = cart.objects.create(user=request.user,book=book)
        Cart.save()
        return redirect('cart')
def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author_name = request.POST['author_name']
        price = request.POST['price']
        image = request.FILES['image']
        pdf=request.FILES['pdf']
        new_book = Book(title=title, author_name=author_name, price=price, image=image,pdf=pdf)
        new_book.save()
        return redirect('books') 
    return render(request, 'book_form.html')