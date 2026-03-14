from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView, Response

import os
from dotenv import load_dotenv

load_dotenv()
IGDB_TOKEN = os.getenv("IGDB_TOKEN")
class GetIGDBTokenView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response({"token": IGDB_TOKEN}, status=HTTP_200_OK)