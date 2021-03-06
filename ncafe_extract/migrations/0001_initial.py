# Generated by Django 2.1.1 on 2020-07-04 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NcafeList',
            fields=[
                ('cafe_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cafe_name', models.CharField(max_length=64)),
                ('updt_dt', models.DateTimeField()),
                ('post_cnt', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ncafe_list',
                'managed': False,
            },
        ),
    ]
