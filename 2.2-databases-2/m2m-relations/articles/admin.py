from django.contrib import admin
from .models import Article, Tag, ArticleTag
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if not form.cleaned_data or form.cleaned_data.get('DELETE') is True:
                continue
            if form.cleaned_data.get('is_main', False):
                count += 1
        if count > 1:
            raise ValidationError('Слишком много главных тегов')
        if count == 0:
            raise ValidationError('Добавьте главный тег')


class ScopeInline(admin.TabularInline):
    model = Tag.article.through
    formset = ScopeInlineFormset
    extra = 5


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [
        ScopeInline,
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

