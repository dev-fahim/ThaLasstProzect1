# Generated by Django 2.2.2 on 2019-06-23 11:05

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
            name='MainUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=55)),
                ('birthday', models.DateField()),
                ('_package', models.CharField(choices=[(1, 'Basic'), (2, 'Standard'), (3, 'Premium')], max_length=55)),
                ('_added', models.DateTimeField(auto_now_add=True)),
                ('_updated', models.DateTimeField(auto_now=True)),
                ('_blocked', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='main_user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationMonthlyPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_paid_time', models.DateTimeField()),
                ('_next_pay', models.DateTimeField()),
                ('main_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthly_payments', to='profile_app.MainUserProfile')),
            ],
        ),
    ]
