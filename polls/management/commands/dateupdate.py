from django.core.management.base import BaseCommand
from django.db.models import F
from polls.models import Realsimulation
import pandas as pd
import sqlite3

class Command(BaseCommand):
  def handle(self, *args, **options):
    stock = Realsimulation.objects.order_by("-date")[:12]

    condition = {
        'date':stock[0].date,
    }
    datas = Realsimulation.objects.all().filter(**condition)
    datass = datas.objects.all().filter(close__gt=F('bb'))
    ma = datass.objects.all().filter(days150__gt=F('days200'))
    
    # データベースにデータを入れる
    con = sqlite3.connect("/Users/yoshimuramasato/Documents/django/jangotest_1/mysite/db.sqlite3")
    # ma = pd.DataFrame(ma,columns=['Date','Open','High','Low','Close','Volume','Currency','code','rsi','days50','days150','days200','weeks20','stdev','BB','id'])
    ma.to_sql('polls_realsimulationchoice',con,if_exists='replace',index=None)
    con.commit()
    con.close()