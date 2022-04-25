from rest_framework.renderers import JSONRenderer
import json
from rest_framework import status


class CustomRenderer(JSONRenderer):
    
    def render(self, request, accepted_media_type=None, renderer_context=None):
        print(request)
        status_code = renderer_context['response'].status_code
        response ={
            "responseCode":status_code,
            "responseMessage":"Fetched Data Successfully",
            "responseData": request
        }

        if not str(status_code).startswith('2'):
            response["status"] = "error"
            response["data"] = None
            try:
                response["message"] = request.data["detail"]
            except KeyError:
                response["data"] = request.data

        return super(CustomRenderer, self).render(response, accepted_media_type, renderer_context)


class UserRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        print(data)
        if 'ErrorDetail' in str(data):
            response = json.dumps({'responseCode':status.HTTP_400_BAD_REQUEST,'responseMessage':"Error in request",'responseError': data})
        else:
            response = json.dumps({'responseCode':status.HTTP_200_OK,'responseMessage':"Successfull",'responsedata': data})
        return response