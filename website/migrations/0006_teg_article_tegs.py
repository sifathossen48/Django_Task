# Generated by Django 4.2 on 2023-05-27 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tegs',
            field=models.ManyToManyField(to='website.teg'),
        ),
    ]
