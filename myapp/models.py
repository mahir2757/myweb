from django.db import models


class ProjectDetail(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.TextField()
    enno = models.IntegerField()
    div  = models.CharField(max_length=50)
    gno = models.IntegerField()
    pdetail = models.TextField()

    class Meta:
        db_table=("project details")

