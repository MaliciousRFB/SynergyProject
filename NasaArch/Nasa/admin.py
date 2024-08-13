from django.contrib import admin
from django import forms
from .models import News, Astro, Vehicle, LifeInSpace, UniverseList
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# News

class EditAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'content', 'photo', 'date')
    search_fields = ('title', 'content')
    list_filter = ('id', 'date')
    fields = ('title', 'content', 'photo',)
    readonly_fields = ('id', 'date')
    form = EditAdminForm

admin.site.register(News, NewsAdmin)


# List of astronauts

class Edit2AdminForm(forms.ModelForm):
    bio = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Astro
        fields = '__all__'

class AstroAdmin(admin.ModelAdmin):
    list_display = ('astronaut',  'bio', 'photo')
    search_fields = ('astronaut', 'bio')
    list_filter = ('id', 'astronaut')
    form = Edit2AdminForm

admin.site.register(Astro, AstroAdmin)



#List of vehicles

class Edit3AdminForm(forms.ModelForm):
    about = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('spaceship',  'about', 'photo')
    search_fields = ('spaceship', 'about')
    list_filter = ('id', 'spaceship')
    form = Edit3AdminForm

admin.site.register(Vehicle, VehicleAdmin)



class Edit4AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = LifeInSpace
        fields = '__all__'

class LifeInSpaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'photos')
    search_fields = ('title', 'content')
    list_filter = ('id', 'title')
    form = Edit4AdminForm

admin.site.register(LifeInSpace, LifeInSpaceAdmin)


class UniverseListAdmin(admin.ModelAdmin):
     list_display = ('id', 'space_object', 'read', 'photo')
     search_fields = ('space_object', 'id')
     list_filter = ('id', 'space_object')

admin.site.register(UniverseList, UniverseListAdmin)