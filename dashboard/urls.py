from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = "dashboard"

urlpatterns = [
    path('dashboard',views.index ,name="index"),
    path('staff/',views.staff,name="staff"),
    path('product/',views.product , name="product"),
    path('order/',views.order, name="order"),
    path('product/delete/<int:pk>/',views.product_delete ,name="product_delete"),
    path('product/update/<int:pk>/',views.product_update ,name="product_update"),
]