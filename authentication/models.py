from django.db import models


class Info(models.Model):
  email=models.CharField(max_length=50, null=True, unique='true');
  comment=models.CharField(max_length=1000, null=True);
 
class review(models.Model):
  comment=models.CharField(max_length=1000,null=True,);
  type=models.IntegerField(null=True);
