# Generated by Django 3.0.7 on 2020-06-17 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='step',
            field=models.CharField(choices=[('one', 'One'), ('two', 'Two'), ('third', 'Third'), ('zero', 'Zero')], default='zero', max_length=5),
        ),
    ]
