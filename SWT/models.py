from django.db import models

class Prj(models.Model):
    name = models.CharField(max_length=30, unique=True)
    dut_id = models.CharField(max_length=30)
    sku_id = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Version(models.Model):
    sw_build = models.CharField(max_length=100)
    sw_version = models.CharField(max_length=100)
    lastupdate = models.DateTimeField(null= True )
    prj = models.ForeignKey(Prj, related_name='version',on_delete=models.CASCADE)

    def prj_name(self):
        return self.prj.name
    class Meta:
        ordering = ['-lastupdate']


class Result(models.Model):
    type_id = models.CharField(max_length=30,null=True)
    test_description = models.CharField(max_length=30,null=True)
    case_pass_rate = models.CharField(max_length=30,null=True)
    running_time = models.CharField(max_length=30,null=True)
    result_url = models.CharField(max_length=70,null=True)
    content = models.TextField(max_length=4000,null=True)
    FC = models.CharField(max_length=30,null=True)
    version = models.ForeignKey(Version, related_name='result',on_delete=models.CASCADE)

    def sw_build(self):
        return self.version.sw_build
    def prj(self):
        return self.version.prj.name


