from django.urls import path
 
from . import views
 
urlpatterns = [
    path('login',views.login,name='login'),
    path('getUser',views.getUser,name='getUser'),
    path('getProduct',views.getProduct,name='getProduct'),
    path('getOther',views.getOther,name='getOther'),
    path('editUser',views.editUser,name='editUser'),
    path('deleteUser',views.deleteUser,name='deleteUser'),
    path('editProduct',views.editProduct,name='editProduct'),
    path('deleteProduct',views.deleteProduct,name='deleteProduct'),
    path('editOther',views.editOther,name='editOther'),
    path('deleteOther',views.deleteOther,name='deleteOther'),
    path('addOther',views.addOther,name='addOther'),
    path('addUser',views.addUser,name='addUser'),
    path('addProduct',views.addProduct,name='addProduct'),
]