from django.urls import path
from authentication.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/42-intra/', Initiate42LoginView.as_view(), name='start_42_oauth'),
    path('login/credentials/', LoginView.as_view(), name='signin'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutAndBlacklistView.as_view(), name='logout'),
    path('callback/', UserAuthenticationView.as_view(), name='callback'),  # Where 42 will redirect back
    path('holder/', tokenHolderFor2faWith_42API.as_view(), name='holder_view'),
    path('get-access-token/', GetAccessTokenView.as_view()),
    path('health_checker/', health_checker, name='health_checker'),
    path('refresh/', RefreshAccessTokenView.as_view(), name='refresh_access_token'),
    path('check-2fa-status/', CheckTwoFactorStatusView.as_view(), name='check_2fa_status'),
    path('enable-2fa/', EnableTwoFactorView.as_view(), name='enable_twoFA'),
    path('disable-2fa/', DisableTwoFactorView.as_view(), name='disable_twoFA'),
    path('verify-2fa/', TwoFactorVerifyViewNewUser.as_view(), name='verify_2fa_token'),
    path('verify-2fa-old/', TwoFactorVerifyViewForOldUser.as_view(), name='verify_2fa_token_old'),
    path('status/', checkAuthStatus.as_view(), name='auth_status'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)