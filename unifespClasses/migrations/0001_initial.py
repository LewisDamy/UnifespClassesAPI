# Generated by Django 4.1 on 2022-08-06 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Subjects",
            fields=[
                ("SubjectID", models.AutoField(primary_key=True, serialize=False)),
                ("subjectName", models.CharField(max_length=50)),
                ("category", models.CharField(max_length=50)),
                ("chTotal", models.IntegerField()),
                ("requirements", models.CharField(max_length=300)),
                ("semesterAvailable", models.CharField(max_length=50)),
            ],
        ),
    ]
