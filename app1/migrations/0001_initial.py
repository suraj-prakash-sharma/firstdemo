# Generated by Django 3.1.2 on 2021-05-30 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.IntegerField()),
                ('stu_name', models.CharField(max_length=40)),
                ('stu_mail', models.CharField(max_length=40)),
            ],
        ),
    ]