from django.urls.conf import path

from users.views import *

app_name = "users"

urlpatterns = [
    path('verify-email/<uidb64>/<token>/',
         VerifyEmail.as_view(), name="verify_email"),
    path('detail-<uuid>/', GetUserDetailsView.as_view(), name="user_details"),
    path('profile-<uuid>/', GetUserProfileDetailsView.as_view(),
         name="profile_details"),
    path('profile/address/update-<uuid>/',
         UpdateUserAddressView.as_view(), name="update_profile_address"),
    path('provinces/', GetProvinceListView.as_view(), name="provinces"),
    path('districts/', GetDistrictListView.as_view(), name="districts"),
    path('profile/update-<uuid>/',
         UpdateUserProfileView.as_view(), name="update_profile"),

    path('user-profile/create/<uuid>/',
         UserProfileCreateView.as_view(), name="user_profile_create"),
    path('org-profile/create/<uuid>/',
         OrganizationProfileCreateView.as_view(), name="org_profile_create"),

    path('register/', CreateUserView.as_view(), name="register_user"),

    path('candidate-cv/<uuid>/', GetUserCvView.as_view(), name="candidate_cv")
]
