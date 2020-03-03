# Generated by Django 2.1 on 2020-03-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo_list',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('pcode', models.CharField(max_length=4)),
                ('user_id', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=1000)),
                ('is_complete', models.BooleanField()),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'todo_list',
                'managed': False,
            },
        ),
    ]