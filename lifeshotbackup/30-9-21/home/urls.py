from django.contrib import admin
from django.urls import path, include
from home import views

# Django  admin header customization
admin.site.site_header = "Lifeshots Admin Dashboard"
admin.site.site_title = "Admin Login"
admin.site.index_title = "Welcome to Admin Portal"

# Home Urls are here
urlpatterns = [
    path('',views.index, name="home"),
    path('service<int:myid>',views.services, name="services"),
    path('service',views.services, name="service"),
    path('serviceshome',views.serviceshome, name="serviceshome"),
    path('signup',views.handleSignup, name="handleSignup"),
    path('login',views.handleLogin, name="handleLogin"),
    path('logout',views.handleLogout, name="handleLogout"),
    path('subscribe',views.subscribe, name="subscribe"),
    path('indo',views.indo, name="indo"),
    path('product',views.product, name="product"),
    path('livestream',views.livestream, name="livestream"),
    path('community',views.community, name="community"),
    path('experiment',views.experiment, name="experiment"),
    path('support',views.support, name="support"),
    path('unicafe',views.unicafe, name="unicafe"),
    path('blog',views.blog, name="blog"),
    path('myaccount',views.myaccount, name="myaccount"),
    path('productinfo',views.productinfo, name="productinfo"),
    path('bloghome',views.bloghome, name="bloghome"),
    path('patenttechs',views.patenttechs, name="patenttechs"),
    path('franchise',views.franchise, name="franchise"),
    ]

