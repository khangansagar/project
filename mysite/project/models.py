from django.db import models

class Support(models.Model):
    Sup_id = models.AutoField(primary_key=True)
    Sup_name= models.CharField(max_length=100)
    Sup_email= models.EmailField(max_length=70, blank=True, null=True, unique=True)
    Sup_phone_india = models.IntegerField(default=0,null=True)
    Sup_phone_usa = models.IntegerField(default=0,null=True)
    Sup_DOJ = models.DateField()

class Consultant(models.Model):
    Con_id = models.AutoField(primary_key=True)
    Con_name= models.CharField(max_length=100)
    Con_email= models.EmailField(max_length=70, blank=True, null=True, unique=True)
    Con_phone = models.IntegerField(default=0,null=True)

class Project(models.Model):
    Proj_id = models.AutoField(primary_key=True)
    client = models.CharField(max_length=100)
    location  = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    technology = models.CharField(max_length=100)
    Sup_init_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    support = models.ForeignKey(Support)
    consultant = models.ForeignKey(Consultant)

class Support_Status(models.Model):
    project= models.ForeignKey(Project)
    Training = 'training'
    Active = 'active'
    Less_active='less active'
    Independent = 'independent'
    Terminated= 'terminated'
    Completed='completed'
    status_choice =(
        (Training, 'Training'),
        (Active, 'Active'),
        (Less_active, 'Less Active'),
        (Independent, 'Independent'),
        (Terminated , 'Terminated'),
        (Completed , 'Completed')
    )
    status = models.CharField(choices=status_choice,max_length=100,default='Training')
