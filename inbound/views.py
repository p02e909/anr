import csv
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render
from .forms import CSVUploadForm
from .models import OrderModel
from io import TextIOWrapper


def upload_csv(request):
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csvfile = request.FILES["file"]
            csvfile_wrapper = TextIOWrapper(csvfile, encoding="utf-8")
            reader = csv.DictReader(csvfile_wrapper)
            for row in reader:
                try:
                    OrderModel.objects.update_or_create(
                        product_id=row["ID"],
                        jap_name=row["Japanese name"],
                        eng_name=row["English name"],
                        category=row["Category"],
                        start_date=row["Start date"],
                        end_date=row["End date"],
                    )
                except Exception:
                    pass
            return HttpResponseRedirect(reverse("show_data"))
    else:
        form = CSVUploadForm()
    return render(request, "upload.html", {"form": form})


def load_filtered_data_from_csv(product_id, category):
    err = ""
    orders = OrderModel.objects.all()
    try:
        if product_id:
            orders = orders.filter(product_id=product_id)
        if category:
            orders = orders.filter(category=category)
    except Exception as e:
        err = str(e)
    return orders, err


def show_data(request):
    product_id = request.GET.get("product_id", "")
    category = request.GET.get("category", "")

    filtered_data, err = load_filtered_data_from_csv(product_id, category)

    # Paginate the data
    paginator = Paginator(filtered_data, 10)  # 10 items per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "data.html",
        {
            "page_obj": page_obj,
            "product_id": product_id,
            "category": category,
            "error_message": err,
        },
    )
