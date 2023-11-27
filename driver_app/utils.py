from calendar import HTMLCalendar
from datetime import datetime as dtime, date, time
import datetime
from .models import Event
 
 
class EventCalendar(HTMLCalendar):
    def __init__(self, events=None):
        super(EventCalendar, self).__init__()
        self.events = events
 
    def formatday(self, day, weekday, events):
        """
        Return a day as a table cell.
        """
        events_from_day = events.filter(day__day=day)
        events_html = "<ul>"
        for event in events_from_day:
            events_html += event.get_absolute_url() + "<br>"
        events_html += "</ul>"
 
        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        else:
            return '<td class="%s">%d%s</td>' % (self.cssclasses[weekday], day, events_html)
 
    def formatweek(self, theweek, events):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd, events) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s
 
    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """
 
        events = Event.objects.filter(day__month=themonth)
 
        list = []
        cell = list.append
        cell('<table border="0" cellpadding="0" cellspacing="0" class="month">')
        cell('\n')
        cell(self.formatmonthname(theyear, themonth, withyear=withyear))
        cell('\n')
        cell(self.formatweekheader())
        cell('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            cell(self.formatweek(week, events))
            cell('\n')
        cell('</table>')
        cell('\n')
        return ''.join(list)