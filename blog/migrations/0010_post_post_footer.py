# Generated by Django 3.0.6 on 2020-05-28 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200528_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_footer',
            field=models.TextField(blank=True),
        ),
    ]