from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import Currency
import requests
import statistics
from numpy import corrcoef
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ParametersForm


def index(request):
    if request.method == 'POST':
        form = ParametersForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            start = cd['start_at']
            end = cd['end_at']
            choice = cd['choice']
            if choice == '1':
                return HttpResponseRedirect(reverse('metrics', args=[start, end]))
            if choice == '2':
                cur1 = cd['cur1']
                cur2 = cd['cur2']
                symbols = cur1 + "," + cur2
                return HttpResponseRedirect(reverse('correlation', args=[start, end, symbols]))
    else:
        form = ParametersForm()
    return render(request, 'Parameters/parameters.html', {'form': form})


class MetricsList(APIView):
    #http://127.0.0.1:8000/metrics/start_at=2020-03-23&end_at=2020-03-25
    def get(self, request, start_at, end_at):
        curs = Currency.objects.all()
        curs = list(curs)
        data_list = {}
        data_metrics = []
        for x in curs:
            data_list[str(x)] = []
        path = "https://api.exchangeratesapi.io/history?start_at=" \
               + start_at + "&end_at=" + end_at
        r = requests.get(path)
        rates = r.json()['rates']
        for x in rates:
            for y in rates[x]:
                data_list[y].append(rates[x][y])
        for x in data_list:
            std_dev = statistics.stdev(data_list[x])
            std_dev = float('{:.4f}'.format(std_dev))
            avg = statistics.mean(data_list[x])
            avg = float('{:.4f}'.format(avg))
            metrics = {'std_dev': std_dev, 'avg': avg}
            range_data = {'currency': x, 'metrics': metrics}
            data_metrics.append(range_data)
        serializer = RangeSerializer(data_metrics, many=True)
        return Response(serializer.data)


class Correlation(APIView):
    # http://127.0.0.1:8000/metrics/correlation/start_at=2020-03-23&end_at=2020-03-25&symbols=ILS,JPY
    def get(self, request, start_at, end_at, symbols):
        path = "https://api.exchangeratesapi.io/history?start_at=" + start_at \
               + "&end_at=" + end_at + "&symbols=" + symbols
        r = requests.get(path)
        cur1 = symbols[:3]
        cur2 = symbols[4:]
        cur1_list = []
        cur2_list = []
        for x in r.json()['rates']:
            cur1_list.append(r.json()['rates'][x][cur1])
            cur2_list.append(r.json()['rates'][x][cur2])
        correlation = corrcoef(cur1_list, cur2_list)[0][1]
        correlation = float('{:.4f}'.format(correlation))
        data = [{'currency1': cur1, 'currency2': cur2, 'base': 'EUR', 'correlation': correlation}]
        serializer = CorrelationSerializer(data, many=True)
        return Response(serializer.data)