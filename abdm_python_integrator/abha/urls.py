from django.urls import path

from abdm_python_integrator.abha.views import abha_creation_views, abha_verification_views

abha_creation_urls = [
    path('api/generate_aadhaar_otp', abha_creation_views.GenerateAadhaarOTP.as_view(), name='generate_aadhaar_otp'),
    path('api/generate_mobile_otp', abha_creation_views.GenerateMobileOTP.as_view(), name='generate_mobile_otp'),
    path('api/verify_aadhaar_otp', abha_creation_views.VerifyAadhaarOTP.as_view(), name='verify_aadhaar_otp'),
    path('api/verify_mobile_otp', abha_creation_views.VerifyMobileOTP.as_view(), name='verify_mobile_otp'),
]

abha_verification_urls = [
    path('api/get_auth_methods', abha_verification_views.get_auth_methods, name='get_auth_methods'),
    path('api/generate_auth_otp', abha_verification_views.generate_auth_otp, name='generate_auth_otp'),
    path('api/confirm_with_mobile_otp', abha_verification_views.confirm_with_mobile_otp,
         name='confirm_with_mobile_otp'),
    path('api/confirm_with_aadhaar_otp', abha_verification_views.confirm_with_aadhaar_otp,
         name='confirm_with_aadhaar_otp'),
    path('api/search_health_id', abha_verification_views.search_health_id, name='search_health_id'),
    path('api/get_health_card_png', abha_verification_views.get_health_card_png, name='get_health_card_png'),
    path('api/exists_by_health_id', abha_verification_views.get_existence_by_health_id,
         name='exists_by_health_id'),
]

abha_urls = abha_creation_urls + abha_verification_urls
