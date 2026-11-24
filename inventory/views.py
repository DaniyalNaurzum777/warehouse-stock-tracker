import logging

from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ProductForm
from .models import Product

logger = logging.getLogger(__name__)


def product_list(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            logger.info("Тауар тіркелді: product_id=%s", product.pk)
            if product.is_low_stock:
                logger.warning(
                    "Қор аз: product_id=%s quantity=%s min_quantity=%s",
                    product.pk,
                    product.quantity,
                    product.min_quantity,
                )
                messages.warning(request, "Тауар тіркелді. Ескерту: қор аз!")
            else:
                messages.success(request, "Тауар сәтті тіркелді.")
            return redirect("product_list")

        logger.warning("Тауар формасы тексеруден өтпеді")
    else:
        form = ProductForm()

    products = Product.objects.all()
    return render(
        request,
        "inventory/product_list.html",
        {"form": form, "products": products},
    )


def delete_product(request, pk):
    if request.method == "POST":
        Product.objects.filter(pk=pk).delete()
        messages.info(request, "Тауар жойылды.")
    return redirect("product_list")
