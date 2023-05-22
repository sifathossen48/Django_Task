# Generated by Django 4.2 on 2023-05-22 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Website_Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='logo/')),
                ('favicon', models.ImageField(upload_to='favicon/')),
                ('facebook', models.CharField(max_length=100)),
                ('youtube', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=100)),
            ],
        ),
    ]
