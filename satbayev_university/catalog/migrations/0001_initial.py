# Generated by Django 2.0.3 on 2018-03-07 20:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp_name', models.CharField(help_text='Enter a student spec', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_name', models.CharField(max_length=200)),
                ('GPA', models.TextField(help_text='Enter a GPA of the student', max_length=1000)),
                ('iin', models.CharField(help_text='13 Character <a href="https://www.iin-international.org/content/what-iin">IIN number</a>', max_length=13, verbose_name='IIN')),
                ('spec', models.ManyToManyField(help_text='Select a spec for this student', to='catalog.Spec')),
            ],
        ),
        migrations.CreateModel(
            name='StudentInformation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False)),
                ('mail', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'Magistrant'), ('o', 'Otchislen'), ('a', 'Bakalavr'), ('r', 'Doctorant')], default='d', help_text='Student status', max_length=1)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Student')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_hire', models.DateField(blank=True, null=True, verbose_name='Hire')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Teacher'),
        ),
    ]
