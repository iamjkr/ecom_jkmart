from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from base import views
from base.views import CategoryView


urlpatterns = [
    path('', views.home_page, name='home'),
    path('category/<slug:val>',CategoryView.as_view(),name='category'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)