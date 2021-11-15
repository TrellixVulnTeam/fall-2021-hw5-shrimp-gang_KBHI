# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def move_content_from_documents_to_ocr_app(apps, schema_editor):
    DocumentPage = apps.get_model('documents', 'DocumentPage')
    DocumentPageContent = apps.get_model('ocr', 'DocumentPageContent')

    for document_page in DocumentPage.objects.using(schema_editor.connection.alias).all():
        DocumentPageContent.objects.using(schema_editor.connection.alias).create(
            document_page=document_page,
            content=document_page.content_old or ''
        )


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0002_documentpagecontent'),
    ]

    operations = [
        migrations.RunPython(move_content_from_documents_to_ocr_app),
    ]
