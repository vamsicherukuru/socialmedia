# Generated by Django 3.0.3 on 2020-08-11 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200811_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newscomment',
            name='comment_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='Description',
            field=models.TextField(),
        ),
    ]
