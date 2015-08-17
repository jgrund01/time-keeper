# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkShift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shift_date', models.DateTimeField()),
                ('work_start_time', models.DateTimeField()),
                ('lunch_start_time', models.DateTimeField()),
                ('lunch_end_time', models.DateTimeField()),
                ('work_end_time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
