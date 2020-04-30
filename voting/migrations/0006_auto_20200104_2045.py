# Generated by Django 2.2.8 on 2020-01-04 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0005_auto_20200104_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voteuser',
            name='vote',
        ),
        migrations.AddField(
            model_name='voteuser',
            name='candidate',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='voting.Candidate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voteuser',
            name='voting_session',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='voting.VotingSession'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='voteuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
