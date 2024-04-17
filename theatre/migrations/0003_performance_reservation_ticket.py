# Generated by Django 5.0.4 on 2024-04-16 11:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0002_actor_genre_theatrehall_'
                    'alter_play_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('show_time', models.DateTimeField()),
                ('play', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='theatre.play')),
                ('theatre_hall', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='theatre.theatrehall')),
            ],
            options={
                'ordering': ['-show_time'],
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('row', models.IntegerField()),
                ('seat', models.IntegerField()),
                ('performance', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='tickets', to='theatre.performance')),
                ('reservation', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='tickets', to='theatre.reservation')),
            ],
            options={
                'unique_together': {('performance', 'row', 'seat')},
            },
        ),
    ]
