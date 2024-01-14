# library_app/urls.py
from django.urls import path, include
from .views import LibraryListView, UserListView, PopulateLibraryDataView, RegisterView, LoginView, LogoutView
from .views import home_view, user_dashboard_view
from .api.views import BookListAPIView, CheckoutAPIView

urlpatterns = [
    path('library/', LibraryListView.as_view(), name='library'),
    path('user_list/', UserListView.as_view(), name='user_list'),
    path('populate-library/', PopulateLibraryDataView.as_view(), name='populate_library'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user-dashboard/', user_dashboard_view, name='user-dashboard'),
    path('home/', home_view, name='home'),
    path('api/', include([
        path('books/', BookListAPIView.as_view(), name='book-list'),
        path('checkout/', CheckoutAPIView.as_view(), name='checkout_api'),
    ]))
]