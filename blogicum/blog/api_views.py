import io

from django.contrib.auth.models import User
from rest_framework import generics, mixins, viewsets
from django.forms import model_to_dict
from django.utils import timezone
from rest_framework import serializers, status
from rest_framework.decorators import api_view, action
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser, BasePermission, SAFE_METHODS
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from blog.models import Comment, Post, Category


# @api_view()
# def comment_example(request):
#     if request.method == 'GET':
#         return Response({'response': 'success'})


# @api_view(('POST', 'GET'))
# def comment_example(request):
#     print(request.data)
#     if request.method == 'GET':
#         return Response({'GET': 'success'})
#
#     if request.method == 'POST':
#         return Response({
#             **{'POST': 'success'},
#             **{'data': {**dict(request.data)}}
#         })


# @api_view(('POST', ))
# def comment_example(request):
#     print(request)
#     if request.method == 'POST':
#         post_id = request.data.get('post_id')
#         author_id = request.data.get('author_id')
#         text = request.data.get('text')
#
#         comment_ = Comment.objects.create(
#             # post_id=post_id,
#             post=Post.objects.get(id=post_id),
#             author_id=author_id,
#             text=text
#         )
#
#         return Response({
#             **{'POST': 'success'},
#             **{'comment': {**model_to_dict(comment_)}}
#         })


#
# class CommentSerializer(serializers.Serializer):
#     post_id = serializers.IntegerField()
#     author_id = serializers.IntegerField()
#     text = serializers.CharField()
#     created_at = serializers.DateTimeField(read_only=True)
#
#
# def encode_example():
#     comment_ = Comment.objects.first()
#     comment_serialized = CommentSerializer(comment_)
#     print(comment_serialized.data)
#     print(type(comment_serialized.data))
#     json = JSONRenderer().render(comment_serialized.data)
#     print(json)
#     print('###################')
#     data = JSONParser().parse(
#         stream=io.BytesIO(json)
#     )
#     comment_serializer = CommentSerializer(data=data)
#     comment_serializer.is_valid()
#     print(comment_serializer.validated_data)
#
#
# @api_view(('POST',))
# def comment_example(request):
#     if request.method == 'POST':
#         comment_serializer = CommentSerializer(data=request.data)
#         comment_serializer.is_valid(raise_exception=True)
#
#         data = comment_serializer.validated_data
#
#         post_id = data.get('post_id')
#         author_id = data.get('author_id')
#         text = data.get('text')
#         new_comment_ = Comment.objects.create(
#             post_id=post_id,
#             author_id=author_id,
#             text=text
#         )
#         comments_list = Comment.objects.all()
#
#         return Response({
#             **{'POST': 'success'},
#             **{'new_comment': CommentSerializer(new_comment_).data},
#             **{'all_comments': CommentSerializer(comments_list, many=True).data},
#         })


# class CommentSerializer(serializers.Serializer):
#     post_id = serializers.IntegerField()
#     author_id = serializers.IntegerField()
#     text = serializers.CharField()
#     created_at = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         return Comment.objects.create(**validated_data)
#
#
# @api_view(('POST', ))
# def comment_example(request):
#     if request.method == 'POST':
#         comment_serializer = CommentSerializer(data=request.data)
#         comment_serializer.is_valid(raise_exception=True)
#         comment_serializer.save()
#
#         comments_list = Comment.objects.all()
#
#         return Response({
#             **{'POST': 'success'},
#             **{'new_comment': comment_serializer.data},
#             **{'all_comments': CommentSerializer(comments_list, many=True).data},
#         })

# class CommentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     post_id = serializers.IntegerField()
#     author_id = serializers.IntegerField()
#     text = serializers.CharField()
#     created_at = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         return Comment.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.post_id = validated_data.get('post_id', instance.post_id)
#         instance.author_id = validated_data.get('author_id', instance.author_id)
#         instance.text = validated_data.get('text', instance.text)
#         instance.save()
#         return instance


# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
#
#
# @api_view(('POST', 'PUT', 'DELETE'))
# def comment_example(request):
#     if request.method == 'POST':
#         comment_serializer = CommentSerializer(data=request.data)
#         comment_serializer.is_valid(raise_exception=True)
#         comment_serializer.save()
#         return Response({
#             'POST': 'success',
#             'comment': comment_serializer.data}
#         )
#
#     if request.method in ('PUT', 'DELETE'):
#         pk = request.data.get('pk', None)
#         if not pk:
#             return Response({
#                 request.method: 'error',
#                 'error': f'Method {request.method} is not allowed or "pk" is required'
#             }, status=status.HTTP_400_BAD_REQUEST)
#
#         try:
#             instance = Comment.objects.get(id=pk)
#         except Comment.DoesNotExist:
#             return Response({
#                 request.method: 'error',
#                 'error': f'Object id={pk} does not exist'
#             }, status=status.HTTP_404_NOT_FOUND)
#
#         if request.method == 'PUT':
#             comment_serializer = CommentSerializer(instance=instance,
#                                                    data=request.data)
#             comment_serializer.is_valid(raise_exception=True)
#             comment_serializer.save()
#             return Response({
#                 'PUT': 'success',
#                 'comment': comment_serializer.data
#             })
#
#         if request.method == 'DELETE':
#             instance.delete()
#             return Response({
#                 'DELETE': 'success',
#                 'comment': model_to_dict(instance=instance)
#             })

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'


# class CommentAPIUpdate(generics.UpdateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
#
# class CommentAPIListCreate(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
#
# class CommentAPIGetPutDelete(mixins.RetrieveModelMixin,
#                              mixins.UpdateModelMixin,
#                              mixins.DestroyModelMixin,
#                              mixins.ListModelMixin,
#                              GenericAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = Post
        fields = '__all__'


class IsAdminOrAuthenticatedUser(BasePermission):
    def has_permission(self, request, view):
        if view.action in ('create', 'update', 'destroy'):
            return request.user.is_authenticated and request.user.is_staff
        return request.user.is_authenticated


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = ()
    # @action(methods=('get', ), detail=False)
    # def categories(self, request):
    #     categories_ = Category.objects.all()
    #     return Response({
    #         'categories': [c.title for c in categories_]
    #     })
    #
    # @action(methods=('get',), detail=True)
    # def category(self, request, pk=None):
    #     category = Category.objects.get(id=pk)
    #     return Response({
    #         'category': model_to_dict(category)
    #     })
#     #
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Post.objects.filter(is_published=True)
#         return Post.objects.get(id=pk)
