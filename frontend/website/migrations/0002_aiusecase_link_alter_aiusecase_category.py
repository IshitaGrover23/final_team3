# Generated by Django 5.0.6 on 2024-08-13 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aiusecase',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aiusecase',
            name='category',
            field=models.CharField(choices=[('health_monitoring', 'Health Monitoring'), ('multi_modal_analytics', 'Multi Modal Analytics'), ('image_analysis', 'Image Analysis'), ('summarization', 'Summarization')], max_length=50),
        ),
    ]
