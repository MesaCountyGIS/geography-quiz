from django.db import models
import datetime

class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField()

    def save(self, *args, **kwargs):
        self.pub_date = datetime.date.today()
        super(Questions, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.question_text

    class Meta:
        verbose_name_plural = "questions"

class Answers(models.Model):
    question = models.ForeignKey(Questions)
    choice_text = models.CharField(max_length=200)
    correct_choice = models.CharField(max_length=1)
    explanation = models.CharField(max_length=500, blank=True)
    url = models.URLField(max_length=200, blank=True)

    def __unicode__(self):
        return self.choice_text

    class Meta:
        verbose_name_plural = "answers"
