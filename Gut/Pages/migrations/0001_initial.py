# Generated by Django 5.0.3 on 2024-03-20 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prompts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.DecimalField(decimal_places=0, max_digits=3)),
                ('Gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=1)),
                ('Allergies', models.CharField(max_length=20)),
                ('Medical_Condition', models.CharField(max_length=20)),
                ('Food_Preferences', models.CharField(max_length=20)),
            ],
        ),
    ]
