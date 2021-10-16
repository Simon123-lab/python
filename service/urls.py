from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.account_registration, name='account_registration'),
    path('login',views.account_login, name='account_login'),
    path('logout',views.logout_user, name='logout'),
    path('cpanel',views.client_panel, name='client_panel'),
    path('panel',views.user_panel, name='user_panel'),
    path('likes',views.post_likes, name='likes'),
    path('order',views.client_order, name='order'),
    path('videos',views.watch_videos, name='videos'),
    path('follows',views.page_follows, name='follows'),
    path('reviews',views.add_review, name='reviews'),
    path('entry',views.contest_submition, name='entry'),
    path('verify',views.confirm_views, name='verify')
]