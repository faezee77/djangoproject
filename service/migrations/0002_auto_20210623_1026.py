# Generated by Django 3.2.1 on 2021-06-23 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='groupPersian',
            field=models.CharField(default='تعمیر کامپیوتر', help_text='Enter Product group', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='group',
            field=models.CharField(default='computerService', help_text='Enter Product group', max_length=50),
        ),
    ]
