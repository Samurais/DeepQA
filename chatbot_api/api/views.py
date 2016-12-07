from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes

from .chatbotmanager import ChatbotManager

@api_view(['POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def question(request, format=None):
    '''
    Get question from body and return the answer.
    '''
    result = {}
    if request.data and 'message' in request.data:
        answer = ChatbotManager.callBot(request.data['message'])
        result['rc'] = 0
        result['msg'] = answer
    else:
        result['rc'] = 1
        result['errmsg'] = 'Invalid body in request.'
    return Response(result)
