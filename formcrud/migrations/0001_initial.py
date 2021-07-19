# Generated by Django 3.2.5 on 2021-07-18 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('addressLine1', models.CharField(max_length=100)),
                ('addressLine2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=50)),
            ],
        ),
    ]
