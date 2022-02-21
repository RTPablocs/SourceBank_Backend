# Generated by Django 4.0.2 on 2022-02-17 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vault',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=240, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('target', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_vaults', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
