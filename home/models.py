from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Category(MPTTModel):
	title = models.CharField(max_length=50, db_index=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	slug = models.SlugField(max_length=50, unique=True)

	class MPTTMeta:
		order_insertion_by = ['title']

	class Meta:
		ordering = ('title',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.title

	def __str__(self):
		full_path = [self.title]
		k = self.parent

		while k is not None:
			full_path.append(k.title)
			k = k.parent

		return ' / '.join(full_path[::-1])

	def get_recursive_product_count(self):
		return Product.objects.filter(category__in=self.get_descendants(include_self=True)).count()

class Product(models.Model):
	category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
	name = models.CharField(max_length=25, db_index=True)
	slug = models.SlugField(max_length=25, db_index=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)

	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	description = models.TextField(blank=True)

	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)
		verbose_name = 'product'
		verbose_name_plural = 'products'

	def __str__(self):
		return self.name