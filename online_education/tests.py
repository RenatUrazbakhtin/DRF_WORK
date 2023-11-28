from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from online_education.models import Lesson, Course, Subscription
from users.models import User


# Create your tests here.
class LessonsTestCase(APITestCase):
    def setUp(self):
        self.course = Course.objects.create(title='check')

        self.user = User.objects.create(email='check123@mail.ru', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)

        self.lesson = Lesson.objects.create(title='check', course_cat=self.course, owner=self.user)


    def test_create_lesson(self):
        data = {
            "title": "testcase",
            "description": "testcase"
        }
        response = self.client.post(
            '/lesson/create/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_delete_lesson(self):
        lesson = Lesson.objects.create(
            title="testcase",
            description="testcase"
        )

        response = self.client.delete(
            f'/lesson/delete/{lesson.id}/',
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_list_lessons(self):
        response = self.client.get(
            '/lessons/',
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )


    def test_update_lessons(self):
        response = self.client.patch(
            f'/lesson/update/{self.lesson.pk}/',
            data={"title": "new"}
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_detail_lessons(self):
        response = self.client.get(
            f'/lesson/{self.lesson.pk}/',
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(response.json(), {
            "id": self.lesson.pk,
            "video_link": self.lesson.video_link,
            "title": self.lesson.title,
            "description": self.lesson.description,
            "preview": None,
            "owner": self.lesson.owner.pk,
            "course_cat": self.lesson.course_cat.pk
        })

class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.course = Course.objects.create(title='check')

        self.user = User.objects.create(email='check123@mail.ru', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)

        self.lesson = Lesson.objects.create(title='check', course_cat=self.course, owner=self.user)

    def test_create_subscription(self):
        data = {
            "course": self.course.pk,
            "is_subscriber": True
        }
        response = self.client.post(
            '/subscription/create/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

        self.assertEquals(response.json(),{
            "id": 1,
            "course": self.course.pk,
            "is_subscriber": True,
            "subscriber": self.user.pk
        })

    def test_delete_subscription(self):
        subscription = Subscription.objects.create(course=self.course)
        response = self.client.delete(
            f'/subscription/delete/{subscription.pk}/',
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )