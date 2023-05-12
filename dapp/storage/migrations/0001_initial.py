# Generated by Django 4.2.1 on 2023-05-11 13:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectArchiveModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.CharField(default='Не описано', max_length=120, verbose_name='Описание')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модели',
            },
        ),
        migrations.CreateModel(
            name='FileArchiveModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('md5', models.CharField(blank=True, max_length=100, null=True, verbose_name='MD5 сумма')),
                ('file', models.FileField(upload_to='img/c/doc/', verbose_name='Архив')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.projectarchivemodel', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Архив',
                'verbose_name_plural': 'Архивы',
            },
        ),
    ]
