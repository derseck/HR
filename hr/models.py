from django.db import models

class Recruitment(models.Model):
    """  
    Recruitment applications are created in this model. 
    """

    dateOfRequest = models.DateField(
        verbose_name = 'Date of request',
        help_text= "Date of recruitment request"
    )
    numberOfVacancies = models.PositiveIntegerField(
        verbose_name = 'Number of vacancies',
        help_text="Number of vacancies available"
    )
    title = models.CharField(
        verbose_name = 'Title',
        max_length=250, 
        help_text="Name of vacancy" 
    )

    class Meta:
        verbose_name = 'Recruitment'
        verbose_name_plural = 'recruitments'

    def __str__(self):
        """Return title of recruitment"""
        return self.title