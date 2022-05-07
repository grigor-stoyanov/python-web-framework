import logging

from django.db.models import Model

from demo.web.views import AppException, internal_error, InternalErrorView


def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code >= 500:
            # return internal_error()

            # level of logging hierarchy
            logging.critical('CRITICAL: tya e pesho')
            logging.error('INTERNAL ERROR: az sum pesho')
            logging.warning('WARNIGN: te sa pesho')
            logging.info('INFO: toi e pesho')
            logging.debug('DEBUG: nie sme pesho')

            return InternalErrorView.as_view()(request)
        return response

    return middleware
