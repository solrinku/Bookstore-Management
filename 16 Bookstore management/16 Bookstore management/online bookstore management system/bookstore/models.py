from django.db import models
from django.contrib.auth.models import User
class Book(models.Model):
    title = models.TextField()
    author_name=models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image=models.ImageField(upload_to='Books/')
    pdf=models.FileField(upload_to='pdfs/')
    def __str__(self):
        return self.title
class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.user.username
        