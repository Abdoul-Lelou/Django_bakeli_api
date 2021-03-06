# Generated by Django 4.0.1 on 2022-02-16 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0004_alter_cour_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivecour',
            name='cour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cour', to='api_app.cour', unique=True),
        ),
        migrations.AlterField(
            model_name='archiveuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
