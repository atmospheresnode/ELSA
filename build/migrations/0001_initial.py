# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11.1 on 2019-12-13 17:39
=======
# Generated by Django 1.11.1 on 2019-08-30 17:37
>>>>>>> 8d1e0d7be88c4a9f8ce80716e7c4e414bdbacdd0
from __future__ import unicode_literals

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
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alternate_id', models.CharField(max_length=100)),
                ('alternate_title', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Aliases',
            },
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='Array',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('array_dimensions', models.CharField(choices=[('Array_2D', 'Array 2D'), ('Array_3D', 'Array 3D')], max_length=100)),
                ('array_type', models.CharField(choices=[('Image', 'Image'), ('Map', 'Map'), ('Spectrum', 'Spectrum')], max_length=100)),
                ('local_identifier', models.CharField(max_length=100)),
                ('md5_checksum', models.CharField(max_length=100)),
                ('offset', models.CharField(max_length=100)),
                ('axes', models.CharField(max_length=100)),
                ('axis_index_order', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
=======
>>>>>>> 8d1e0d7be88c4a9f8ce80716e7c4e414bdbacdd0
            name='Bundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bundle_type', models.CharField(choices=[('Archive', 'Archive'), ('Supplemental', 'Supplemental')], default='Archive', max_length=12)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('status', models.CharField(choices=[('b', 'Build'), ('r', 'Review'), ('s', 'Submit')], default='b', max_length=1)),
                ('version', models.CharField(choices=[('1A10', '1A10'), ('1A00', '1A00'), ('1900', '1900'), ('1800', '1800'), ('1700', '1700'), ('1410', '1410'), ('1300', '1300'), ('1000', '1000')], max_length=4)),
<<<<<<< HEAD
=======
                ('data_enum', models.PositiveIntegerField(default=0, null=True)),
>>>>>>> 8d1e0d7be88c4a9f8ce80716e7c4e414bdbacdd0
            ],
        ),
        migrations.CreateModel(
            name='Citation_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_list', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('editor_list', models.CharField(max_length=100)),
                ('keyword', models.CharField(max_length=100)),
                ('publication_year', models.CharField(max_length=100)),
                ('bundle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='build.Bundle')),
            ],
        ),
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_document', models.BooleanField(default=True)),
                ('has_context', models.BooleanField(default=True)),
<<<<<<< HEAD
                ('has_raw_data', models.BooleanField(default=False)),
                ('has_calibrated_data', models.BooleanField(default=False)),
                ('has_derived_data', models.BooleanField(default=False)),
=======
                ('has_xml_schema', models.BooleanField(default=True)),
                ('has_data', models.BooleanField(default=False)),
                ('data_enum', models.PositiveIntegerField(default=0)),
>>>>>>> 8d1e0d7be88c4a9f8ce80716e7c4e414bdbacdd0
                ('bundle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='build.Bundle')),
            ],
            options={
                'verbose_name_plural': 'Collections',
            },
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='Color_Display_Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_display_axis', models.PositiveIntegerField()),
                ('comment_color_display', models.CharField(max_length=100)),
                ('red_channel_band', models.PositiveIntegerField()),
                ('green_channel_band', models.PositiveIntegerField()),
                ('blue_channel_band', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256)),
                ('processing_level', models.CharField(choices=[('Calibrated', 'Calibrated'), ('Derived', 'Derived'), ('Raw', 'Raw'), ('Reduced', 'Reduced')], default='Raw', max_length=30)),
                ('data_enum', models.PositiveSmallIntegerField(default=0)),
=======
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processing_level', models.CharField(choices=[('Calibrated', 'Calibrated'), ('Derived', 'Derived'), ('Raw', 'Raw'), ('Reduced', 'Reduced')], default='Archive', max_length=30)),
>>>>>>> 8d1e0d7be88c4a9f8ce80716e7c4e414bdbacdd0
                ('bundle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='build.Bundle')),
            ],
            options={
                'verbose_name_plural': 'Data',
            },
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='Data_Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=251)),
                ('data_type', models.CharField(choices=[('Table Delimited', 'Table Delimited'), ('Table Binary', 'Table Binary'), ('Table Fixed-Width', 'Table Fixed-Width'), ('Array', 'Array')], default='Table Delimited', max_length=256)),
                ('data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='build.Data')),
            ],
            options={
                'verbose_name_plural': 'Data Object',
            },
        ),
        migrations.CreateModel(
            name='Display_Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_display_direction', models.CharField(max_length=100)),
                ('horizontal_display_axis', models.PositiveIntegerField()),
                ('horizontal_display_direction', models.PositiveIntegerField()),
                ('vertical_display_axis', models.PositiveIntegerField()),
                ('vertical_display_direction', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Display_Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_display_axis', models.PositiveIntegerField()),
                ('comment', models.CharField(max_length=100)),
                ('frame_rate', models.FloatField()),
                ('loop_flag', models.BooleanField()),
                ('loop_count', models.PositiveIntegerField()),
                ('loop_delay', models.FloatField()),
                ('loop_back_and_forth_flag', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='DisplayDictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Color_Display_Settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='build.Color_Display_Settings')),
                ('Display_Direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='build.Display_Direction')),
                ('Display_Settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='build.Display_Settings')),
=======
            name='Data_Prep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=251)),
                ('data_type', models.CharField(choices=[('Table Delimited', 'Table Delimited'), ('Table Binary', 'Table Binary'), ('Table Fixed-Width', 'Table Fixed-Width')], default='Table Delimited', max_length=256)),
                ('bundle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='build.Bundle')),
            ],
            options={
                'verbose_name_plural': 'Data Prep',
            },
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
>>>>>>> 8d1e0d7be88c4a9f8ce80716e7c4e414bdbacdd0
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('type_of', models.CharField(choices=[('Laboratory', 'Laboratory'), ('Observatory', 'Observatory')], max_length=100)),
                ('version', models.FloatField(default=1.0)),
                ('vid', models.FloatField(default=1.0)),
                ('starbase_label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Field_Binary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('field_number', models.IntegerField()),
                ('field_location', models.CharField(max_length=256)),
                ('data_type', models.CharField(max_length=256)),
                ('field_length', models.IntegerField()),
                ('unit', models.CharField(max_length=256, null=True)),
                ('scaling_factor', models.IntegerField()),
                ('value_offset', models.IntegerField()),
                ('description', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Field_Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('field_number', models.IntegerField()),
                ('data_type', models.CharField(max_length=256)),
                ('field_length', models.IntegerField()),
                ('field_location', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Field_Delimited',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('field_number', models.IntegerField()),
                ('data_type', models.CharField(max_length=256)),
                ('unit', models.CharField(max_length=256, null=True)),
                ('description', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('type_of', models.CharField(choices=[('Accelerometer', 'Accelerometer'), ('Alpha Particle Detector', 'Alpha Particle Detector'), ('Alpha Particle X-Ray Spectrometer', 'Alpha Particle X-Ray Spectrometer'), ('Altimeter', 'Altimeter'), ('Anemometer', 'Anemometer'), ('Atmospheric Sciences', 'Atmospheric Sciences'), ('Atomic Force Microscope', 'Atomic Force Microscope'), ('Barometer', 'Barometer'), ('Biology Experiments', 'Biology Experiments'), ('Bolometer', 'Bolometer'), ('Camera', 'Camera'), ('Cosmic Ray Detector', 'Cosmic Ray Detector'), ('Drilling Tool', 'Drilling Tool'), ('Dust', 'Dust'), ('Dust Detector', 'Dust Detector'), ('Electrical Probe', 'Electrical Probe'), ('Energetic Particle Detector', 'Energetic Particle Detector'), ('Gamma Ray Detector', 'Gamma Ray Detector'), ('Gas Analyzer', 'Gas Analyzer'), ('Gravimeter', 'Gravimeter'), ('Grinding Tool', 'Grinding Tool'), ('Hygrometer', 'Hygrometer'), ('Imager', 'Imager'), ('Imaging Spectrometer', 'Imaging Spectrometer'), ('Inertial Measurement Unit', 'Inertial Measurement Unit'), ('Infrared Spectrometer', 'Infrared Spectrometer'), ('Interferometer', 'Interferometer'), ('Laser Induced Breakdown Spectrometer', 'Laser Induced Breakdown Spectrometer'), ('Magnetometer', 'Magnetometer'), ('Mass Spectrometer', 'Mass Spectrometer'), ('Microscope', 'Microscope'), ('Microwave Spectrometer', 'Microwave Spectrometer'), ('Moessbauer Spectrometer', 'Moessbauer Spectrometer'), ('Naked Eye', 'Naked Eye'), ('Neutral Particle Detector', 'Neutral Particle Detector'), ('Neutron Detector', 'Neutron Detector'), ('Particle Detector', 'Particle Detector'), ('Photometer', 'Photometer'), ('Plasma Analyzer', 'Plasma Analyzer'), ('Plasma Detector', 'Plasma Detector'), ('Plasma Wave Spectrometer', 'Plasma Wave Spectrometer'), ('Polarimeter', 'Polarimeter'), ('Radar', 'Radar'), ('Radio Science', 'Radio Science'), ('Radio Spectrometer', 'Radio Spectrometer'), ('Radio Telescope', 'Radio Telescope'), ('Radio-Radar', 'Radio-Radar'), ('Radiometer', 'Radiometer'), ('Reflectometer', 'Reflectometer'), ('Regolith Properties', 'Regolith Properties'), ('Robotic Arm', 'Robotic Arm'), ('Seismometer', 'Seismometer'), ('Small Bodies Sciences', 'Small Bodies Sciences'), ('Spectrograph', 'Spectrograph'), ('Spectrograph Imager', 'Spectrograph Imager'), ('Spectrometer', 'Spectrometer'), ('Thermal Imager', 'Thermal Imager'), ('Thermal Probe', 'Thermal Probe'), ('Thermometer', 'Thermometer'), ('Ultraviolet Spectrometer', 'Ultraviolet Spectrometer'), ('Weather Station', 'Weather Station'), ('Wet Chemistry Laboratory', 'Wet Chemistry Laboratory'), ('X-ray Detector', 'X-ray Detector'), ('X-ray Diffraction Spectrometer', 'X-ray Diffraction Spectrometer'), ('X-ray Fluorescence Spectrometer', 'X-ray Fluorescence Spectrometer')], max_length=100)),
                ('vid', models.FloatField(default=1.0)),
                ('starbase_label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument_Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('type_of', models.CharField(choices=[('Earth Based', 'Earth Based'), ('Lander', 'Lander'), ('Rover', 'Rover'), ('Spacecraft', 'Spacecraft'), ('unk', 'unk')], max_length=100)),
                ('vid', models.FloatField(default=1.0)),
                ('starbase_label', models.CharField(max_length=100)),
                ('instruments', models.ManyToManyField(to='build.Instrument')),
            ],
        ),
        migrations.CreateModel(
            name='Investigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type_of', models.CharField(choices=[('individual', 'individual'), ('mission', 'mission'), ('observing_campaign', 'observing_campaign'), ('other_investigation', 'other_investigation')], max_length=100)),
                ('lid', models.CharField(max_length=255)),
                ('vid', models.FloatField(default=1.0)),
                ('starbase_label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('investigation', models.ManyToManyField(to='build.Investigation')),
            ],
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='Movie_Display_Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_display_axis', models.PositiveIntegerField()),
                ('comment', models.CharField(max_length=100)),
                ('frame_rate', models.FloatField()),
                ('loop_flag', models.BooleanField()),
                ('loop_count', models.PositiveIntegerField()),
                ('loop_delay', models.FloatField()),
                ('loop_back_and_forth_flag', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
=======
>>>>>>> 8d1e0d7be88c4a9f8ce80716e7c4e414bdbacdd0
            name='Product_Bundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bundle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='build.Bundle')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.CharField(choices=[('Document', 'Document'), ('Context', 'Context'), ('XML_Schema', 'XML_Schema'), ('Data', 'Data'), ('Browse', 'Browse'), ('Geometry', 'Geometry'), ('Calibration', 'Calibration'), ('Not_Set', 'Not_Set')], default='Not_Set', max_length=100)),
                ('bundle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='build.Bundle')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acknowledgement_text', models.CharField(max_length=100)),
                ('author_list', models.CharField(max_length=100)),
                ('copyright', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('document_editions', models.CharField(max_length=100)),
                ('document_name', models.CharField(max_length=100)),
                ('doi', models.CharField(max_length=100)),
                ('editor_list', models.CharField(max_length=100)),
                ('publication_date', models.CharField(max_length=100)),
                ('revision_id', models.CharField(max_length=100)),
                ('bundle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='build.Bundle')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Observational',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(choices=[('Atmosphere', 'Atmosphere'), ('Dynamics', 'Dynamics'), ('Heliosphere', 'Heliosphere'), ('Interior', 'Interior'), ('Interstellar', 'Interstellar'), ('Ionosphere', 'Ionosphere'), ('Magnetosphere', 'Magnetosphere'), ('Rings', 'Rings'), ('Surface', 'Surface')], default='Atmosphere', max_length=100)),
                ('discipline', models.CharField(choices=[('Atmospheres', 'Atmospheres'), ('Fields', 'Fields'), ('Flux Measurements', 'Flux Measurements'), ('Geosciences', 'Geosciences'), ('Imaging', 'Imaging'), ('Particles', 'Particles'), ('Radio Science', 'Radio Science'), ('Ring-Moon Systems', 'Ring-Moon Systems'), ('Small Bodies', 'Small Bodies'), ('Spectroscopy', 'Spectroscopy')], default='Atmospheres', max_length=100)),
                ('processing_level', models.CharField(choices=[('Calibrated', 'Calibrated'), ('Derived', 'Derived'), ('Reduced', 'Reduced'), ('Raw', 'Raw')], max_length=100)),
                ('purpose', models.CharField(choices=[('Calibration', 'Calibration'), ('Checkout', 'Checkout'), ('Engineering', 'Engineering'), ('Navigation', 'Navigation'), ('Observation Geometry', 'Observation Geometry'), ('Science', 'Science')], max_length=1000)),
                ('title', models.CharField(max_length=100)),
                ('type_of', models.CharField(choices=[('Table Binary', 'Table Binary'), ('Table Character', 'Table Character'), ('Table Delimited', 'Table Delimited')], default='Not_Set', max_length=100)),
                ('bundle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='build.Bundle')),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='build.Data')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('observational_type', models.CharField(choices=[('Table Base', 'Table Base'), ('Table Binary', 'Table Binary'), ('Table Character', 'Table Character'), ('Table Delimited', 'Table Delimited')], max_length=100)),
                ('local_identifier', models.CharField(max_length=100)),
                ('offset', models.CharField(max_length=100)),
                ('object_length', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('records', models.CharField(max_length=100)),
                ('fields', models.CharField(max_length=100)),
                ('groups', models.CharField(max_length=100)),
                ('product_observational', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='build.Product_Observational')),
            ],
        ),
        migrations.CreateModel(
            name='Table_Binary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('name', models.CharField(blank=True, max_length=256)),
=======
                ('name', models.CharField(max_length=256)),
>>>>>>> 8d1e0d7be88c4a9f8ce80716e7c4e414bdbacdd0
                ('offset', models.IntegerField(default=-1)),
                ('records', models.IntegerField(default=-1)),
                ('fields', models.IntegerField(default=-1)),
                ('bundle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='build.Bundle')),
<<<<<<< HEAD
                ('data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='build.Data')),
=======
>>>>>>> 8d1e0d7be88c4a9f8ce80716e7c4e414bdbacdd0
            ],
        ),
        migrations.CreateModel(
            name='Table_Delimited',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('name', models.CharField(blank=True, max_length=256)),
=======
                ('name', models.CharField(max_length=256)),
>>>>>>> 8d1e0d7be88c4a9f8ce80716e7c4e414bdbacdd0
                ('offset', models.IntegerField(default=-1)),
                ('object_length', models.IntegerField(default=-1)),
                ('description', models.CharField(default='unset', max_length=5000)),
                ('records', models.IntegerField(default=-1)),
<<<<<<< HEAD
                ('field_delimiter', models.CharField(blank=True, choices=[('Comma', 'Comma'), ('Horizontal Tab', 'Horizontal Tab'), ('Semicolon', 'Semicolon'), ('Vertical Bar', 'Vertical Bar')], default='Comma', max_length=256)),
                ('fields', models.IntegerField(default=-1)),
                ('bundle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='build.Bundle')),
                ('data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='build.Data')),
=======
                ('field_delimiter', models.CharField(choices=[('Comma', 'Comma'), ('Horizontal Tab', 'Horizontal Tab'), ('Semicolon', 'Semicolon'), ('Vertical Bar', 'Vertical Bar')], default='Comma', max_length=256)),
                ('fields', models.IntegerField(default=-1)),
                ('bundle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='build.Bundle')),
>>>>>>> 8d1e0d7be88c4a9f8ce80716e7c4e414bdbacdd0
            ],
        ),
        migrations.CreateModel(
            name='Table_Fixed_Width',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('name', models.CharField(blank=True, max_length=256)),
=======
                ('name', models.CharField(max_length=256)),
>>>>>>> 8d1e0d7be88c4a9f8ce80716e7c4e414bdbacdd0
                ('offset', models.IntegerField(default=-1)),
                ('object_length', models.IntegerField(default=-1)),
                ('description', models.CharField(default='unset', max_length=5000)),
                ('records', models.IntegerField(default=-1)),
<<<<<<< HEAD
                ('record_delimiter', models.CharField(blank=True, choices=[('Sample Choice', 'Sample Choice')], default='Sample Choice', max_length=256)),
                ('fields', models.IntegerField(default=-1)),
                ('bundle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='build.Bundle')),
                ('data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='build.Data')),
=======
                ('record_delimiter', models.CharField(default='Comma', max_length=256)),
                ('fields', models.IntegerField(default=-1)),
                ('bundle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='build.Bundle')),
>>>>>>> 8d1e0d7be88c4a9f8ce80716e7c4e414bdbacdd0
            ],
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('type_of', models.CharField(choices=[('Asteroid', 'Asteroid'), ('Calibration', 'Calibration'), ('Calibration Field', 'Calibration Field'), ('Calibrator', 'Calibrator'), ('Comet', 'Comet'), ('Dust', 'Dust'), ('Dwarf Planet', 'Dwarf Planet'), ('Equipment', 'Equipment'), ('Exoplanet System', 'Exoplanet System'), ('Galaxy', 'Galaxy'), ('Globular Cluster', 'Globular Cluster'), ('Lunar Sample', 'Lunar Sample'), ('Meteorite', 'Meteorite'), ('Meteoroid', 'Meteoroid'), ('Meteoroid Stream', 'Meteoroid Stream'), ('Nebula', 'Nebula'), ('Open Cluster', 'Open Cluster'), ('Planet', 'Planet'), ('Planetary Nebula', 'Planetary Nebula'), ('Planetary System', 'Planetary System'), ('Plasma Cloud', 'Plasma Cloud'), ('Plasma Stream', 'Plasma Stream'), ('Ring', 'Ring'), ('Satellite', 'Satellite'), ('Star', 'Star'), ('Star Cluster', 'Star Cluster'), ('Sun', 'Sun'), ('Synthetic Sample', 'Synthetic Sample'), ('Target Analog', 'Target Analog'), ('Terrestrial Sample', 'Terrestrial Sample'), ('Trans-Neptunian Object', 'Trans-Neptunian Object')], max_length=100)),
                ('vid', models.FloatField(default=1.0)),
                ('starbase_label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Telescope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('vid', models.FloatField(default=1.0)),
                ('starbase_label', models.CharField(max_length=100)),
                ('facilities', models.ManyToManyField(to='build.Facility')),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=4)),
                ('xml_model', models.CharField(max_length=100)),
                ('xmlns', models.CharField(max_length=100)),
                ('xsi', models.CharField(max_length=100)),
                ('schemaLocation', models.CharField(max_length=100)),
                ('schematypens', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='instrument_host',
            name='investigations',
            field=models.ManyToManyField(to='build.Investigation'),
        ),
        migrations.AddField(
            model_name='instrument_host',
            name='targets',
            field=models.ManyToManyField(to='build.Target'),
        ),
        migrations.AddField(
            model_name='field_delimited',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='build.Table_Delimited'),
        ),
        migrations.AddField(
            model_name='field_character',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='build.Table_Fixed_Width'),
        ),
        migrations.AddField(
            model_name='field_binary',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='build.Table_Binary'),
        ),
        migrations.AddField(
            model_name='facility',
            name='instruments',
            field=models.ManyToManyField(to='build.Instrument'),
        ),
        migrations.AddField(
            model_name='bundle',
            name='facilities',
            field=models.ManyToManyField(to='build.Facility'),
        ),
        migrations.AddField(
            model_name='bundle',
            name='instrument_hosts',
            field=models.ManyToManyField(to='build.Instrument_Host'),
        ),
        migrations.AddField(
            model_name='bundle',
            name='instruments',
            field=models.ManyToManyField(to='build.Instrument'),
        ),
        migrations.AddField(
            model_name='bundle',
            name='investigations',
            field=models.ManyToManyField(to='build.Investigation'),
        ),
        migrations.AddField(
            model_name='bundle',
            name='targets',
            field=models.ManyToManyField(to='build.Target'),
        ),
        migrations.AddField(
            model_name='bundle',
            name='telescopes',
            field=models.ManyToManyField(to='build.Telescope'),
        ),
        migrations.AddField(
            model_name='bundle',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
<<<<<<< HEAD
            model_name='array',
            name='product_observational',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='build.Product_Observational'),
        ),
        migrations.AddField(
=======
>>>>>>> 8d1e0d7be88c4a9f8ce80716e7c4e414bdbacdd0
            model_name='alias',
            name='bundle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='build.Bundle'),
        ),
    ]
