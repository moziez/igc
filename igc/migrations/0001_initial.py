# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 08:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fellow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220, verbose_name='\u0418\u043c\u044f')),
                ('surname', models.CharField(max_length=220, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('biography', models.TextField(verbose_name='\u0411\u0438\u043e\u0433\u0440\u0430\u0444\u0438\u044f')),
                ('email', models.EmailField(max_length=254, verbose_name='\u042d\u043b. \u0430\u0434\u0440\u0435\u0441')),
                ('phone', models.CharField(max_length=100, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u043e\u0444\u043d\u0430')),
                ('active', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
