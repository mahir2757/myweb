# Generated by Django 4.2.3 on 2023-08-02 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_todolist_delete_to_do_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('roll', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('enno', models.IntegerField()),
                ('div', models.CharField(max_length=50)),
                ('group_no', models.IntegerField()),
                ('project_detail', models.TextField()),
            ],
            options={
                'db_table': 'work_list',
            },
        ),
        migrations.AlterModelOptions(
            name='todolist',
            options={'verbose_name_plural': 'To-Do Lists'},
        ),
    ]