# Generated by Django 2.0.2 on 2019-02-05 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coment', models.CharField(max_length=228)),
            ],
        ),
        migrations.AlterField(
            model_name='mainform',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
