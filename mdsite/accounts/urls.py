from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .import views

app_name = 'accounts'
urlpatterns = [
	path('register/',views.RegisterView.as_view(),name='register'),
	path('login/',auth_views.LoginView.as_view(template_name = "registration/login.html"),name='login'),
	path('logout/',auth_views.LogoutView.as_view(template_name = "registration/logout.html"),name='logout'),
	path('password_change/',auth_views.PasswordChangeView.as_view(template_name = "registration/password_change.html",
		success_url=reverse_lazy('accounts:password_change_done')),name='password_change'),
	path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name = "registration/password_change_done_custom.html"),name='password_change_done'),
	# path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
	# path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
	# path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
	# path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]