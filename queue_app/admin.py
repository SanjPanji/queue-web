from django.contrib import admin
from .models import Item, Review  # импортируем модели

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # какие поля показывать в общем списке
    search_fields = ('name',)  # поиск по названию

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_review')  # свои методы можно указывать
    search_fields = ('review',)  # поиск по тексту отзыва

    def short_review(self, obj):
        return obj.review[:50] + ('...' if len(obj.review) > 50 else '')
    short_review.short_description = 'Отзыв'