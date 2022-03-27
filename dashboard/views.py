from django.shortcuts import render
from .models import Staff  # on current view import staff model


import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# Create your views here.
def index(request):
	# create a variable called staff and assign
	staff = Staff.objects.all()
	# create a variable called contex and assign key: value

	context = {  
              
              'staff' : staff,
	}
	return render(request, 'dashboard/index.html', context)




def payslip(request, pk):
    staff = Staff.objects.get(id=pk)
    template_path = 'dashboard/staff_payslip.html'
    context = {
        'staff': staff,
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
