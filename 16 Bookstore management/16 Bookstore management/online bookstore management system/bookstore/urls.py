from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('Admin_login',views.admin_login_view,name='Admin'),
    path('Register',views.Register_view,name='register'),
    path('books',views.books_view,name='books'),
    path('cart/',views.cart_view,name='cart'),
    path('addcart/<int:pk>/',views.cart_Add,name='addcart'),
    path('add-book/', views.add_book, name='add_book'),
]
