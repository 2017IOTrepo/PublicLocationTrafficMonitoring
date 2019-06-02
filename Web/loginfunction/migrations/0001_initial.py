# Generated by Django 2.0 on 2019-05-23 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50, verbose_name='地点')),
                ('pedestrian_flow', models.IntegerField(verbose_name='人流量')),
                ('is_overloading', models.BooleanField(verbose_name='是否超载')),
                ('abnormal_video', models.BinaryField(verbose_name='异常视频')),
                ('time', models.CharField(max_length=50, verbose_name='捕获时间')),
            ],
            options={
                'verbose_name': '人流量',
                'verbose_name_plural': '人流量',
                'db_table': 'local_data',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='security_staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='姓名')),
                ('location', models.CharField(max_length=50, verbose_name='位置')),
                ('p_number', models.CharField(max_length=50, verbose_name='联系方式')),
                ('weixin', models.CharField(max_length=50, null=True, verbose_name='微信')),
            ],
            options={
                'verbose_name': '安保人员',
                'verbose_name_plural': '安保人员',
                'db_table': 'security_staff',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['c_time'],
            },
        ),
    ]
