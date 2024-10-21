from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from .models import Topic, Comment
from .serializers import TopicSerializer, CommentSerializer, RegisterSerializer


class TopicListGenericView(GenericAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def get(self, request):
        topics = self.get_queryset()
        topics_serializer = self.get_serializer(topics, many=True)
        return Response(topics_serializer.data)

    def post(self, request):
        topic_serializer: TopicSerializer = self.get_serializer(data=request.data)
        if topic_serializer.is_valid():
            topic = topic_serializer.save()
            context = {
                'message': "Mavzu yaratildi",
                'topic': self.get_serializer(topic).data
            }
            return Response(context, status=200)
        return Response(topic_serializer.errors, status=400)


class TopicDetailGenericView(GenericAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = 'pk'

    def get(self, request, pk):
        topic = self.get_object()
        topic_serializer = self.get_serializer(topic)
        return Response(topic_serializer.data)

    def put(self, request, pk):
        topic_serializer: TopicSerializer = self.get_serializer(data=request.data, partial=True)
        if topic_serializer.is_valid():
            topic = self.get_object()
            updated_topic = topic_serializer.update(instance=topic, validated_data=topic_serializer.validated_data)
            context = {
                'message': "Mavzu tahrirlandi",
                'topic': self.get_serializer(updated_topic).data
            }
            return Response(context)
        return Response(topic_serializer.errors, status=400)


class RegisterView(generics.CreateAPIView):
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class TopicListView(APIView):
    def get(self, request):
        topics = Topic.objects.all()
        topics_serializer = TopicSerializer(topics, many=True)
        return Response(topics_serializer.data, status=200)

    def post(self, request):
        topic_data = TopicSerializer(data=request.data)
        if topic_data.is_valid():
            topic_data.save()
            context = {
                'message': "Mavzu yaratildi",
                'topic': topic_data.data
            }
            return Response(context, status=200)
        return Response(topic_data.errors, status=400)


class TopicDetailView(APIView):
    def get(self, request, pk):
        try:
            topic = Topic.objects.get(pk=pk)
            return Response(TopicSerializer(topic).data, status=200)
        except Topic.DoesNotExist as e:
            return Response({'message': str(e)}, status=404)
        except Exception as e:
            return Response({'message': str(e)}, status=400)

    def put(self, request, pk):
        topic_data = TopicSerializer(data=request.data, partial=True)
        if topic_data.is_valid():
            try:
                topic = Topic.objects.get(pk=pk)
                updated_topic = topic_data.update(topic, topic_data.validated_data)
                context = {
                    'message': "Mavzu yangilandi",
                    'topic': TopicSerializer(updated_topic).data
                }
                return Response(context, status=200)
            except Topic.DoesNotExist as e:
                return Response({'message': str(e)}, status=404)
            except Exception as e:
                return Response({'message': str(e)}, status=400)
        return Response(topic_data.errors, status=400)

    def delete(self, request, pk):
        try:
            Topic.objects.get(pk=pk).delete()
            return Response({'message': "Mavzu o'chirildi"}, status=200)
        except Topic.DoesNotExist as e:
            return Response({'message': str(e)}, status=404)


class CommentListView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        comments_serializer = CommentSerializer(comments, many=True)
        return Response(comments_serializer.data, status=200)

    def post(self, request):
        comment_data = CommentSerializer(data=request.data)
        if comment_data.is_valid():
            comment_data.save()
            context = {
                'message': "Izoh yaratildi",
                'comment': comment_data.data
            }
            return Response(context, status=200)
        return Response(comment_data.errors, status=400)


class CommentDetailView(APIView):
    def get(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            return Response(CommentSerializer(comment).data, status=200)
        except Comment.DoesNotExist as e:
            return Response({'message': str(e)}, status=404)
        except Exception as e:
            return Response({'message': str(e)}, status=400)

    def put(self, request, pk):
        comment_data = CommentSerializer(data=request.data, partial=True)
        if comment_data.is_valid():
            try:
                comment = Comment.objects.get(pk=pk)
                updated_comment = comment_data.update(comment, comment_data.validated_data)
                context = {
                    'message': "Izoh yangilandi",
                    'comment': CommentSerializer(updated_comment).data
                }
                return Response(context, status=200)
            except Comment.DoesNotExist as e:
                return Response({'message': str(e)}, status=404)
            except Exception as e:
                return Response({'message': str(e)}, status=400)
        return Response(comment_data.errors, status=400)

    def delete(self, request, pk):
        try:
            Comment.objects.get(pk=pk).delete()
            return Response({'message': "Izoh o'chirildi"}, status=200)
        except Comment.DoesNotExist as e:
            return Response({'message': str(e)}, status=404)


