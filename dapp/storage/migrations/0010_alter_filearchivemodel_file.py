# Generated by Django 4.2.1 on 2023-05-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0009_alter_filearchivemodel_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filearchivemodel',
            name='file',
            field=models.FileField(upload_to='storage/models/<bound method ForeignKey.get_attname of <django.db.models.fields.related.ForeignKey>>/', verbose_name='Архив'),
        ),
    ]
