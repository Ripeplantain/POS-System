from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('update-profile/', profile_page, name='update_profile'),
    path('add_users', register_view, name='add_users'),
    path('reset_password',auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"), name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_done.html"), name="password_reset_complete"),
]