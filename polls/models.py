from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  def __str__(self):
        return self.question_text
  def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
  question = models.ForeignKey(Question,on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  def __str__(self):
        return self.choice_text
# それぞれdjango.db.models.Modelのサブクラス
# charfield⇢文字のフィールド
# datetimefield⇢日時フィールド
# ForeignKey⇢外部キー
class Stock(models.Model):
      datetime=models.DateTimeField()

class  Realsimulation(models.Model):
      id = models.IntegerField(primary_key=True) 
      date = models.DateTimeField()
      open = models.FloatField(null=True,blank=True)
      high = models.FloatField(null=True,blank=True)
      low = models.FloatField(null=True,blank=True)
      close = models.FloatField(null=True,blank=True)
      volume = models.IntegerField(null=True,blank=True)
      currency = models.IntegerField(null=True,blank=True)
      code = models.CharField(max_length=255)
      rsi = models.FloatField(null=True,blank=True)
      days50 = models.FloatField(null=True,blank=True)
      days150 = models.FloatField(null=True,blank=True)
      days200 = models.FloatField(null=True,blank=True)
      weeks20 = models.FloatField(null=True,blank=True)
      stdev = models.FloatField(null=True,blank=True)
      bb = models.FloatField(null=True,blank=True)
      def __str__(self):
            return self.code

class  Realsimulationchoice(models.Model):
      id = models.IntegerField(primary_key=True) 
      date = models.DateTimeField()
      open = models.FloatField(null=True,blank=True)
      high = models.FloatField(null=True,blank=True)
      low = models.FloatField(null=True,blank=True)
      close = models.FloatField(null=True,blank=True)
      volume = models.IntegerField(null=True,blank=True)
      currency = models.IntegerField(null=True,blank=True)
      code = models.CharField(max_length=255)
      rsi = models.FloatField(null=True,blank=True)
      days50 = models.FloatField(null=True,blank=True)
      days150 = models.FloatField(null=True,blank=True)
      days200 = models.FloatField(null=True,blank=True)
      weeks20 = models.FloatField(null=True,blank=True)
      stdev = models.FloatField(null=True,blank=True)
      bb = models.FloatField(null=True,blank=True)
      def __str__(self):
            return self.code