# Generated by Django 4.0.2 on 2022-03-25 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_alter_message_receiver'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_send',
            field=models.BooleanField(default=False),
        ),
    ]
