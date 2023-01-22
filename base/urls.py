from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from base import views
from base.views import CategoryView, CategoryDetail, CategoryTitle

urlpatterns = [
    path('', views.home_page, name='home'),
    path('product/<slug:val>',CategoryView.as_view(),name='category'),
    path('product-details/<int:pk>',CategoryDetail.as_view(),name='product-details'),
    path('category-title/<val>', CategoryTitle.as_view(),name='category-title'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)