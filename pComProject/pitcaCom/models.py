from django.db import models

# 평촌아이티 컴퓨터 모델 생성
class PitcaCom(models.Model):
    pc_name = models.CharField(max_length=50)
    pc_ip = models.CharField(max_length=50)
    pc_cpu = models.CharField(max_length=100)
    pc_ram = models.IntegerField(default=0)
    pc_storage = models.CharField(max_length=50)
    pc_hdmi = models.BooleanField(default=False)

    def __str__(self):
        return self.pc_name