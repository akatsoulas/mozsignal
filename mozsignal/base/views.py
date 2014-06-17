from django.shortcuts import render


def main(request):
    """Main page of the website."""
    return render(request, 'base.html')
