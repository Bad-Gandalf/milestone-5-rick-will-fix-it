from djqscsv import write_csv
from datetime import datetime, timedelta, time
from .models import BugWorkTime

data_file = 'workflow.csv' 

def bug_workflow(request):
    today = datetime.now().date()
    start_date = today - timedelta(31)
    bugs = BugWorkTime.objects.values('bug__title', 'time_spent_mins', 'timestamp', 'user__username').filter(timestamp__gte=start_date, timestamp__lt=today)
    
    with open(data_file, 'wb') as csv_file:
        write_csv(bugs, csv_file)