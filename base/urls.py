from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from base import views
from django.contrib.auth import views as auth_view

from base.forms import UserLoginForm, PasswordResetForm
from base.views import CategoryView, CategoryDetail, CategoryTitle, RegistrationView, ProfileView, UpdateAddress

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('product/<slug:val>',CategoryView.as_view(),name='category'),
    path('product-details/<int:pk>',CategoryDetail.as_view(), name='product-details'),
    path('category-title/<str:val>', CategoryTitle.as_view(), name='category-title'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/',views.address,name='address'),
    path('update_address/<int:pk>', views.UpdateAddress.as_view(), name='update_address'),



    #login authentication
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='login.html', authentication_form=UserLoginForm), name='login'),
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='password_reset.html', form_class=PasswordResetForm), name='password_reset'),

   # path('product/<str:title>/', product_detail, name='product_detail')
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)