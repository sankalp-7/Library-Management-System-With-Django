# Generated by Django 4.0.5 on 2022-06-14 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=30)),
                ('isbn', models.IntegerField(max_length=13)),
                ('author', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='issuedbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lms.student')),
                ('isbn2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lms.book')),
            ],
        ),
    ]