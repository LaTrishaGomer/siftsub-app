from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'), 
    path('subscriptions/', views.subscription_index, name='subscription-index'),
    path('subscriptions/<int:subscription_id>/', views.subscription_detail, name='subscription-detail'),
    path('subscriptions/create/', views.SubscriptionCreate.as_view(), name='subscription-create'),
]


