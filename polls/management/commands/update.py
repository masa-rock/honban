from django.core.management.base import BaseCommand
from polls.models import Realsimulation
import investpy
import pandas as pd
import datetime
import sqlite3

class Command(BaseCommand):
  def handle(self, *args,**options):
    def valuesdata(stock_df):
      stock_df["days50"] = stock_df["Close"].rolling(10).mean().round(1)
      stock_df["days150"] = stock_df["Close"].rolling(30).mean().round(1)
      stock_df["days200"] = stock_df["Close"].rolling(40).mean().round(1)
      stock_df["weeks20"] = stock_df["Close"].rolling(20).mean().round(1)
      stock_df["stdev"] = stock_df['Close'].rolling(20).std(ddof=0)
      stock_df['BB'] = stock_df['weeks20'] + stock_df['stdev']*2
      
      return stock_df
    # 指標にrsiを追加する
    def rsi(stock_df):
      rsi=[]
      dummy = 0
      for num in range(15):
        rsi.append(dummy)
      for i in range(16,len(stock_df)+1):
        down = 0
        up = 0
          for u in range(0,14):
              x = i-14+u
              difference = int(stock_df.iloc[x,4])-int(stock_df.iloc[x-1,4])
              if(difference >= 0):
                  up = up + difference
              else:
                  down = down + abs(difference)
          RSI = up *100 / (down + up)
          rsi.append(RSI)
        return rsi
    
    def get_brand(code):
        now = datetime.datetime.now()
        now = now.strftime('%d/%M/%Y')
        country = 'japan'
        interval = 'Weekly'
        from_date = '01/05/2020'
        to_date = 'now'
        stock = str(code)
        try:
            df = investpy.stocks.get_stock_historical_data(stock=stock, country=country, from_date=from_date,to_date=to_date, interval=interval)
            df = df.assign(code=code)
            rsi(df)
            df = df.assign(rsi=rsi(df))
            df =valuesdata(df)        
            df.reset_index(drop=False,inplace=True)
            
            print(code)
        except(RuntimeError,IndexError,ValueError):
            return None
        return df

    def brands_generator(code_range):
        #enumerateは、iが0,1,2,3,・・・codeがcode_rangeに従って循環される
        for i,code in enumerate(code_range):
            if i == 0:
            #cols = ['日付','始値','高値','安値','終値','出来高','国']
                df = pd.DataFrame(index=[])
            brand = get_brand(code)
            #concatはデータを結合する。（デフォルトでaxis=0のため縦方向に結合）
            if brand is not None:
                df = pd.concat([df,brand]).reset_index(drop=True)
        return df

    dfa = brands_generator(range(1300,9999))
    dfa['id'] = dfa.index
    # 最新のデータに並び替え
    dfb = df.sort_values(by=['Date'],ascending=False)
    # 最新の日にちを取得する
    dfc = dfb.Date[0]
    # 最新の日にちのデータを取得する
    dfd = dfb[dfb.Date == dfc]
    
    # データベースにデータを入れる
    con = sqlite3.connect("/mysite/db.sqlite3")
    df.to_sql('polls_realsimulation',con,if_exists='append',index=None)
    con.commit()
    con.close()
