from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from core.watch_it import models, serializers
from rest_framework import status
from django.http import Http404
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from core.permission import AdminOrReadonly, ReviewUserOrReadOnly
from rest_framework.serializers import ValidationError

class ReviewView(ListAPIView):
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        try:
            content = models.Content.objects.get(pk=self.kwargs.get("pk"))
        except models.Content.DoesNotExist:
            raise Http404
        review = models.Review.objects.all().filter(content=content)
        return review

class ReviewCreate(CreateAPIView):
    serializer_class = serializers.ReviewSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return models.Review.objects.all()
    
    def perform_create(self, serializer):
        try:
            content = models.Content.objects.get(pk=self.kwargs.get("pk"))
        except models.Content.DoesNotExist:
            raise Http404
        logged_user = self.request.user
        review_queryset = models.Review.objects.filter(content=content, review_user=logged_user)
        if review_queryset.exists():
            raise ValidationError(detail="You have already reviewed this content")
        content.total_rating += serializer.validated_data['rating']
        content.count_rating += 1
        content.save()
        serializer.save(content=content, review_user=logged_user)

class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ReviewUserOrReadOnly]
    serializer_class = serializers.ReviewSerializer
    queryset = models.Review.objects.all()

    def perform_update(self, serializer):
        try:
            review = models.Review.objects.get(pk=self.kwargs.get("pk"))
        except models.Review.DoesNotExist:
            raise Http404
        review.content.total_rating += (serializer.validated_data['rating'] - review.rating)
        review.content.save()
        serializer.save()
    
    def perform_destroy(self, instance):
        instance.content.total_rating -= instance.rating
        instance.content.count_rating -= 1
        instance.content.save()
        instance.delete()


class StreamPlatformViewAV(APIView):
    permission_classes = [AdminOrReadonly]
    def get(self, request):
        platform_list = models.StreamPlatform.objects.all()
        serializer = serializers.StreamPlatformSerializer(platform_list, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.StreamPlatformSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class StreamPlatformDetailViewAV(APIView):
    permission_classes = [AdminOrReadonly]
    def get_object(self, pk):
        try:
            platform = models.StreamPlatform.objects.get(pk=pk)
            return platform
        except models.StreamPlatform.DoesNotExist as e:
            raise Http404

    def get(self, request, pk):
        platform = self.get_object(pk=pk)
        serializer = serializers.StreamPlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self, request, pk):
        platform = self.get_object(pk=pk)
        serializer = serializers.StreamPlatformSerializer(instance=platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        platform = self.get_object(pk=pk)
        platform.delete()
        return Response(data = {'message' : 'Platform deleted'}, status=status.HTTP_204_NO_CONTENT)


class ContentViewAV(APIView):
    permission_classes = [AdminOrReadonly]
    def get(self, request):
        content_list = models.Content.objects.all()
        serializer = serializers.ContentSerializer(content_list, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.ContentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class ContentDetailViewAV(APIView):
    permission_classes = [AdminOrReadonly]
    def get_object(self, pk):
        try:
            content = models.Content.objects.get(pk=pk)
            return content
        except models.Content.DoesNotExist as e:
            raise Http404

    def get(self, request, pk):
        content = self.get_object(pk=pk)
        serializer = serializers.ContentSerializer(content)
        return Response(serializer.data)
    
    def put(self, request, pk):
        content = self.get_object(pk=pk)
        serializer = serializers.ContentSerializer(instance=content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        content = self.get_object(pk=pk)
        content.delete()
        return Response(data = {'message' : 'Content deleted'}, status=status.HTTP_204_NO_CONTENT)


# class ReviewViewAV(APIView):
#     def get(self, request, pk):
#         try:
#             content = models.Content.objects.get(pk=pk)
#         except models.Content.DoesNotExist:
#             return Response({"detail" : "Content does not exist"}, status=status.HTTP_404_NOT_FOUND)
#         reviews = models.Review.objects.all().filter(content=content)
#         serializer = serializers.ReviewSerializer(reviews, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class ReviewCreateAV(APIView):
#     def post(self, request, pk):
#         try:
#             content = models.Content.objects.get(pk=pk)
#         except models.Content.DoesNotExist:
#             return Response({"detail" : "Content does not exist"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = serializers.ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(content=content)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
    
# class ReviewDetailViewAV(APIView):

#     def get_object(self, pk):
#         try:
#             review = models.Review.objects.get(pk=pk)
#             return review
#         except models.Review.DoesNotExist as e:
#             raise Http404

#     def get(self, request, pk):
#         review = self.get_object(pk=pk)
#         serializer = serializers.ReviewSerializer(review)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         review = self.get_object(pk=pk)
#         serializer = serializers.ReviewSerializer(instance=review, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors)

#     def delete(self, request, pk):
#         review = self.get_object(pk=pk)
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Same implimentaion with function based views

# @api_view(['GET', 'POST'])
# def list_content(request):
#     if request.method == 'GET':
#         content_list = models.Content.objects.all()
#         serializer = serializers.ContentSerializer(content_list, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = serializers.ContentSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def content_detail(request, pk):
#     try:
#         content = models.Content.objects.get(pk=pk)
#     except ObjectDoesNotExist as e:
#         return Response(data = {'data' : 'Content does not exist'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = serializers.ContentSerializer(content)
#         return Response(serializer.data)
    
#     if request.method == 'DELETE':
#         content.delete()
#         return Response(data = {'message' : 'Content deleted'}, status=status.HTTP_204_NO_CONTENT)
    
#     if request.method == 'PUT':
#         serializer = serializers.ContentSerializer(instance=content, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors)
