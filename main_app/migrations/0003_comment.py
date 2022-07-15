# Generated by Django 2.2.12 on 2022-07-15 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20220712_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1)),
                ('comment', models.TextField(max_length=250)),
                ('figure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Figure')),
            ],
        ),
    ]
