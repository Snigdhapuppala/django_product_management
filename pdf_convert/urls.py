from django.urls import path
from . import views
urlpatterns = [
    path('showproducts', views.show_products, name='showproducts'),
    path('CreatePdf', views.pdf_report_create, name='createpdf'),
]
