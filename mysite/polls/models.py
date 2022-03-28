from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    class Meta:
        #overiding the name of the table from 'appname_model'
        db_table = 'questions'

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    class Meta:
        #overiding the name of the table from 'appname_model'
        db_table = 'choices'

        
        def __str__(self):
            return self.choice_text

