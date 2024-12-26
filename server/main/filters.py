from django.db.models import Q
from .models import NewsModel
import django_filters

class NewsFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_title')

    class Meta:
        model = NewsModel
        fields = ['search']

    def filter_title(self, queryset, name, value):
        request = self.request
        lang = request.headers.get('Accept-Language', 'uz')

        if lang == "en":
            return queryset.filter(Q(title_en__icontains=value))
        elif lang == "ru":
            return queryset.filter(Q(title_ru__icontains=value))
        return queryset.filter(Q(title_uz__icontains=value))
    
class LaboratoryFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_title')

    class Meta:
        model = NewsModel
        fields = ['search']

    def filter_title(self, queryset, name, value):
        request = self.request
        lang = request.headers.get('Accept-Language', 'uz')

        if lang == "en":
            return queryset.filter(Q(title_en__icontains=value))
        elif lang == "ru":
            return queryset.filter(Q(title_ru__icontains=value))
        return queryset.filter(Q(title_uz__icontains=value))
    
class ApparatFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_title')

    class Meta:
        model = NewsModel
        fields = ['search']

    def filter_title(self, queryset, name, value):
        request = self.request
        lang = request.headers.get('Accept-Language', 'uz')

        if lang == "en":
            return queryset.filter(Q(title_en__icontains=value))
        elif lang == "ru":
            return queryset.filter(Q(title_ru__icontains=value))
        return queryset.filter(Q(title_uz__icontains=value))
    
