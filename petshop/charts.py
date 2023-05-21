from abc import ABC, abstractmethod
from datetime import datetime
from django.db.models import Count
from django.shortcuts import render

from adoption.models import Adoption


class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass


class ChartCreator(ABC):
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, data):
        for observer in self.observers:
            observer.update(data)

    @abstractmethod
    def create_chart(self, request):
        pass


class AlbaChartCreator(ChartCreator):
    def create_chart(self, request):
        data = (
            Adoption.objects.filter(adapost='alba')
            .values('created')
            .annotate(adoption_count=Count('id'))
            .order_by('created')
        )
        adoption_count_data = []
        date_labels = []
        for item in data:
            adoption_count_data.append(item['adoption_count'])
            date_labels.append(item['created'].strftime('%Y-%m-%d'))

        unique_dates = list(set(date_labels))
        final_adoption_count_data = []
        for unique_date in unique_dates:
            total_count = 0
            for item in data:
                if item['created'].strftime('%Y-%m-%d') == unique_date:
                    total_count += item['adoption_count']
            final_adoption_count_data.append(total_count)

        chart_data = {
            'labels': unique_dates,
            'datasets': [{
                'label': 'Adoption Count',
                'data': final_adoption_count_data,
                'fill': 'false',
                'borderColor': 'rgb(0, 0, 0)',
                'lineTension': 0.1
            }]
        }

        self.notify(chart_data)
        return chart_data


class ClujChartCreator(ChartCreator):
    def create_chart(self, request):
        data = (
            Adoption.objects.filter(adapost='cluj')
            .values('created')
            .annotate(adoption_count=Count('id'))
            .order_by('created')
        )
        adoption_count_data = []
        date_labels = []
        for item in data:
            adoption_count_data.append(item['adoption_count'])
            date_labels.append(item['created'].strftime('%Y-%m-%d'))

        unique_dates = list(set(date_labels))
        final_adoption_count_data = []
        for unique_date in unique_dates:
            total_count = 0
            for item in data:
                if item['created'].strftime('%Y-%m-%d') == unique_date:
                    total_count += item['adoption_count']
            final_adoption_count_data.append(total_count)

        chart_data = {
            'labels': unique_dates,
            'datasets': [{
                'label': 'Adoption Count',
                'data': final_adoption_count_data,
                'fill': 'false',
                'borderColor': 'rgb(0, 0, 0)',
                'lineTension': 0.1
            }]
        }

        self.notify(chart_data)
        return chart_data


class SibiuChartCreator(ChartCreator):
    def create_chart(self, request):
        data = (
            Adoption.objects.filter(adapost='sibiu')
            .values('created')
            .annotate(adoption_count=Count('id'))
            .order_by('created')
        )
        adoption_count_data = []
        date_labels = []
        for item in data:
            adoption_count_data.append(item['adoption_count'])
            date_labels.append(item['created'].strftime('%Y-%m-%d'))

        unique_dates = list(set(date_labels))
        final_adoption_count_data = []
        for unique_date in unique_dates:
            total_count = 0
            for item in data:
                if item['created'].strftime('%Y-%m-%d') == unique_date:
                    total_count += item['adoption_count']
            final_adoption_count_data.append(total_count)

        chart_data = {
            'labels': unique_dates,
            'datasets': [{
                'label': 'Adoption Count',
                'data': final_adoption_count_data,
                'fill': 'false',
                'borderColor': 'rgb(0, 0, 0)',
                'lineTension': 0.1
            }]
        }

        self.notify(chart_data)
        return chart_data


class ChartDecorator(ChartCreator):
    def __init__(self, chart_creator):
        self.chart_creator = chart_creator

    def create_chart(self, request):
        chart_data = self.chart_creator.create_chart(request)
        data = chart_data['datasets'][0]['data']
        date_labels = chart_data['labels']

        first_date = datetime.strptime(date_labels[0], '%Y-%m-%d')
        last_date = datetime.strptime(date_labels[-1], '%Y-%m-%d')
        months_passed = (last_date.year - first_date.year) * 12 + (last_date.month - first_date.month) + 1

        total_adoptions = sum(data)
        overall_average = total_adoptions / months_passed

        if overall_average > 10:
            chart_data['datasets'][0]['borderColor'] = 'rgb(0, 128, 0)'
        else:
            chart_data['datasets'][0]['borderColor'] = 'rgb(255, 0, 0)'

        return render(request, 'charts.html', {'chart_data': chart_data})


class AdoptionChartObserver(Observer):
    def update(self, data):
        pass


class ChartCreatorFactory:
    @staticmethod
    def create_chart_creator(chart_type):
        if chart_type == 'alba':
            return AlbaChartCreator()
        if chart_type == 'sibiu':
            return SibiuChartCreator()
        if chart_type == 'cluj':
            return ClujChartCreator()

        else:
            raise ValueError(f"Invalid chart type: {chart_type}")
