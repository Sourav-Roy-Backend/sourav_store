from django.urls import path
from . import views
urlpatterns = [
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('review/', views.write_review, name='reviewpage'),
    
]