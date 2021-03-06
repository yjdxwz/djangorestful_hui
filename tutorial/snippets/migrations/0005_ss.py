# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='SS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('qq', models.TextField(default='')),
                ('wechat', models.TextField(default='')),
                ('alipay', models.TextField(default='')),
                ('buy_time', models.TextField(default='')),
                ('end_time', models.TextField(default='')),
                ('ss_ip', models.TextField(default='')),
                ('ss_port', models.TextField(default='')),
                ('ss_passwd', models.TextField(default='')),
                ('ss_encry', models.TextField(default='aes-256-cfb')),
                ('isExpired', models.BooleanField(default=False)),
                ('note', models.TextField(default='')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
