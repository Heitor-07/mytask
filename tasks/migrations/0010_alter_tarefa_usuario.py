# Generated by Django 4.0 on 2022-01-02 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('tasks', '0009_tarefa_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
        ),
    ]
