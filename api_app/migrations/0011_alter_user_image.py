# Generated by Django 4.0.1 on 2022-04-13 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0010_alter_archiveuser_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='', upload_to='uploads/'),
        ),
    ]