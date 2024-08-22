import csv
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render
from inbound.forms import CSVUploadForm
from inbound.models import MenuModel, ElementModel
from io import TextIOWrapper
from bulk_sync import bulk_sync


def strip_spaces(row):
    return {key.strip(): value.strip() for key, value in row.items()}

def upload_menu(request):
    menu_models = []
    menu_code = []
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csvfile = request.FILES["file"]
            csvfile_wrapper = TextIOWrapper(csvfile, encoding="utf-8")
            reader = csv.DictReader(csvfile_wrapper)
            for line in reader:
                line = strip_spaces(line)
                menu_code.append(line['menu_code'])
                try:
                    menu = MenuModel(
                        menu_code=line['menu_code'], 
                        menu_name=line['menu_name'],
                    )
                    menu_models.append(menu)
                except Exception as e:
                    print(e) # handle logger here
                    pass
        bulk_sync(
            new_models=menu_models,
            db_class=MenuModel,
            filters=None,
            fields=['menu_code', 'menu_name'],
            key_fields=['menu_code', 'id']
        )
        return HttpResponseRedirect(reverse("list_menu_uploaded"))
    else:
        form = CSVUploadForm()

    return render(request, "upload.html", {"form": form})

def load_filtered_data_from_csv(menu_code, menu_name):
    err = ""
    menu = MenuModel.objects.all()
    try:
        if menu_code:
            menu = menu.filter(menu_code=menu_code)
        if menu_name:
            menu = menu.filter(menu_name=menu_name)
    except Exception as e:
        err = str(e)
    return menu, err


def list_menu_uploaded(request):
    menu_code = request.GET.get("menu_code", "")
    menu_name = request.GET.get("menu_name", "")

    filtered_data, err = load_filtered_data_from_csv(menu_code, menu_name)

    # Paginate the data
    paginator = Paginator(filtered_data, 10)  # 10 items per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "data_menu.html",
        {
            "page_obj": page_obj,
            "menu_code": menu_code,
            "menu_name": menu_name,
            "error_message": err,
        },
    )


def upload_element(request):
    element_models = []
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csvfile = request.FILES["file"]
            csvfile_wrapper = TextIOWrapper(csvfile, encoding="utf-8")
            reader = csv.DictReader(csvfile_wrapper)
            for line in reader:
                line = strip_spaces(line)
                try:
                    element = ElementModel(
                        element_code=line['element_code'], 
                        element_name=line['element_name'],
                    )
                    element_models.append(element)
                except Exception as e:
                    print(e) # handle logger here
                    pass
        bulk_sync(
            new_models=element_models,
            db_class=ElementModel,
            filters=None,
            fields=['element_code', 'element_name'],
            key_fields=['element_code', 'id']
        )
        return HttpResponseRedirect(reverse("list_element_uploaded"))
    else:
        form = CSVUploadForm()

    return render(request, "upload.html", {"form": form})

def load_filtered_data_from_csv(element_code, element_name):
    err = ""
    element = ElementModel.objects.all()
    
    try:
        if element_code:
            element = element.filter(element_code=element_code)
        if element_name:
            element = element.filter(element_name=element_name)
        print(element,23123123)
    except Exception as e:
        err = str(e)
    return element, err


def list_element_uploaded(request):
    element_code = request.GET.get("element_code", "")
    element_name = request.GET.get("element_name", "")

    filtered_data, err = load_filtered_data_from_csv(element_code, element_name)
    # Paginate the data
    paginator = Paginator(filtered_data, 10)  # 10 items per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "data_element.html",
        {
            "page_obj": page_obj,
            "element_code": element_code,
            "element_name": element_name,
            "error_message": err,
        },
    )
