from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from multiselectfield import MultiSelectField
from django.urls import reverse



class Post(models.Model):
    movie= models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    release_date=models.DateTimeField(blank=True,null=True)
    show_date=models.DateTimeField()
    cost=models.IntegerField()
    no_tickets=[
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
    ]
    tickets=models.CharField(max_length=10,choices=no_tickets,default='two')
    seatNo=models.CharField(max_length=100)
    theater=models.CharField(max_length=100)
    district_choice=[
        ('adilabad','Adilabad'),
        ('kothagudem','Kothagudem'),
        ('hyderabad','Hyderabad'),
        ('jagitial','Jagitial'),
        ('bhupalpalle','Bhupalpalle'),
        ('gadwal','Gadwal'),
        ('kamareddy','Kamareddy'),
        ('karimnagar','Karimnagar'),
        ('khammam','Khammam'),
        ('komaram bheem','Komaram Bheem'),
        ('mahabubabad','Mahabubabad'),
        ('mahabubnagar','Mahabubnagar'),
        ('mancherial','Mancherial'),
        ('medak','Medak'),
        ('medchal','Medchal'),
        ('mulugu','Mulugu'),
        ('nagarkurnool','Nagarkurnool'),
        ('narayanpet','Narayanpet'),
        ('nalgonda','Nalgonda'),
        ('nirmal','Nirmal'),
        ('nizamabad','Nizamabad'),
        ('peddapalli','Peddapalli'),
        ('sircilla','Sircilla'),
        ('ranga Reddy','Ranga Reddy'),
        ('sangareddy','Sangareddy'),
        ('siddipet','Siddipet'),
        ('suryapet','Suryapet'),
        ('vikarabad','Vikarabad'),
        ('wanaparthy','Wanaparthy'),
        ('warangal','Warangal'),
        ('yadadri bhuvanagiri','Yadadri Bhuvanagiri'),  
    ]
    district=models.CharField(max_length=20,choices=district_choice,default='hyderabad')
    theater_location=models.TextField()
    cast=models.CharField(max_length=100)
    language_Choice=[
        ('Telugu','Telugu'),
        ('Hindi','Hindi'),
        ('English','English'),
        ('Malayalam','Malayalam'),
        ('kannada','kannada'),
    ]
    language=models.CharField(max_length=10, choices=language_Choice,default='Telugu')
    movie_Type=[
        ('2d','2D'),
        ('3d','3D'),
        ('imax2d','IMAX 2D'),
        ('imax3d','IMAX 3D'),
        ('4dx','4DX'),
        ('4dx3d','4DX 3D'),
        ('mx4d','MX4D'),

    ]
    movie_type=models.CharField(max_length=7, choices=movie_Type,default='2d')
    seller=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.movie

    def get_absolute_url(self):                                                #when new post is creeated it shows that specific post
        return reverse('post_detail' ,kwargs={'pk': self.pk})
