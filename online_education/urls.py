from django.urls import path
from rest_framework.routers import DefaultRouter

import online_education
from online_education.apps import OnlineEducationConfig
from online_education.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PaymentListAPIView, PaymentUpdateAPIView, SubscriptionCreateAPIView, \
    SubscriptionDestroyAPIView

app_name = OnlineEducationConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='create-lesson'),
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-one'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

    path('payments/', PaymentListAPIView.as_view(), name='payment-list'),
    path('payments/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment-update'),

    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription-create'),
    path('subscription/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription-delete'),
] + router.urls