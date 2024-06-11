from django.contrib import admin
from .models import Product

class NewViewAdmin(admin.ModelAdmin): #создаём новый класс для представления товаров в админке

    list_display = ['column1', 'column2', 'column3', 'user'] # генерируем список имён всех полей для более красивого отображения. # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами. list_display = ("column1", "column3") - если выводим только конкретные поля
    list_filter = [field.name for field in Product._meta.get_fields()] # добавляем примитивные фильтры в нашу админку (но это скорее не фильры, а сортировщики). list_filter = ("column1", "column3") - если выводим фильтры только конкретных полей.
    search_fields = [field.name for field in Product._meta.get_fields()]  # тут всё очень похоже на фильтры из запросов в базу

    def user(self, obj):
        return ", ".join([user.username for user in obj.user.all()]) # эту функцию мы вставили в виде строки в list_display

admin.site.register(Product, NewViewAdmin)
