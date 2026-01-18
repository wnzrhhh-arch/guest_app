from django.contrib import admin
from django.urls import path
from books_app import views  # MUST be books_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow'),
    path('return/<int:book_id>/', views.return_book, name='return'),
]
