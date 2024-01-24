# Generated by Django 4.0.3 on 2024-01-23 02:23

import django.core.validators
from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_alter_notice_subsites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='body',
            field=models.CharField(blank=True, help_text='\n    <ul style=\'margin-left: 2rem;\'>\n        <li style=\'list-style: disc;\'>\n            Enter valid GitHub markdown -\n    <a href="https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax" target="_blank">see markdown guide</a>.\n    We\'re using <b>"code-friendly" mode</b>, so __ and _ will be rendered\n    literally! Use * and ** for italics/bold instead.\n    \n        </li>\n        <li style=\'list-style: disc;\'>\n            <b>This text will be displayed on a dedicated webpage</b>\n            that is linked to from the landing page notice.\n            If this field is left blank, there will be no link.\n            For notices with <b>static display</b>, this will be displayed on\n            the landing page in a block element, in addition to the dedicated\n            webpage.\n        </li>\n    </ul>\n    ', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice_class',
            field=models.CharField(choices=[('info', 'info'), ('warning', 'warning'), ('none', 'image')], default='', help_text='\n    <ul style=\'margin-left: 2rem;\'>\n        <li style=\'list-style: disc;\'>\n            A style class to set a color scheme for the notice - uses\n            <a\n                href=\'https://getbootstrap.com/docs/5.0/components/alerts/\'\n                target=\'_blank\'\n            >standard bootstrap styling</a>\n            (\n                <em>info</em>: blue,\n                <em>warning</em>: orange,\n            ).\n        </li>\n        <li style=\'list-style: disc;\'>\n            Use the <em>Cover Image</em> model for displaying banner images.\n            <span class="text-danger">\n              The <em>image</em> class is deprecated\n            </span>\n            - existing image notices should be migrated to\n            <em>Cover Image</em> records.\n        </li>\n    </ul>\n    ', max_length=16),
        ),
        migrations.AlterField(
            model_name='notice',
            name='static_display',
            field=models.BooleanField(default=False, help_text="\n    <ul style='margin-left: 2rem;'>\n        <li style='list-style: disc;'>\n            Display the notice as a static block beneath the GA logo, in addition\n            to the default rotating notice (i.e. the banner beneath the navbar).\n        </li>\n        <li style='list-style: disc;'>\n            Ideally, this should be checked\n            <b style='color: firebrick;'>only for a single, high-priority notice</b>\n            to prevent cluttering of the landing page.\n        </li>\n        <li style='list-style: disc;'>\n            Static notices show the <b>body</b> on the landing page in addition\n            to the <b>short description</b>. If the block notice is dismissed\n            by the user, they can still access and click through the rotating\n            notice.\n        </li>\n    </ul>\n    "),
        ),
        migrations.CreateModel(
            name='CoverImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('img', models.FileField(upload_to=home.models.get_upload_path)),
                ('display_width', models.IntegerField(help_text='\n    For images with a banner-style aspect ratio (1000x300) this should be set\n    set to 100% (the default). For a square image 50% would be more\n    appropriate.\n    ', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Display width (%)')),
                ('enabled', models.BooleanField(default=False, help_text='Display on the Galaxy Australia landing page.')),
                ('is_published', models.BooleanField(default=False, help_text='Unpublished content is visible to admin users only. Use this to review content before release to public users.')),
                ('subsites', models.ManyToManyField(default=home.models.default_subsite, help_text='Select which subdomain sites should display the notice.', to='home.subsite')),
            ],
        ),
    ]
