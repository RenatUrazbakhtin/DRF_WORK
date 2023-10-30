from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ViewSet

from online_education.models import Course, Lesson, Payments, Subscription
from online_education.paginators import CoursePaginator
from online_education.permissions import IsOwnerOrManager, IsStaff
from online_education.serializers import CourseSerializer, LessonSerializer, PaymentListSerializer, PaymentSerializer, \
    SubscriptionSerializer
from online_education.validators import URLValidator


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator
    def get_permissions(self):
        if self.action in ['delete', 'create']:
            permission_classes = [IsStaff]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsOwnerOrManager]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsStaff]
    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    pagination_class = CoursePaginator

    def get_queryset(self):
        user = self.request.user
        if self.request.user.groups.filter(name='moderators'):
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=user)

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrManager]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrManager]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsStaff]

class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentListSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method',)
    ordering_fields = ('payment_date',)


class PaymentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()

class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    def perform_create(self, serializer):
        subscription = serializer.save()
        subscription.subscriber = self.request.user
        subscription.save()


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()