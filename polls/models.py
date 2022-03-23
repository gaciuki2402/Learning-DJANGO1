from django.db import models

<<<<<<< HEAD
class Question(models.Model):
     question_text=models.CharField(max_length=200)
     pub_date=models.DateTimeField("date published")

class Choice(models.Model):
     question=models.ForeignKey(Question, on_delete=models.CASCADE)
     choice_text=models.CharField(max_length=200)
     votes=models.IntegerField("date published")

        



=======
>>>>>>> c979997c2e55e1eea0d57b172d424e32f685934d
# Create your models here.
