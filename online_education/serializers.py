from rest_framework import serializers

from online_education.models import Course, Lesson, Payments


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(source='course', many=True)
    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, instance):
        return instance.course.count()

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