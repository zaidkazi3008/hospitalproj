# Generated by Django 3.2 on 2021-07-08 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_form_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='address',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='age',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='anesthesia',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='anus',
            field=models.TextField(blank=True, default='DEFAULT VALUE', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='bleeding',
            field=models.TextField(blank=True, default='DEFAULT VALUE', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='burning',
            field=models.TextField(blank=True, default='DEFAULT VALUE', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='constipation',
            field=models.TextField(blank=True, default='DEFAULT VALUE', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='diagnosis',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='digitalex',
            field=models.CharField(default='DEFAULT VALUE, null=True, blank=True', max_length=200),
        ),
        migrations.AlterField(
            model_name='form',
            name='estimate',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='itching',
            field=models.TextField(blank=True, default='DEFAULT VALUE', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='name',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='othercom',
            field=models.TextField(blank=True, default='DEFAULT VALUE', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='otherhis',
            field=models.CharField(default='DEFAULT VALUE, null=True, blank=True', max_length=200),
        ),
        migrations.AlterField(
            model_name='form',
            name='pain',
            field=models.TextField(blank=True, default='DEFAULT VALUE', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='pathological',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='phone',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='prolepse',
            field=models.TextField(blank=True, default='DEFAULT VALUE', max_length=122, null=True),
        ),
    ]
