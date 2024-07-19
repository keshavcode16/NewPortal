from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

#local imports
from .exceptions import ProfileDoesNotExist
from .models import Profile
from .serializers import ProfileSerializer
import logging
logger = logging.getLogger("loggers")




class ProfileRetrieveAPIView(RetrieveAPIView):
    """
    This class contains view to retrieve a profile instance.
    Any user is allowed to retrieve a profile
    """

    permission_classes = (AllowAny,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.select_related('user')

    def retrieve(self, request, username, *args, **kwargs):
        try:
            profile = self.queryset.get(user__username=username)
            serializer = self.serializer_class(profile,)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            raise ProfileDoesNotExist(
                'A profile for user {} does not exist.'.format(username))
        except Exception as error:
            return Response({'error':f'Error in retriving profile detail {str(error)}'})



