# Generated by Django 5.1.7 on 2025-04-22 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_livro_coautor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='coautor',
        ),
        migrations.AddField(
            model_name='livro',
            name='autores',
            field=models.ManyToManyField(blank=True, related_name='livros', to='core.autor'),
        ),
    ]
