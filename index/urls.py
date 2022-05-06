from django.urls import  path

from index.views import FileUploadView

urlpatterns = [
    path('', FileUploadView.as_view(), name='file-upload'),

]
