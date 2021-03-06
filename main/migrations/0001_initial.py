# Generated by Django 2.1.3 on 2018-11-21 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='food', max_length=128)),
                ('description', models.CharField(max_length=512)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='static/food_pics/')),
            ],
        ),
    ]
