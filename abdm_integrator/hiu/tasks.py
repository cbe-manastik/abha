from abdm_integrator.exceptions import ABDMServiceUnavailable
from abdm_integrator.settings import app_settings


@app_settings.CELERY_APP.task(queue=app_settings.CELERY_QUEUE, bind=True, ignore_result=False,
                              autoretry_for=(ABDMServiceUnavailable,), retry_backoff=2, max_retries=3)
def process_hiu_consent_notification_request(self, request_data):
    from abdm_integrator.hiu.views.consents import GatewayConsentRequestNotifyProcessor
    GatewayConsentRequestNotifyProcessor(request_data).process_request()
