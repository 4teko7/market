from django.conf.urls import url
from django.contrib import admin
from product.productViews import *
app_name = "productroutes"

urlpatterns = [
    url("addproduct/",addProduct,name = "addproduct"),
    url("myproducts/",myProducts,name = "myproducts"),
    url("productdetail/(?P<id>\d+)/",productDetail,name = "productdetail"),
    url("allproducts/",allProducts,name = "allproducts"),
    url("editproduct/(?P<id>\d+)/",editProduct,name = "editproduct"),
    url("deleteproduct/(?P<id>\d+)/",deleteProduct,name = "deleteproduct"),
    url("searchproduct/",searchProduct,name = "searchproduct"),
    url("allorders/",allOrders,name = "allorders"),


]