from rest_framework import status
from rest_framework.response import Response #redirect,render
from rest_framework.decorators import api_view

from haber_app.models import Makale
from haber_app.api.serializers import MakaleSerilazer

#class views
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class MakaleListCreateAPIView(APIView):
    def get(self,request):
      makaleler = Makale.objects.filter(aktif=True) #makale de ki aktif olan yazıları listeler(burda nesnelerdem oluşan bir qaru set var)
      serializer = MakaleSerilazer(makaleler, many=True) # 
      return Response(serializer.data)
    

    def post(self,request):
      serializer = MakaleSerilazer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status = status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class MakaleDetailAPIView(APIView):

    def get_object(self,pk):
        makale_instance = get_object_or_404(Makale,pk=pk)
        return makale_instance

    def get(self,request,pk):
        makale = self.get_object(pk=pk)
        serializer = MakaleSerilazer(makale)  
        return Response(serializer.data)        
    
    def put(self,request,pk):
        makale = self.get_object(pk=pk)
        serializer = MakaleSerilazer(makale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self,request,pk):
        makale = self.get_object(pk=pk)
        makale.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



















































### function view 

# @api_view(['GET','POST'])
# def makale_list_create_api_view(request):
   
#    if request.method =='GET':
#       makaleler = Makale.objects.filter(aktif=True) #makale de ki aktif olan yazıları listeler(burda nesnelerdem oluşan bir qaru set var)
#       serializer = MakaleSerilazer(makaleler, many=True) # 
#       return Response(serializer.data)
   
#    elif request.method == 'POST':
#       serializer = MakaleSerilazer(data=request.data)
#       if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data, status = status.HTTP_201_CREATED)
#       return Response(status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def makale_detail_api_view(request, pk):
#     try:
#         makale_instance = Makale.objects.get(pk=pk)
#     except Makale.DoesNotExist:
#         return Response(
#             {
#                 'errors': {
#                     'code': 404,
#                     'messages': f'Böyle bir id ({pk}) ile ilgili makale bulunamadı'
#                 }
#             },
#             status=status.HTTP_404_NOT_FOUND
#         )
    
#     if request.method == 'GET':
#         serializer = MakaleSerilazer(makale_instance)  # Doğru serializer adını kullan
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = MakaleSerilazer(makale_instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Hata durumunu gönder
    
#     elif request.method == 'DELETE':
#         makale_instance.delete()
#         return Response(
#             {
#                 'islem': {
#                     'code': 204,
#                     'messages': f'({pk}) id li makale silinmiştir'
#                 }
#             },
#             status=status.HTTP_204_NO_CONTENT
#         )