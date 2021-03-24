from django.forms import ModelForm

from apps.product.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['vendor', 'slug', 'thumbnail', 'date_added']