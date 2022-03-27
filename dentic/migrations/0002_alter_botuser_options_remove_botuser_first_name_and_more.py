# Generated by Django 4.0.3 on 2022-03-26 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='botuser',
            options={'verbose_name': 'Клиент'},
        ),
        migrations.RemoveField(
            model_name='botuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='botuser',
            name='language',
        ),
        migrations.RemoveField(
            model_name='botuser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='botuser',
            name='register_status',
        ),
        migrations.RemoveField(
            model_name='botuser',
            name='user_telegram_id',
        ),
        migrations.RemoveField(
            model_name='botuser',
            name='username',
        ),
        migrations.AddField(
            model_name='botuser',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ФИО'),
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
