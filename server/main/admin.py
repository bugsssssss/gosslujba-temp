from django.contrib import admin
from .models import *


admin.site.register(Contacts)
admin.site.register(BannerModel)
admin.site.register(AboutModel)
admin.site.register(ServiceModel)
admin.site.register(PicturesModel)
admin.site.register(Statistics)
admin.site.register(UsefulLinks)
admin.site.register(MailsModel)
admin.site.register(LaboratoryModel)
admin.site.register(ApparatModel)
admin.site.register(HomeAboutModel)
admin.site.register(Structure)
admin.site.register(LegalStatusModel)
admin.site.register(ActivityModel)
admin.site.register(Weekend)
admin.site.register(PartnersModel)
admin.site.register(ManagementModel)
admin.site.register(CorruptionModel)


@admin.register(Announce)
class AnnounceAdmin(admin.ModelAdmin):
    readonly_fields = ("picture_count",)


@admin.register(OpenDataFiles)
class OpenDataFilesAdmin(admin.ModelAdmin):
    readonly_fields = ("size",)


@admin.register(CorruptionFiles)
class CorruptionFilesAdmin(admin.ModelAdmin):
    readonly_fields = ("size",)


@admin.register(FinanceFiles)
class FinanceFilesAdmin(admin.ModelAdmin):
    readonly_fields = ("size",)


@admin.register(LegalStatusFiles)
class LegalStatusFilesAdmin(admin.ModelAdmin):
    readonly_fields = ("size",)


@admin.register(StructureFiles)
class StructureFilesAdmin(admin.ModelAdmin):
    readonly_fields = ("size",)


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ("picture_count",)


@admin.register(PhotoGalery)
class PhotoGaleryAdmin(admin.ModelAdmin):
    readonly_fields = ("picture_count",)
