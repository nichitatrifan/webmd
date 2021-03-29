# Generated by Django 3.1.2 on 2021-02-28 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0004_question_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.vote'),
        ),
    ]
