from django.urls import path

from app.views import ProductListView, Order_add, UserListView, user_orders, Login, user_logout, SignUp, \
    OrderListView, order_products, delivered, page_delivered

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('users', UserListView.as_view(), name='user_list'),
    path('orders', OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>', order_products, name='order'),
    path('delivered/<int:pk>', delivered, name='delivered'),
    path('delivered_page/', page_delivered, name='delivered_page'),
    path('user-orders/<int:pk>', user_orders, name='user_orders'),
    path('product/<int:pk>/', Order_add, name='order_add'),


    path('login/', Login.as_view(), name='login'),
    path('singup/', SignUp.as_view(), name='signin'),
    path('logout/', user_logout, name='logout'),
]