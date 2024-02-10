# Generated by Django 5.0.1 on 2024-01-11 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stfcda', '0016_journalfiles_version_alter_journalfiles_journal'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('surname', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('skills', models.TextField()),
                ('position', models.CharField(choices=[('editor_in_chief', 'Editor-in-Chief'), ('managing_editor', 'Managing Editor'), ('section_editor', 'Section Editor'), ('copy_editor', 'Copy Editor'), ('peer_review_coordinator', 'Peer Review Coordinator'), ('design_layout_editor', 'Design and Layout Editor'), ('technical_editor', 'Technical Editor'), ('publications_manager', 'Publications Manager'), ('marketing_coordinator', 'Marketing Coordinator'), ('advisory_board_member', 'Advisory Board Member')], max_length=30)),
                ('why_volunteer', models.TextField()),
                ('fit_for_position', models.TextField()),
                ('resume', models.FileField(upload_to='resumes/')),
            ],
        ),
    ]