from django.contrib import admin
from .models import (
    User, Profile, Level, Object, ObjectPart,
    Progress, HistoryLevel, History_images
)
from django.utils.html import format_html


# ==========================
# Вспомогательные функции
# ==========================
def image_preview(obj):
    if obj and obj.image:
        return format_html('<img src="{}" style="max-height: 80px;">', obj.image.url)
    return "-"


# ==========================
# Inline для частей объекта
# ==========================
class ObjectPartInline(admin.TabularInline):
    model = ObjectPart
    extra = 1
    fields = ("image", "center_x", "center_y", "preview")
    readonly_fields = ("preview",)

    def preview(self, obj):
        return image_preview(obj)


# ==========================
# Inline для объектов уровня
# ==========================
class ObjectInline(admin.TabularInline):
    model = Object
    extra = 1
    fields = ("name",)
    show_change_link = True


# ==========================
# User + Profile
# ==========================
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("login",)
    inlines = [ProfileInline]


# ==========================
# Level + объекты
# ==========================
@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ("name", "star_pr", "preview")
    inlines = [ObjectInline]

    def preview(self, obj):
        if obj.level_image:
            return format_html('<img src="{}" style="max-height: 100px;">', obj.level_image.url)
        return "-"


# ==========================
# Объекты
# ==========================
@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ("id", "level", "name")
    inlines = [ObjectPartInline]


# ==========================
# Части объекта
# ==========================
@admin.register(ObjectPart)
class ObjectPartAdmin(admin.ModelAdmin):
    list_display = ("id", "parent", "center_x", "center_y", "preview")
    readonly_fields = ("preview",)

    def preview(self, obj):
        return image_preview(obj)


# ==========================
# Прогресс
# ==========================
@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "level", "completed")
    list_filter = ("completed", "level")


# ==========================
# История
# ==========================
class HistoryImageInline(admin.TabularInline):
    model = HistoryLevel.image.through
    extra = 1


@admin.register(HistoryLevel)
class HistoryLevelAdmin(admin.ModelAdmin):
    list_display = ("level", "short_text")
    inlines = [HistoryImageInline]

    def short_text(self, obj):
        return (obj.text[:50] + "...") if len(obj.text) > 50 else obj.text


@admin.register(History_images)
class HistoryImageAdmin(admin.ModelAdmin):
    list_display = ("name", "preview")

    def preview(self, obj):
        if obj.history_image:
            return format_html('<img src="{}" style="max-height: 80px;">', obj.history_image.url)
        return "-"
