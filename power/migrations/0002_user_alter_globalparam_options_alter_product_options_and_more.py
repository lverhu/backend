# Generated by Django 4.2.5 on 2024-04-04 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('power', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': '用户表',
                'db_table': 'tb_user',
            },
        ),
        migrations.AlterModelOptions(
            name='globalparam',
            options={'verbose_name_plural': '全局参数表'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': '产品表'},
        ),
        migrations.AlterModelOptions(
            name='productdetail',
            options={'verbose_name_plural': '产品详情表'},
        ),
        migrations.AlterModelOptions(
            name='testunit',
            options={'verbose_name_plural': '测试用例表'},
        ),
        migrations.AlterModelOptions(
            name='unitparam',
            options={'verbose_name_plural': '用例参数表'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='productdetail',
        ),
    ]
