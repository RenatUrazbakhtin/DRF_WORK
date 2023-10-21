from django.db import models

from users.models import NULLABLE


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название курса')
    preview = models.ImageField(upload_to='Course/', verbose_name='превью курса', **NULLABLE)
    description = models.TextField(max_length=1000, verbose_name='описание', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название урока')
    description = models.TextField(max_length=1000, verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='Lesson/', verbose_name='превью урока', **NULLABLE)
    video_link = models.URLField(verbose_name='ссылка на видео', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

