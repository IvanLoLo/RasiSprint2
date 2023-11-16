from django.db import models

class ContractFile(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    fileName = models.CharField(max_length=15)
    publicURI = models.CharField(max_length=255)
    def __str__(self):
        return f"ID: {self.auto_increment_id} Contract name: {self.fileName} - public uri: {self.publicURI}"

