# Generated by Django 3.1.5 on 2021-01-11 19:24

from django.db import migrations, models
import django.db.models.deletion
import legislatives.models
import location_field.models.spatial


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '__first__'),
        ('politicans', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('permanent', models.BooleanField()),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('website', models.URLField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=legislatives.models.Commission.get_commission_upload_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommissionMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('commission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legislatives.commission')),
            ],
        ),
        migrations.CreateModel(
            name='Parlament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('number_of_seats', models.IntegerField(blank=True, null=True)),
                ('street1', models.CharField(blank=True, max_length=200)),
                ('street2', models.CharField(blank=True, max_length=200)),
                ('location_query', models.CharField(blank=True, max_length=200, null=True)),
                ('location', location_field.models.spatial.LocationField(blank=True, null=True, srid=4326)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('website', models.URLField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=legislatives.models.Parlament.get_parlament_upload_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parlaments', to='locations.plz')),
                ('jurisdiction_canton', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='canton_parlaments', to='locations.canton')),
                ('jurisdiction_country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country_parlaments', to='locations.country')),
                ('jurisdiction_municipality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='municipality_parlaments', to='locations.municipality')),
            ],
        ),
        migrations.CreateModel(
            name='ParlamentMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParlamentSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('opening_session', models.BooleanField(blank=True, null=True)),
                ('regular_session', models.BooleanField(blank=True, null=True)),
                ('additional_information', models.TextField(blank=True)),
                ('greeting', models.TextField(blank=True)),
                ('discharge', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('excused_politicans', models.ManyToManyField(blank=True, to='politicans.Politican')),
            ],
        ),
        migrations.CreateModel(
            name='ParlamentRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parlament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parlament_roles', to='legislatives.parlament')),
            ],
        ),
        migrations.CreateModel(
            name='ParlamentMembershipRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parlament_membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legislatives.parlamentmembership')),
                ('parlament_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legislatives.parlamentrole')),
            ],
        ),
        migrations.AddField(
            model_name='parlamentmembership',
            name='membership_roles',
            field=models.ManyToManyField(through='legislatives.ParlamentMembershipRole', to='legislatives.ParlamentRole'),
        ),
        migrations.AddField(
            model_name='parlamentmembership',
            name='parlament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legislatives.parlament'),
        ),
        migrations.AddField(
            model_name='parlamentmembership',
            name='politican',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='politicans.politican'),
        ),
        migrations.AddField(
            model_name='parlament',
            name='members',
            field=models.ManyToManyField(through='legislatives.ParlamentMembership', to='politicans.Politican'),
        ),
        migrations.CreateModel(
            name='CommissionRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('commission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commission_roles', to='legislatives.commission')),
            ],
        ),
        migrations.CreateModel(
            name='CommissionMembershipRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('commission_membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legislatives.commissionmembership')),
                ('commission_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legislatives.commissionrole')),
            ],
        ),
        migrations.AddField(
            model_name='commissionmembership',
            name='membership_roles',
            field=models.ManyToManyField(through='legislatives.CommissionMembershipRole', to='legislatives.CommissionRole'),
        ),
        migrations.AddField(
            model_name='commissionmembership',
            name='politican',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='politicans.politican'),
        ),
        migrations.AddField(
            model_name='commission',
            name='members',
            field=models.ManyToManyField(through='legislatives.CommissionMembership', to='politicans.Politican'),
        ),
        migrations.AddField(
            model_name='commission',
            name='parlament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commissions', to='legislatives.parlament'),
        ),
        migrations.AddConstraint(
            model_name='parlamentrole',
            constraint=models.UniqueConstraint(fields=('title', 'parlament'), name='unique_parlament_roles'),
        ),
        migrations.AddConstraint(
            model_name='parlamentmembershiprole',
            constraint=models.UniqueConstraint(fields=('parlament_membership', 'parlament_role'), name='unique_parlament_membership_roles'),
        ),
        migrations.AddConstraint(
            model_name='parlamentmembership',
            constraint=models.UniqueConstraint(fields=('politican', 'parlament'), name='unique_parlament_memberships'),
        ),
        migrations.AddConstraint(
            model_name='commissionrole',
            constraint=models.UniqueConstraint(fields=('title', 'commission'), name='unique_commission_roles'),
        ),
        migrations.AddConstraint(
            model_name='commissionmembership',
            constraint=models.UniqueConstraint(fields=('politican', 'commission'), name='unique_commission_memberships'),
        ),
    ]
