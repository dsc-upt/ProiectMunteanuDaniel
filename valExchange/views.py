from django.shortcuts import render

# Create your views here.
from valExchange.models import Exchange

def index_view(request):
    converter = Exchange('https://api.exchangerate-api.com/v4/latest/USD')
    context = {"curr": converter.currencies}
    if request.method == "GET":
        context["iValue"] = 0
        context["fValue"] = 0.0
        context["iCurr"] = "USD"
        context["fCurr"] = "USD"
    if request.method == "POST":
        context["iValue"] = request.POST.get("initial")
        context["iCurr"] = request.POST.get("cIn")
        context["fCurr"] = request.POST.get("cOut")
        context["fValue"] = converter.convert(context["iCurr"], context["fCurr"], context["iValue"])
    return render(request, "home.html", context)