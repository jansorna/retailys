from django.urls import path

from app.views import ProductCount, ProductList, SparePartsList

urlpatterns = [
    path("1", ProductCount.as_view(), name="product_count"),
    path("2", ProductList.as_view(), name="product_list"),
    path("3", SparePartsList.as_view(), name="spare_parts_list"),
]
