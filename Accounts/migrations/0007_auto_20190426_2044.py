# Generated by Django 2.2 on 2019-04-26 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_auto_20190426_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='subject',
            field=models.CharField(choices=[('', 'Choose a Subject'), ('Suggestions', 'suggestions'), ('Compliment', 'Compliment')], max_length=50),
        ),
    ]
