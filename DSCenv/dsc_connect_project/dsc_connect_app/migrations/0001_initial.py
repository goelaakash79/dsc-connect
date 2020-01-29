# Generated by Django 3.0.2 on 2020-01-27 05:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dsc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[('0', 'draft'), ('1', 'published')], default=1, max_length=1)),
                ('lead', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('gmail', models.EmailField(blank=True, max_length=254)),
                ('cover', models.ImageField(upload_to='images/')),
                ('city', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=300)),
                ('team_size', models.IntegerField()),
                ('established_on', models.DateField()),
                ('created_on', models.DateTimeField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('website', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('medium', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('youtube', models.URLField(blank=True)),
                ('behance', models.URLField(blank=True)),
                ('custom', models.URLField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]