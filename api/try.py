# from django.contrib.auth.models import User
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status, generics
# from .models import Book
# from .serializer import UserSerializer, BooKSerializer
# from rest_framework.permissions import IsAuthenticated, AllowAny



# class CreateUserView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]
    
    

# @api_view(['GET'])
# def get_users(request):
#     users = User.objects.all()
#     serializedData = UserSerializer(users, many=True).data
#     return Response(serializedData)
        

# # api for the books ============================
# # @api_view(['POST'])
# # def add_book(request):
# #     data = request.data
# #     serializer = BooKSerializer(data=data)
# #     if serializer.is_valid():
# #         serializer.save()
# #         return Response(serializer.data, status=status.HTTP_201_CREATED)
# #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BookListCreate(generics.ListCreateAPIView):
#     serializer_class = BooKSerializer
#     permission_classes = [IsAuthenticated]
    
#     def get_queryset(self):
#         user = self.request.user
#         return Book.objects.filter(owner=user)
    
#     def perform_create(self, serializer):
#         if serializer.is_valid():
#             serializer.save(owner=self.request.user)
#         else:
#             print(serializer.errors)
            
            
# class BookDelete(generics.DestroyAPIView):
#     serializer_class = BooKSerializer
#     permission_classes = [IsAuthenticated]
    
#     def get_queryset(self):
#         user = self.request.user
#         return Book.objects.filter(owner=user)


# @api_view(['GET'])
# def get_books(request):
#     books = Book.objects.all()
#     serializedData = BooKSerializer(books, many=True).data
#     return Response(serializedData)
    