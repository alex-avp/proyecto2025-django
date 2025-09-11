from django.urls import path
from users import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test_view, name='test'),

    # LISTA
    path('about/', views.about, name='about'),

    # CREATE
    path('create/', views.create_product, name="create-product-view"),

    # UPDATE & DELETE
    path('product/<int:pk>/edit/', views.update_product, name="edit-product"),
    path('product/<int:pk>/delete/', views.delete_product, name="delete-product"),
]
