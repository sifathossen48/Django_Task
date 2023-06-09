# Generated by Django 4.2 on 2023-06-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_comment_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60)),
            ],
        ),
    ]
