# Generated by Django 4.2.3 on 2023-07-13 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0008_alter_diaryimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaryimage',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='diary/2023.07.14'),
        ),
    ]