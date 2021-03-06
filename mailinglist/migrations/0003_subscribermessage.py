# Generated by Django 2.2.4 on 2019-08-13 13:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mailinglist', '0002_auto_20190812_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriberMessage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sent', models.DateField(default=None, null=True)),
                ('last_attempt', models.DateTimeField(default=None, null=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailinglist.Message')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailinglist.Subscriber')),
            ],
        ),
    ]
