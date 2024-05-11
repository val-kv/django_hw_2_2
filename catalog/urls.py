from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home
from catalog.views import contacts
from . import views


app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('contacts/contact_form/', contacts, name='contact_form'),
path('product/<int:pk>/', views.product_detail, name='product_detail'),
]