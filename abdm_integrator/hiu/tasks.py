from abdm_integrator.const import CELERY_TASK
from abdm_integrator.exceptions import ABDMServiceUnavailable
from abdm_integrator.settings import app_settings


@CELERY_TASK(queue=app_settings.CELERY_QUEUE, bind=True, ignore_result=False,
             autoretry_for=(ABDMServiceUnavailable,), retry_backoff=2, max_retries=3)
def process_hiu_consent_notification_request(self, request_data):
    from abdm_integrator.hiu.views.consents import GatewayConsentRequestNotifyProcessor
    GatewayConsentRequestNotifyProcessor(request_data).process_request()


@CELERY_TASK(queue=app_settings.CELERY_QUEUE, bind=True, ignore_result=False)
def process_hiu_health_information_receiver(self, request_data):
    from abdm_integrator.hiu.views.health_information import ReceiveHealthInformationProcessor
    ReceiveHealthInformationProcessor(request_data).process_request()
