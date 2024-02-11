from django.http import HttpResponse
from django.shortcuts import render


def main_page(request):
    return render(request, 'final-project/main_page.html')


def sendHTML(request):
    return render(request, 'final-project/sendHTML.html')


def set_cookie(request):
    cookie_name = request.GET.get('name')
    cookie_value = request.GET.get('value')
    if cookie_name and cookie_value:
        response = HttpResponse("Cookie Set")
        response.set_cookie(cookie_name, cookie_value, httponly=True)
        return response
    else:
        return HttpResponse("Missing parameter")


def get_cookie(request, cookie_name):
    cookie_value = request.COOKIES.get(cookie_name)
    if cookie_value:
        return HttpResponse(f"Cookie Value: {cookie_value}")
    else:
        return HttpResponse("Cookie not found")


def set_header(request):
    header_name = request.GET.get('name')
    header_value = request.GET.get('value')
    if header_name and header_value:
        response = HttpResponse("Header Set")
        response[header_name] = header_value
        return response
    else:
        return HttpResponse("Missing parameter")


def get_header(request, header_name):
    header_value = request.headers.get(header_name)
    if header_value:
        return HttpResponse(f"Header Value: {header_value}")
    else:
        return HttpResponse("Header not found")
