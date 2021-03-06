# Generated by Django 2.0.3 on 2018-04-19 09:03

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('learnview', '0002_auto_20180323_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('aparent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learnview.AreaInfo')),
            ],
        ),
        migrations.AlterModelManagers(
            name='bookinfo',
            managers=[
                ('bookInfo', django.db.models.manager.Manager()),
            ],
        ),
    ]
