# Generated by Django 4.2.6 on 2023-10-23 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='course_cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='online_education.course', verbose_name='курс урока'),
        ),
    ]
