# Generated by Django 3.2 on 2021-06-11 05:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_form_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]