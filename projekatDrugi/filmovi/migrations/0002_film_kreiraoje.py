# Generated by Django 3.1.5 on 2021-01-08 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('filmovi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='kreiraoJe',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
