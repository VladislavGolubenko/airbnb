# Generated by Django 4.0.4 on 2022-06-02 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-date_creation'], 'verbose_name': 'Букинг', 'verbose_name_plural': 'Букинг'},
        ),
        migrations.AlterField(
            model_name='pictures',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
