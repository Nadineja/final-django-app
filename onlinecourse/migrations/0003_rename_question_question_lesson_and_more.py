# Generated by Django 4.1.3 on 2022-12-01 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20221129_2305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='lesson',
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default=' Choose an answer', max_length=300),
        ),
        migrations.AlterField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.CharField(default='question text', max_length=300),
        ),
    ]
