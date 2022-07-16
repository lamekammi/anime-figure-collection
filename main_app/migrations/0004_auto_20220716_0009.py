# Generated by Django 2.2.12 on 2022-07-16 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='figure',
            name='stores',
            field=models.ManyToManyField(to='main_app.Store'),
        ),
    ]
