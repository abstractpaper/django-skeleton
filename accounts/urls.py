from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm

login_view = auth_views.LoginView.as_view(
    template_name='accounts/login.html',
    authentication_form=LoginForm,
)

logout_view = auth_views.LogoutView.as_view(
    next_page=reverse_lazy('home'),
)

urlpatterns = [
    path('login/',                   login_view,                                               name='accounts-login'),
    path('logout/',                  logout_view,                                              name='accounts-logout'),
    # path('password_change/',         auth_views.PasswordChangeView.as_view(),                                           name='password_change'),
    # path('password_change/done/',    auth_views.PasswordChangeDoneView.as_view(),                                       name='password_change_done'),
    # path('password_reset/',          auth_views.PasswordResetView.as_view(),                                            name='password_reset'),
    # path('password_reset/done/',     auth_views.PasswordResetDoneView.as_view(),                                        name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',  auth_views.PasswordResetConfirmView.as_view(),                                     name='password_reset_confirm'),
    # path('reset/done/',              auth_views.PasswordResetCompleteView.as_view(),                                    name='password_reset_complete'),
]