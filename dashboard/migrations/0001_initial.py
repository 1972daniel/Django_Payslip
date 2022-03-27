# Generated by Django 3.1.7 on 2022-03-27 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('basic_salary', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('hours', models.PositiveIntegerField(default=0)),
                ('gross_salary', models.PositiveIntegerField(default=0)),
                ('grade_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.grade')),
            ],
        ),
    ]
