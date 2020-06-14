# Generated by Django 3.0.6 on 2020-06-14 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=100)),
                ('staff_address', models.CharField(max_length=200)),
                ('staff_phone', models.BigIntegerField()),
                ('staff_description', models.CharField(max_length=500)),
                ('college_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.College')),
            ],
        ),
    ]