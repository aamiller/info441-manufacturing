from django.urls import path
from . import views

app_name = 'auth'
urlpatterns = [
        path('signin', views.signin, name='signin'),
        path('signout', views.signout, name='signout'),
        path('register', views.register, name='register'),
        path('purchases/<int:purchase_id>', views.PurchaseView.as_view()),
        path('profile/<int:profile_id>', views.ProfileView.as_view()),
]