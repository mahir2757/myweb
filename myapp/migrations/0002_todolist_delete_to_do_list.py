# Generated by Django 4.2.3 on 2023-08-02 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='to_do_list',
        ),
    ]
