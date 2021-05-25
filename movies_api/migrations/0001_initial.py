# Generated by Django 3.2.3 on 2021-05-25 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('image', models.CharField(default='https: // demofree.sirv.com/nope-not-here.jpg', max_length=2048)),
                ('year', models.CharField(max_length=4)),
                ('synopsis', models.CharField(max_length=1024)),
                ('rating', models.CharField(max_length=2)),
            ],
        ),
    ]