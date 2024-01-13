# library_app/urls.py
from django.urls import path, include
from .views import library_list, user_list, populate_library_data, register_view, login_view, home_view
from .api.views import BookListAPIView, CheckoutAPIView

urlpatterns = [
    path('library/', library_list),
    path('users/', user_list),
    path('populate-library/', populate_library_data),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('', home_view, name='home'),
    path('api/', include([
        path('books/', BookListAPIView.as_view(), name='book-list'),
        path('checkout/', CheckoutAPIView.as_view(), name='checkout_api'),
    ]))
]