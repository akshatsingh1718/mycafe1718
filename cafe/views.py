from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import DailyStatement, Sale
from datetime import date, datetime

# Create your views here.
def index(request):
    print('hello index')
    return render(request, 'cafe/index.html')


# Entry
def entry(request):
    sales = Sale.objects.order_by('-pk')
    daily_sale, iscreated  = DailyStatement.objects.get_or_create(timestamp__day= datetime.now().day)
    return render(request, 'cafe/entry.html', {'sales': sales, 'dailySales': daily_sale})


def del_sale(request):
    if request.method == 'POST':
        try:
            sale_id = int(request.POST.get('sale-id'))
            sale = Sale.objects.get(pk = sale_id)
            msg = f'Sale done by {sale.user} of Rs. {sale.amount} at {sale.timestamp} has been deleted successfully.'
            amt = sale.amount
            pmt_type = sale.payment_type
            sale.delete()
            response = {
                'msg': msg,
                'status' : True,
                'amount': amt,
                'payment_type': pmt_type
            }
        except Exception as e:
            response = {
                'msg': str(e),
                'status' : False
            }
        return JsonResponse(response)
        

def add_sale(request):
    if request.method == 'POST':
        try:
            ## Creating Sale ##
            sale = Sale()
            # sale.timestamp = request.POST.get('sale-time')
            sale.timestamp = datetime.now()

            sale.amount = request.POST.get('amount')
            sale.desc = request.POST.get('description')
            sale.payment_type = request.POST.get('payment_type')
            sale_done_by = request.POST.get('user')
            user = User.objects.get(username= sale_done_by)
            sale.user = user
            sale.save()

            # Getting current day DailyStatus object to add new statement
            daily, is_created = DailyStatement.objects.get_or_create(timestamp__day= datetime.now().day)
            daily.statements.add(sale)
            daily.save()

            response = {
                'msg' : f'{sale.user.username} has done sale of {sale.amount} on {sale.timestamp}',
                'pk': sale.pk,
                'status': True
            }
        except Exception as e:
            response = {
                'msg' : str(e),
                'status': False
            }
        return JsonResponse(response)


def search_sale(request):
    if request.method == 'POST':
        search_date = request.POST.get('search-sale-date')
        print(f'{search_date} : {date.today()}')
        print(search_date == date.today())
        print(search_date is date.today())

        daily_stmt, is_created = DailyStatement.objects.get_or_create(timestamp = search_date)
    else:
        daily_stmt, is_created = DailyStatement.objects.get_or_create(timestamp = date.today())
    return render(request, 'cafe/search-sale.html', {'dailySales': daily_stmt})
