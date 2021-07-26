from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import DailyStatement, Sale
from datetime import datetime

# Create your views here.
def index(request):
    print('hello index')
    return render(request, 'cafe/index.html')


# Entry
def entry(request):
    sales = Sale.objects.all()
    return render(request, 'cafe/entry.html', {'sales': sales})


def add_sale(request):
    if request.method == 'POST':
        try:
            ## Creating Sale ##
            sale = Sale()
            # sale.timestamp = request.POST.get('sale-time')
            sale.timestamp = datetime.now()

            sale.amount = request.POST.get('sale-amt')
            sale.desc = request.POST.get('sale-desc')
            sale.payment_type = request.POST.get('sale-pmt-type')
            sale_done_by = request.POST.get('sale-by')
            user = User.objects.get(username= sale_done_by)
            sale.user = user
            sale.save()

            daily, created = DailyStatement.objects.get_or_create(timestamp__day= datetime.now().day)
            daily.statements.add(sale)
            daily.save()

            response = {
                'msg' : f'{sale.user.username} has done sale of {sale.amount} on {sale.timestamp}',
                'status': True
            }
        except Exception as e:
            print('------------ EXCEPTION')
            response = {
                'msg' : str(e),
                'status': False
            }
        return JsonResponse(response)
