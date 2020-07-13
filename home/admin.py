from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Category, Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
	prepopulated_fields = {'slug': ('title',)}

	mptt_indent_field = "title"
	list_display = ('parent', 'tree_actions', 'indented_title', 'slug',
		'related_products_count', 'related_products_cumulative_count')
	list_display_links = ('indented_title',)

	def get_queryset(self, request):
		qs = super().get_queryset(request)

		# Add cumulative product count
		qs = Category.objects.add_related_count(qs, Product, 'category',
			'products_cumulative_count', cumulative=True)

		# Add non cumulative product count
		qs = Category.objects.add_related_count(qs, Product, 'category',
			'products_count', cumulative=False)
		return qs

	def related_products_count(self, instance):
		return instance.products_count

	related_products_count.short_description = 'Related products (for this specific category)'

	def related_products_cumulative_count(self, instance):
		return instance.products_cumulative_count
	related_products_cumulative_count.short_description = 'Related products (in tree)'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}