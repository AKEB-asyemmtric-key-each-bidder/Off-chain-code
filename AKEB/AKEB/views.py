from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from AKEB.FileEditor.fileeditor import FileEditor


@api_view(['GET'])
def incrementNumberOfBidders(request):
    fileEditor = FileEditor()
    fileEditor.incrementNumberOfBidders()
    return Response(None, status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def submitBid(request):
    bid = request.data['bid']
    fileEditor = FileEditor()
    fileEditor.submitBid(bid)
    return Response(None, status=status.HTTP_201_CREATED)
