from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Topic
from .serializers import TopicSerializers


class TopicListView(APIView):
    def get(self, request):
        topics = Topic.objects.all()
        topics_serializer = TopicSerializers(topics, many=True)
        return Response(topics_serializer.data, status=200)

    def post(self, request):
        topic_data = TopicSerializers(data=request.data)
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
            return Response(TopicSerializers(topic).data, status=200)
        except Topic.DoesNotExist as e:
            return Response({'message': str(e)}, status=404)
        except Exception as e:
            return Response({'message': str(e)}, status=400)

    def put(self, request, pk):
        topic_data = TopicSerializers(data=request.data, partial=True)
        if topic_data.is_valid():
            try:
                topic = Topic.objects.get(pk=pk)
                updated_topic = topic_data.update(topic, topic_data.validated_data)
                context = {
                    'message': "Mavzu yangilandi",
                    'topic': TopicSerializers(updated_topic).data
                }
                return Response(context, status=200)
            except Topic.DoesNotExist as e:
                return Response({'message': str(e)}, status=404)
            except Exception as e:
                return Response({'message': str(e)}, status=400)
        return Response(topic_data.errors, status=400)




