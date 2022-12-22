from django.urls import path

from MyReadingPal.home.views import home, register_page, login_page, logout_user, book_lists_page, my_book_list

urlpatterns = (
    path('', home, name='home'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('booklists/', book_lists_page, name='book lists'),
    path('mybooklist/', my_book_list, name='my book list'),
)
