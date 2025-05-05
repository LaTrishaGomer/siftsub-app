from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import SubscriptionCreate, SubscriptionUpdate, SubscriptionDelete



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'), 
    path('signin/', views.signin, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('subscriptions/<int:subscription_id>/', views.subscription_detail, name='subscription-detail'),
    path('subscriptions/create/', SubscriptionCreate.as_view(), name='subscription-create'),
    path('subscriptions/<int:pk>/edit/', SubscriptionUpdate.as_view(), name='subscription-update'),
    path('subscriptions/<int:pk>/delete/', SubscriptionDelete.as_view(), name='subscription-delete'),
]


