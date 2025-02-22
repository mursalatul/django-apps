
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def main(request):
    main_page = loader.get_template('main.html')
    return HttpResponse(main_page.render())