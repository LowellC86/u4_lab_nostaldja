# Generated by Django 4.2.3 on 2023-07-17 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_year', models.CharField(max_length=4)),
                ('end_year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Fads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=200)),
                ('decade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fads', to='nostaldja.decades')),
            ],
        ),
    ]
