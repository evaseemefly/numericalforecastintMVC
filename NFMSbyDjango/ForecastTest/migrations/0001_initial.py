# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionInfo',
            fields=[
                ('AID', models.AutoField(primary_key=True, serialize=False)),
                ('ParentID', models.IntegerField(default=0)),
                ('Name', models.CharField(max_length=64)),
                ('DelFlag', models.BooleanField(default=True)),
                ('ModifiedOnTime', models.DateField()),
                ('Remark', models.CharField(max_length=256)),
                ('Url', models.CharField(max_length=256)),
                ('AreaName', models.CharField(max_length=64)),
                ('ActionMethodName', models.CharField(max_length=64)),
                ('ControllerName', models.CharField(max_length=64)),
                ('JsFunctionName', models.CharField(max_length=32)),
                ('Sort', models.SmallIntegerField(default=0)),
                ('ActionTypeEnum', models.PositiveSmallIntegerField(default=0)),
                ('IconWidth', models.PositiveSmallIntegerField(null=True)),
                ('IconHeigh', models.PositiveSmallIntegerField(null=True)),
                ('IconCls', models.CharField(max_length=64)),
                ('IconClassName', models.CharField(max_length=64)),
                ('isShow', models.BooleanField(default=True)),
                ('MethodTypeEnum', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'db_table': 'actioninfo',
            },
        ),
        migrations.CreateModel(
            name='R_UserInfo_Action',
            fields=[
                ('RID', models.AutoField(primary_key=True, serialize=False)),
                ('isPass', models.BooleanField(default=False)),
                ('ActionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ForecastTest.ActionInfo')),
            ],
            options={
                'db_table': 'r_userinfo_action',
            },
        ),
        migrations.CreateModel(
            name='TestInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubTime', models.DateTimeField(auto_now=True)),
                ('TestTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'testinfo',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('UID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=64)),
                ('Pwd', models.CharField(max_length=64)),
                ('DelFlag', models.BooleanField(default=False)),
                ('SubTime', models.DateTimeField(auto_now_add=True)),
                ('ModifiedOnTime', models.DateTimeField(auto_now=True)),
                ('TestModifiedOnTime', models.DateTimeField(auto_now=True)),
                ('Remark', models.CharField(max_length=256)),
                ('Sort', models.SmallIntegerField(default=0)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
        migrations.AddField(
            model_name='r_userinfo_action',
            name='UserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ForecastTest.UserInfo'),
        ),
    ]
