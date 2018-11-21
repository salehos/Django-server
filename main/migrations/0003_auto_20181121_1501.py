# Generated by Django 2.1.3 on 2018-11-21 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20181121_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reserve_date', models.DateField(auto_now_add=True)),
                ('type', models.IntegerField(choices=[(1, 'lunch'), (2, 'dinner')], default=1)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Food')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='food',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='reserve',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
