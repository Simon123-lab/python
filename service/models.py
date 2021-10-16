from django.contrib.admin.filters import EmptyFieldListFilter
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from embed_video.fields import EmbedVideoField

# Create your models here.
class User(AbstractUser):
    Is_worker = models.BooleanField('Is worker', default=False)
    Is_client = models.BooleanField('Is client', default=False)
    
choice_category = (
    ('Facebook Likes', 'Facebook Likes'),
    ('Facebook Follows', 'Facebook Follows'),
    ('Instagram Likes', 'Instagram Likes'),
    ('Instagram Follows', 'Instagram Follows'),
    ('Youtube Likes', 'Youtube Likes'),
    ('Youtube Views', 'Youtube Views')
)

choice_status = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('In Process', 'In Process'),
    ('Cancelled', 'Cancelled'),
    ('Completed', 'Completed')
)

choice_quantity = (
    ('50', '50'),
    ('100', '100'),
    ('300', '300'),
    ('500', '500'),
    ('700', '700'),
    ('1000', '1000')
)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(User,on_delete=models.CASCADE)
    url = models.URLField(max_length=250)
    category = models.CharField(max_length=20, choices=choice_category)
    quantity = models.CharField(max_length=20, choices=choice_quantity)
    id_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=20)
    img = models.ImageField(upload_to='transactions/%Y/%m/%d/')
    status = models.CharField(max_length=50, default='pending',choices=choice_status) 
    
    def amount(self):
        if(self.quantity != None):
            quantity = int(self.quantity)
            accValue = self.category
            if (accValue == "Youtube Views" or accValue == "Youtube Likes"):
                amount = quantity * 2
                return amount
                
            elif (accValue == "Facebook Likes" or accValue == "Facebook Follows"):
                amount = quantity * 1.20
                return amount
                
            elif (accValue == "Instagram Likes" or accValue == "Instagram Follows"):
                amount = quantity * 1.20
                return amount

choice_receipt = (
    ('VID101', 'VID101'),
    ('LIK101', 'LIK101'),
    ('FOL101', 'FOL101'),
)           
     
class AssignOrder(models.Model):
    assign_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    assign_at = models.DateTimeField(auto_now_add=True)
    reciept = models.CharField(max_length=30, choices=choice_receipt)
    video = EmbedVideoField(blank=True)
    url = models.URLField(max_length=500, blank=True)
    
    def link(self):
        if(self.reciept == "VID101"):
            vidUrl = self.video + "?&autoplay=1&mute=1"
            return vidUrl
        elif (self.reciept != "VID101"):
            old = EmptyFieldListFilter
            return old
    
    def __str__(self):
        return str(self.reciept)
    
choice_percent = (
    ('30%','30%'),
    ('50%','50%'),
    ('70%','70%'),
    ('90%','90%'),
)
    
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    details = models.CharField(max_length=120)
    rating = models.CharField(max_length=20, choices=choice_percent)
    
    def  __str__(self):
        return str(self.user_id)
    
class ContestEntries(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    whatsapp = models.ImageField(upload_to="whatsapp")
    facebook = models.ImageField(upload_to="facebook")
    twitter = models.ImageField(upload_to="twitter")
    
    def __str__(self):
        return str(self.user_name)
    
class FrequentlyAskQuestions(models.Model):
    faq_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=1000)
    
    def str(self):
        return str(self.question)
        
class UpdateWeeklyContest(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="contest")
    title = models.CharField(max_length=50)
    alert = models.CharField(max_length=100)
    detail = models.CharField(max_length=1000)
    
    def __str__(self):
        return str(self.title)
  
class RobotConfirmationViews(models.Model):
    con_id = models.AutoField(primary_key=True)
    champ_id = models.ForeignKey(User,on_delete=models.CASCADE)
    hero_task = models.ForeignKey(AssignOrder,on_delete=CASCADE)
    entry_code = models.CharField(max_length=50)
    submit_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.entry_code)


        
    

    
    
    
        

    
    