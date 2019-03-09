from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

class Masseur(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    basic_photo = models.ImageField()
    back_profile_photo = models.ImageField(blank=True)
    work_time = models.CharField(max_length=3)
    description = models.TextField()
    ordinal_number = models.IntegerField()

    def __str__(self):
        return '%s - %s' %(self.name, self.surname)

    class Meta:
        ordering = ['ordinal_number']



class Img(models.Model):
    masseur = models.ForeignKey(Masseur, on_delete=models.CASCADE)
    img_file = models.ImageField()

    def __str__(self):
        return '%s - %s' %(self.masseur, self.id)



class MassageProduct(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    image = models.ImageField()
    number_ordering = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(6),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return '%s - pozycja: %s' %(self.name, self.number_ordering)

    class Meta:
        ordering = ['number_ordering']

class PostDetail(models.Model):
    title = models.CharField(max_length=150)
    img = models.ImageField()
    description = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["added_at"]

    def __str__(self):
        return self.title

class PolishCV(models.Model):
    CHOICES = (
        ('M', 'Pan'),
        ('W', 'Pani')
    )
    CHOICES_WORK_EXPERIENCE = (
        ('1', 'poniżej 1 roku'),
        ('1_2', 'od 1 roku do 2 lat'),
        ('2_4', 'od 2 do 4 lat'),
        ('4', 'powyżej 4 lat')
    )
    SKILLS = (
        ('1', 'nie znam'),
        ('2', 'znam podstawy'),
        ('3', 'poziom średnim'),
        ('4', 'poziom średnio-zaawansowanym'),
        ('5', 'poziom zaawansowanym')
    )
    sex = models.CharField(max_length=2, choices=CHOICES)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    e_mail = models.EmailField()
    cv =  models.FileField(upload_to='app/documents/', blank=True)
    photo_1 = models.ImageField()
    photo_2 = models.ImageField()
    photo_3 = models.ImageField()
    # zmiana start
    privacy_policy = models.BooleanField(default=False)
    work_experience_in_year = models.CharField(max_length=5, choices=CHOICES_WORK_EXPERIENCE, default=None)
    classic_massage = models.CharField(max_length=1, choices=SKILLS, default=None)
    relaks_massage = models.CharField(max_length=1, choices=SKILLS, default=None)
    sport_massage = models.CharField(max_length=1, choices=SKILLS, default=None)
    taj_massage = models.CharField(max_length=1, choices=SKILLS, default=None)
    checolate_massage = models.CharField(max_length=1, choices=SKILLS, default=None)
    limfatic_massage = models.CharField(max_length=1, choices=SKILLS, default=None)
    massage_skills = models.TextField() #more maassage with now
    #zmiana koniec
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s %s' %(self.name, self.surname, self.id)

    class Meta:
        ordering = ["-added_at"]