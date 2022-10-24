# Generated by Django 4.1 on 2022-10-21 08:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundBannerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_photo', models.CharField(choices=[('Фото на фоне', 'Фото на фоне'), ('Просто фон', 'Просто фон')], default='Просто фон', max_length=20)),
                ('image', models.ImageField(default=None, null=True, upload_to='background/')),
            ],
            options={
                'db_table': 'back_banner',
            },
        ),
        migrations.CreateModel(
            name='CinemaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title_uk', models.CharField(max_length=50, null=True)),
                ('title_en', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_uk', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('condition', models.TextField(blank=True, null=True)),
                ('condition_uk', models.TextField(blank=True, null=True)),
                ('condition_en', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(upload_to='logo/')),
                ('banner', models.ImageField(upload_to='banner/')),
            ],
            options={
                'db_table': 'cinema_page',
            },
        ),
        migrations.CreateModel(
            name='ImagesTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'images_title',
            },
        ),
        migrations.CreateModel(
            name='SeoBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_url', models.URLField()),
                ('seo_title', models.CharField(max_length=50)),
                ('seo_title_uk', models.CharField(max_length=50, null=True)),
                ('seo_title_en', models.CharField(max_length=50, null=True)),
                ('seo_keywords', models.CharField(max_length=50)),
                ('seo_keywords_uk', models.CharField(max_length=50, null=True)),
                ('seo_keywords_en', models.CharField(max_length=50, null=True)),
                ('seo_description', models.TextField()),
                ('seo_description_uk', models.TextField(null=True)),
                ('seo_description_en', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OtherPageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_published', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_published', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=50)),
                ('title_uk', models.CharField(max_length=50, null=True)),
                ('title_en', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_uk', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('images', models.ImageField(upload_to='images/')),
                ('collection_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.imagestitle')),
                ('seo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.seoblock')),
            ],
            options={
                'db_table': 'other_page',
            },
        ),
        migrations.CreateModel(
            name='NewsAndPromotions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=50)),
                ('title_uk', models.CharField(max_length=50, null=True)),
                ('title_en', models.CharField(max_length=50, null=True)),
                ('data_published', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_uk', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('images', models.ImageField(upload_to='images/')),
                ('link', models.URLField()),
                ('page_type', models.IntegerField(choices=[(0, 'Action'), (1, 'News')], default=0)),
                ('collection_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.imagestitle')),
                ('seo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.seoblock')),
            ],
            options={
                'db_table': 'news_and_promotions',
            },
        ),
        migrations.CreateModel(
            name='MainPageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title_uk', models.CharField(max_length=50, null=True)),
                ('title_en', models.CharField(max_length=50, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('data_published', models.DateTimeField(default=django.utils.timezone.now)),
                ('phone_1', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('phone_2', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('seo_text', models.TextField(blank=True, null=True)),
                ('seo_text_uk', models.TextField(blank=True, null=True)),
                ('seo_text_en', models.TextField(blank=True, null=True)),
                ('seo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.seoblock')),
            ],
            options={
                'db_table': 'main_page',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/')),
                ('url', models.URLField()),
                ('text', models.CharField(max_length=50)),
                ('text_uk', models.CharField(max_length=50, null=True)),
                ('text_en', models.CharField(max_length=50, null=True)),
                ('collection_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.imagestitle')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='HallModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title_uk', models.CharField(max_length=50, null=True)),
                ('title_en', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_uk', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('sceme_hall', models.ImageField(upload_to='hall/')),
                ('banner', models.ImageField(upload_to='banner/')),
                ('data_published', models.DateTimeField(default=django.utils.timezone.now)),
                ('cinema', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.cinemamodel')),
                ('collection_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.imagestitle')),
                ('seo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.seoblock')),
            ],
            options={
                'db_table': 'hall_page',
            },
        ),
        migrations.CreateModel(
            name='FilmModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title_uk', models.CharField(max_length=50, null=True)),
                ('title_en', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_uk', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('images', models.ImageField(upload_to='images/')),
                ('link', models.URLField()),
                ('is_active', models.IntegerField(choices=[(0, 'Poster'), (1, 'while')], default=0)),
                ('type_of_film_3D', models.BooleanField(default=False)),
                ('type_of_film_2D', models.BooleanField(default=False)),
                ('type_of_film_IMAX', models.BooleanField(default=False)),
                ('collection_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.imagestitle')),
                ('seo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.seoblock')),
            ],
            options={
                'db_table': 'film_page',
            },
        ),
        migrations.CreateModel(
            name='ContactPageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title_uk', models.CharField(max_length=50, null=True)),
                ('title_en', models.CharField(max_length=50, null=True)),
                ('data_published', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=False)),
                ('seo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.seoblock')),
            ],
            options={
                'db_table': 'contact_pages',
            },
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title_uk', models.CharField(max_length=50, null=True)),
                ('title_en', models.CharField(max_length=50, null=True)),
                ('address', models.TextField(blank=True)),
                ('address_uk', models.TextField(blank=True, null=True)),
                ('address_en', models.TextField(blank=True, null=True)),
                ('coordinates', models.CharField(blank=True, max_length=100)),
                ('coordinates_uk', models.CharField(blank=True, max_length=100, null=True)),
                ('coordinates_en', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('logo', models.ImageField(upload_to='contact/')),
                ('contact_page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.contactpagemodel')),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.AddField(
            model_name='cinemamodel',
            name='collection_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.imagestitle'),
        ),
        migrations.AddField(
            model_name='cinemamodel',
            name='seo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.seoblock'),
        ),
        migrations.CreateModel(
            name='BannerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(choices=[(0, 'main'), (1, 'news')], default=0)),
                ('is_published', models.BooleanField(default=False)),
                ('rotation_speed', models.IntegerField(null=True)),
                ('collection_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.imagestitle')),
            ],
            options={
                'db_table': 'banner',
            },
        ),
    ]
