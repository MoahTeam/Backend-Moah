# Generated by Django 4.2.3 on 2023-07-09 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diaries', '0002_diaryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='diaryimage',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='diaryimage',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='diary/None/2023/07/09'),
        ),
        migrations.DeleteModel(
            name='summer_note_model',
        ),
    ]