from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from online_education.models import Course, Lesson, Payments, Subscription
from online_education.services import create_session_and_take_url
from online_education.validators import URLValidator


class LessonSerializer(serializers.ModelSerializer):
    video_link = serializers.CharField(validators=[URLValidator()], required=False)

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    subscription = serializers.SerializerMethodField()
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(source='course', many=True, read_only=True)

    payment_url = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = '__all__'

    def get_subscription(self, value):
        try:
            print(Subscription.objects.get(subscriber=value.id))
            subscription = Subscription.objects.get(
                course=value.id,
                subscriber=self.context['request'].user.id,
            )
        except ObjectDoesNotExist:
            return False

        else:
            return subscription.is_subscriber


    def get_lesson_count(self, instance):
        return instance.course.count()

    def get_payment_url(self, instance):
        return create_session_and_take_url(instance)


class PaymentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if instance.paid_course:
            course = CourseSerializer(instance.paid_course).data
            data['course'] = course
        elif instance.paid_lesson:
            lesson = CourseSerializer(instance.paid_lesson).data
            data['lesson'] = lesson

        return data


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
