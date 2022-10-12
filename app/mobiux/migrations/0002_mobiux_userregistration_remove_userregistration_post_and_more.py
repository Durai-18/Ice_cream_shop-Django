# Generated by Django 4.1.1 on 2022-10-04 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiux', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mobiux_userregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('mobile', models.IntegerField(max_length=10)),
            ],
            options={
                'db_table': 'mobiux_userregistration',
            },
        ),
        migrations.RemoveField(
            model_name='userregistration',
            name='post',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='UserRegistration',
        ),
    ]
