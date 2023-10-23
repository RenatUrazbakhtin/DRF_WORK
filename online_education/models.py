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

    course_cat = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course', verbose_name='курс урока', **NULLABLE)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

class Payments(models.Model):
    payment_choice = [('cash', 'Наличные'), ('bank_transfer', 'Перевод на счет')]

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='клиент', **NULLABLE)
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    payment_amount = models.PositiveIntegerField(verbose_name='стоимость', **NULLABLE)
    payment_method = models.CharField(choices=payment_choice, verbose_name='способ оплаты', **NULLABLE)



