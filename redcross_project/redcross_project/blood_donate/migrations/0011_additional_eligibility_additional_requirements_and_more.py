# Generated by Django 4.2.4 on 2023-08-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donate', '0010_alter_homenav_drop_options_alter_homenav_drop_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='additional_eligibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept', models.CharField(default='', max_length=2000)),
                ('images', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='additional_requirements',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='media/')),
                ('points', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='basicrequirements',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=200)),
                ('icon', models.ImageField(upload_to='media/')),
                ('points', models.CharField(max_length=2000)),
                ('images', models.ImageField(default='', upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='eligibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept', models.CharField(default='', max_length=2000)),
                ('images', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='patient_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('mobilenumber', models.CharField(max_length=100)),
                ('hospitalname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('bloodgroup', models.CharField(max_length=100)),
                ('bloodrequirements', models.CharField(max_length=100)),
                ('bloodtypes', models.CharField(max_length=100)),
            ],
        ),
    ]
