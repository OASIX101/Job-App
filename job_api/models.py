from django.db import models
from django.forms import model_to_dict

class JobAdvert(models.Model):
    EMPLOYMENT_CHOICES = (
                    ("full-time", "Full Time"),
                    ("contract", "Contract"),
                    ("remote","Remote"),
                    ("part-time", "Part Time"),
                )
    
    EMPLOYMENT_LEVELS = ( 
                    ("entry-level","Entry level"), 
                    ("mid-level","Mid-level"), 
                    ("senior","Senior")
                )
    
    STATUS_CHOICE = (
            ("available","Available"), 
            ("unavailable","Unavailable"), 
        )
    

    job_name = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    employment_type = models.CharField(max_length=250, choices=EMPLOYMENT_CHOICES, default='full-time')
    employment_level = models.CharField(max_length=250, choices=EMPLOYMENT_LEVELS, default='entry-level')
    location = models.CharField(max_length=250)
    job_description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default="unavailable")
    date_added = models.DateTimeField(auto_now=True)

    @property
    def Job_applicants_count(self):
        return self.applicants.all().values().count()
    
    def __str__(self):
        return f"{self.job_name}"
    
class JobApplication(models.Model):
    
    EXPERIENCE_LEVELS = (("0 - 1", "0 - 1"), 
                         ("1 - 2", "1 - 2"), 
                         ("3 - 4", "3 - 4"),
                         ("5 - 6", "5 - 6"), 
                         ("7 and above", "7 and above")
                        )
    
    
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length = 50)
    linkedin = models.URLField()
    github = models.URLField()
    website = models.URLField(blank=True, null=True)
    years_of_experience = models.CharField(max_length=50, choices=EXPERIENCE_LEVELS, default="0 - 1")
    cover_letter = models.TextField(blank=True, null=True)
    job_advert = models.ForeignKey(JobAdvert, related_name="applicants", on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    @property
    def Job(self):
        return model_to_dict(self.job_advert, fields=['job_name'])

    def __str__(self):
        return f"Application for --- {self.job_advert}"