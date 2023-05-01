from django.urls import path
from admin_modernize import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('icon-tabler/', views.icon_tabler, name='icon-tabler'),
    path('sample-page/', views.sample_page, name='sample-page'),
    path('ui-alerts/', views.ui_alerts, name='ui-alert'),
    path('ui-buttons/', views.ui_buttons, name='ui-button'),
    path('ui-cards/', views.ui_card, name='ui-card'),
    path('ui-forms/', views.ui_forms, name='ui-form'),
    path('ui-typography/', views.ui_typography, name='ui-typography'),
   
   

    # Authentication
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/', views.user_logout_view, name='logout'),
    path('accounts/register/', views.registration, name='register'),
    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name="password_change_done" ),
    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
]
