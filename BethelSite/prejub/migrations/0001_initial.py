# Generated by Django 3.1.3 on 2020-11-27 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_text', models.TextField(max_length=520, verbose_name='Sugerencia')),
            ],
        ),
    ]