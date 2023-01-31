from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from base import views
from django.contrib.auth import views as auth_view


from base.forms import UserLoginForm, PasswordResetForm, PasswordChangeForm, MySetPasswordForm
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
    path('password_change/', auth_view.PasswordChangeView.as_view(template_name='password_change.html', form_class=PasswordChangeForm, success_url='/passwordchangedone'), name='password_change'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='passssword_change_done.html'), name='password_change_done'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

    #passwrord rest
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='password_reset.html', form_class=PasswordResetForm), name='password_reset'),
    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),

    #path('password_reset_confirm/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', ), name='password_reset_confirm'),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='password_rest_complete.html'), name='password_reset_complete'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)