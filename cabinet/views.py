from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from cabinet.forms import VisitModelForm
from cabinet.models import Gallery, License, Master, Price, Review


def get_paginator(request, data, per_page):
    paginator = Paginator(data, per_page)

    return paginator.get_page(request.GET.get("page"))


def main(request):
    context = {
        "masters": Master.objects.all(),
    }
    return render(request, "main.html", context)


def price(request):
    context = {"prices": Price.objects.all().order_by('price')}
    return render(request, "cabinet/price.html", context)


class AppointmentView(View):
    def get(self, request):
        context = {
            "form": VisitModelForm(),
        }
        return render(request, "cabinet/appointment.html", context)

    def post(self, request):
        form = VisitModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("thanks_page")

        context = {
            "form": form,
        }
        return render(request, "cabinet/appointment.html", context)


def license_page(request):
    context = {"licenses": License.objects.all()}
    return render(request, "cabinet/license.html", context)


def gallery(request):
    context = {"galleries": Gallery.objects.all()}
    return render(request, "cabinet/gallery.html", context)


def preparation(request):
    return render(request, "cabinet/preparation.html")


def reviews(request):
    page_obj = get_paginator(
        request, Review.objects.all(), settings.REVIEWS_PER_PAGE
    )
    context = {
        "page_obj": page_obj,
    }

    return render(request, "cabinet/reviews.html", context)


class ThanksView(View):
    def get(self, request):
        return render(request, "cabinet/thanks_page.html")


def get_services_by_master(request, master_id):
    master = get_object_or_404(Master, id=master_id)

    services = master.services.all()

    services_data = [
        {"id": service.id, "name": service.name} for service in services
    ]

    return JsonResponse({"services": services_data})
