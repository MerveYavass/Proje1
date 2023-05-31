# Generated by Django 4.2 on 2023-05-26 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0018_evozellik_card_ev_ozellikleri'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='resim',
        ),
        migrations.AddField(
            model_name='card',
            name='resim1',
            field=models.FileField(null=True, upload_to='resimler/'),
        ),
        migrations.AddField(
            model_name='card',
            name='resim2',
            field=models.FileField(null=True, upload_to='resimler/'),
        ),
        migrations.AddField(
            model_name='card',
            name='resim3',
            field=models.FileField(null=True, upload_to='resimler/'),
        ),
        migrations.AddField(
            model_name='card',
            name='resim4',
            field=models.FileField(null=True, upload_to='resimler/'),
        ),
        migrations.AddField(
            model_name='card',
            name='resim5',
            field=models.FileField(null=True, upload_to='resimler/'),
        ),
        migrations.DeleteModel(
            name='Resim',
        ),
    ]
