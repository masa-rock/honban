from django.contrib import admin
from .models import Question, Choice, Realsimulation
# 210430_import_export_csvインポートのため追加
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

admin.site.register(Realsimulation)
admin.site.register(Question) 
admin.site.register(Choice)