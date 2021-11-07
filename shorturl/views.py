from django.conf import settings
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import  status
from rest_framework.response import Response
from .models import Short_URL
from .serializers import ShortUrlSerializer,ShortUrlSerializerview,ForAnonymousSerializer,EditUrlSerializer
from django.contrib.auth.models import User
from shorturl.models import randomurl

class ShortedUrls(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        cuser= User.objects.get(username= self.request.user)
        # urll=Short_URL.objects.order_by(("id").desc())
        url=Short_URL.objects.filter(currentuser=cuser)
        urlserializer = ShortUrlSerializerview(url, many=True)
        return Response(urlserializer.data)
"""
#for test: login and press get
"""

class Quickshort(APIView):
    def post(self, request):

        short=(settings.HOST_URL+ randomurl())
        s_url= Short_URL(short_url=short)
        data= {"currentuser":request, "main_url":request.data, "short_url":short}
        serializer= ForAnonymousSerializer( s_url,data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
# FOR TEST: 
# {
"main_url": "https://www.youtube.com/watch?v=JFadax8wtx8g55fExDAPXBsbV&index=19"
}
"""


class CustomizeShortUrl(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        if request.method=="POST":
            mainUrl=request.data["main_url"]

            givenshort=request.data["short_url"]
            if(givenshort==""):
                givenshort=randomurl()
            else:
                givenshort=givenshort.replace(' ', '-')
            
            short=(settings.HOST_URL+ givenshort)

            if(User.objects.filter(username= self.request.user)).exists():
                cuser= User.objects.get(username= self.request.user)
                s_url= Short_URL(currentuser=cuser)

                if Short_URL.objects.filter(main_url=mainUrl,currentuser=cuser).exists():
                    return Response( {"Alart: This Url is already Shorted. Check Your List."}, status=status.HTTP_400_BAD_REQUEST)
                
                data= {"currentuser":cuser, "main_url":mainUrl, "short_url":short}
                serializer= ShortUrlSerializer( s_url, data=data)

            else:
                 data= { "main_url":mainUrl, "short_url":short}
                 serializer= ShortUrlSerializer( data=data)
            
            if serializer.is_valid():
                serializer.save() 
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
# FOR TEST: {
"main_url": "https://www.youtube.com/watch?v=JFadax8wtx8g55fExDAPXBsbV&list=&index=19",
"short_url" : "SSG"}
"""

class EditShortUrl(APIView):
    permission_classes=[IsAuthenticated]
    def put(self, request, id):

        cuser= User.objects.get(username= self.request.user)
        if cuser.username!="Anonymous":
            selected_url= Short_URL.objects.get(id=id)
            givenshort=request.data['short_url']

            if(givenshort==""):
                givenshort=randomurl()
            else:
                givenshort=givenshort.replace(' ', '-')
            
            exact_short= settings.HOST_URL + givenshort

            data= {"short_url":exact_short}

            serializer= EditUrlSerializer( selected_url, data=data, partial=True)
            if serializer.is_valid():
                serializer.save() 
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response( {"Login Required from Regular User Account"}, status=status.HTTP_400_BAD_REQUEST)

"""
# FOR TEST: {
http://127.0.0.1:8000/api/editshorturl/<id>/
"main_url": "https://www.youtube.com/watch?v=JFadax8wtx8g55fExDAPXBsbV&list=&index=19",
"short_url" : "CodingWithMitch"}
"""

class DeleteShortUrl(APIView):
    permission_classes=[IsAuthenticated]
    def delete( self,request, id):
        cuser= User.objects.get(username= self.request.user)
        if cuser.username!="Anonymous":
            selected_url= Short_URL.objects.get(id=id)
            selected_url.delete()
            return Response({"Successfully Deleted"},status=status.HTTP_204_NO_CONTENT)
        return Response( {"Login Required from Regular User Account"}, status=status.HTTP_400_BAD_REQUEST)
"""
# FOR TEST: {
http://127.0.0.1:8000/api/deleteshorturl/<id>/
and press delete
"""

            
class Redirect(APIView):
    def get(self,request,shortUrl):
        short_link=settings.HOST_URL+ shortUrl
        url=(Short_URL.objects.get(short_url=short_link))
        redirectTo=url.main_url
        return redirect(redirectTo)
