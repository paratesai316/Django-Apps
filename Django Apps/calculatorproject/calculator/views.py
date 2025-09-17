from django.shortcuts import render

def calculator_view(request):
    display = "0"
    error = None
    button_list = ["1", "2", "3", "+", "4", "5", "6", "-", "7", "8", "9", "*", "C", "0", "=", "/"]

    if request.method == "POST":
        expr = request.POST.get("display", "0")
        btn = request.POST.get("btn")
        if btn == "C":
            display = "0"
        elif btn == "=":
            try:
                display = str(eval(expr, {"__builtins__": {}}, {}))
            except Exception:
                error = "Invalid Expression"
                display = "0"
        else:
            if expr == "0":
                display = btn
            else:
                display = expr + btn

    return render(request, "calculator/home.html", {"display": display, "error": error, "button_list": button_list})
