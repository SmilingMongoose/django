from django.shortcuts import render, redirect
from .forms import TickerInput
from .models import Visitor, Ticker
import requests, json

# Create your views here.
def index(request):
    input_text = request.POST.get('visitor_input', None)
    if input_text == None:
        input_text = ''
    else:
        input_text = request.POST.get('visitor_input', "you didn't enter anything")
    
    visitors = Visitor.objects.all()

    context = {
        'visitors': visitors,
        'input_text': input_text
    }
    return render(request, 'index.html', context)


def view_data(request):

    api_res = ''
    entered_ticker = ''
    data_open_close = []
    data_close = []
    tickers = Ticker.objects.all()


    if request.method == 'POST':
        form = TickerInput(request.POST)
        entered_ticker = request.POST['ticker_input']

        try:
            api_request = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey=EVKWQOL8PYGMPDWC".format(entered_ticker))
            print("api_request:", api_request)

            api_res = api_request.json()['Time Series (Daily)']
            data_open_close = [[x, api_res[x]['1. open'], api_res[x]['4. close']] for x in api_res]
            data_close = [[x, api_res[x]['4. close']] for x in api_res]


        except Exception as e:
            api_res = "Error..."

        context = {
            'form': form,
            'ticker': tickers,
            'api_res': api_res,
            'data_open_close': data_open_close,
            'data_close': data_close,
            'entered_ticker': entered_ticker   
        }

        return render(request, 'data_page.html', context)
    else:
        form = TickerInput()

    context = {
        'form': form,
        'ticker': tickers,
        'api_res': api_res,
        'data_open_close': data_open_close,
        'data_close': data_close,
        'entered_ticker': entered_ticker   
    }
    return render(request, 'data_page.html', context)

def view_data_tmp(tkr):

    api_request = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey=EVKWQOL8PYGMPDWC".format(tkr))

    if api_request.status_code == 200:
        return api_request.json()['Meta Data']['2.Symbol']
    else:
        return 'Something went wrong...'