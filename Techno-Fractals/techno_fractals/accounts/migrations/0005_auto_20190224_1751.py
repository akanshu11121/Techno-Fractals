# Generated by Django 2.1.7 on 2019-02-24 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190224_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='writer',
            field=models.ForeignKey(default="<class 'django.contrib.auth.models.User'>", on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]