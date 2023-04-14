from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=50,verbose_name="Course Name")
    course_number=models.IntegerField( help_text="Course Number represents the Course ID",verbose_name="Course Number   ")
    def get_name_and_number(self):
        return "%s %s"%(self.course_name,self.course_number)