# Generated by Django 4.0 on 2021-12-26 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50, verbose_name='Categoria')),
            ],
        ),
        migrations.RemoveField(
            model_name='tarefa',
            name='categoria',
        ),
    ]