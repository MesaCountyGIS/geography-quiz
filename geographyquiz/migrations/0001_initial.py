# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('correct_choice', models.CharField(max_length=1)),
                ('explanation', models.CharField(max_length=500, blank=True)),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'answers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'questions',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(to='geographyquiz.Questions'),
            preserve_default=True,
        ),
    ]
