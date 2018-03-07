# Generated by Django 2.0.2 on 2018-03-06 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept_path', models.CharField(max_length=500)),
                ('concept_text', models.CharField(max_length=200)),
                ('concept_type', models.CharField(choices=[('TXT', 'Text'), ('INT', 'Integer'), ('FLOAT', 'Floating Point')], max_length=25)),
                ('concept_depth', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ConceptTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Ontology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='concept',
            name='ontology',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='metadata.Ontology'),
        ),
    ]
