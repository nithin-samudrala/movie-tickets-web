from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from user import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('post.url')),
    path('register/',user_views.register,name='register'),
    path('profile/',user_views.profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='user/password_change.html'),name='password_change'),
    path('password_change/done',auth_views.PasswordChangeDoneView.as_view(template_name='user/password_change_done.html'),name='password_change_done'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'),name='password_reset'),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)