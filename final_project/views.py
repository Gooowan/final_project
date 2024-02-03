from django.shortcuts import render


def main_page(request):
    return render(request, 'final-project/main_page.html')
