# Generated by Django 4.0 on 2022-01-08 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_alter_tarefa_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='descricao',
            field=models.TextField(max_length=500, verbose_name='Descrição'),
        ),
    ]