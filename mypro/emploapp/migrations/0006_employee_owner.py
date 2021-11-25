# Generated by Django 3.2.9 on 2021-11-10 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emploapp', '0005_stud_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='empl', to='auth.user'),
            preserve_default=False,
        ),
    ]
