"""API to check the service status"""
import falcon
import json

class ServiceCheck:
    """API to check the service status"""

    def on_get(self, request, response):
        """ Dummy Response"""
        try:
            response.status = falcon.HTTP_200
            response.body = json.dumps({"Response": "Running"})
        except Exception as ex:
            response.body = json.dumps({"errors": str(ex.args[0])})
            response.status = falcon.HTTP_500
            raise
