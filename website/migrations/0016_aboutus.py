# Generated by Django 4.2 on 2023-07-01 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_category_html_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(blank=True, null=True)),
                ('desc2', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='about/')),
            ],
        ),
    ]
