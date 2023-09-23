import requests
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from abdm_integrator.exceptions import ABDMServiceUnavailable, ABDMGatewayError, CustomError
from abdm_integrator.hiu.const import HIUGatewayAPIPath, ABHA_EXISTS_BY_HEALTH_ID_PATH
from abdm_integrator.hiu.exceptions import HIUError
from abdm_integrator.hiu.models import ConsentRequest
from abdm_integrator.hiu.serializers.consents import ConsentRequestSerializer, GenerateConsentSerializer
from abdm_integrator.hiu.views.base import HIUBaseView
from abdm_integrator.utils import ABDMRequestHelper


class GenerateConsent(HIUBaseView):

    def post(self, request, format=None):
        serializer = GenerateConsentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        consent_data = serializer.data
        self.check_if_health_id_exists(consent_data['patient']['id'])
        gateway_request_id = self.gateway_consent_request_init(consent_data)
        consent_request = self.save_consent_request(gateway_request_id, consent_data, request.user)
        return Response(status=HTTP_201_CREATED,
                        data=ConsentRequestSerializer(consent_request).data)

    def check_if_health_id_exists(self, health_id):
        try:
            payload = {'healthId': health_id}
            response = ABDMRequestHelper().abha_post(ABHA_EXISTS_BY_HEALTH_ID_PATH, payload)
            if not response.get('status'):
                raise CustomError(
                    error_code=HIUError.CODE_PATIENT_NOT_FOUND,
                    error_message=HIUError.CUSTOM_ERRORS[HIUError.CODE_PATIENT_NOT_FOUND],
                    detail_attr='patient.id'
                )
        # TODO Remove below exception handling once addressed on abha side
        except requests.Timeout:
            raise ABDMServiceUnavailable()
        except requests.HTTPError as err:
            error = ABDMRequestHelper.gateway_json_from_response(err.response)
            raise ABDMGatewayError(error.get('code'), error.get('message'))


    def gateway_consent_request_init(self, consent_data):
        payload = ABDMRequestHelper.common_request_data()
        payload['consent'] = consent_data
        ABDMRequestHelper().gateway_post(HIUGatewayAPIPath.CONSENT_REQUEST_INIT, payload)
        return payload['requestId']

    def save_consent_request(self, gateway_request_id, consent_data, user):
        consent_request = ConsentRequest(user=user, gateway_request_id=gateway_request_id, details=consent_data)
        consent_request.update_user_amendable_details(consent_data['permission'], consent_data['hiTypes'])
        return consent_request
