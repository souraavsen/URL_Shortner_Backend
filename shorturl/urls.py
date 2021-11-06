from django.urls import path

from shorturl.views import Quickshort,ShortedUrls,EditShortUrl,DeleteShortUrl,CustomizeShortUrl

urlpatterns = [
    path("quickshort/", Quickshort.as_view()),
    path("shortedurls/", ShortedUrls.as_view(), name="shortedurls"),
    path("shorturl/", CustomizeShortUrl.as_view(), name="Customizeshorturl"),
    path("editshorturl/<int:id>/", EditShortUrl.as_view(), name="editshorturl"),
    path("deleteshorturl/<int:id>/", DeleteShortUrl.as_view(), name="deleteshorturl"),

]

"""
# Endpoints:
http://127.0.0.1:8000/api/shortedurls/
http://127.0.0.1:8000/api/quickshort/
http://127.0.0.1:8000/api/shorturl/
http://127.0.0.1:8000/api/editshorturl/<int:id>/
http://127.0.0.1:8000/api/deleteshorturl/<int:id>/

"""