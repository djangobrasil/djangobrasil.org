from django.views.generic import dates

from djangobrasil.blog.models import Entry


class Index(dates.ArchiveIndexView):
    queryset = Entry.published
    date_field = "pub_date"
    num_latest = 5


class YearArchive(dates.YearArchiveView):
    queryset = Entry.published
    date_field = "pub_date"


class MonthArchive(dates.MonthArchiveView):
    queryset = Entry.published
    date_field = "pub_date"
    month_format = '%m'


class DayArchive(dates.DayArchiveView):
    queryset = Entry.published
    date_field = "pub_date"
    month_format = '%m'


class DateDetail(dates.DateDetailView):
    queryset = Entry.published
    date_field = "pub_date"
    month_format = '%m'
    slug_field = 'slug'
