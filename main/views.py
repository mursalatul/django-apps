
from django.http import HttpResponse
from django.template import loader
# Create your views here.

from main.models import *
def main(request):
    app_data = {
        'app_names' : AllApps.objects.all(),
    }
    main_page = loader.get_template('main.html')
    return HttpResponse(main_page.render(app_data, request))
