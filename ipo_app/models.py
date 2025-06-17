from django.db import models

class IPO(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('listed', 'Listed'),
    ]

    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/')
    price_band = models.CharField(max_length=100)
    open_date = models.DateField()
    close_date = models.DateField()
    issue_size = models.CharField(max_length=100)
    issue_type = models.CharField(max_length=100)
    listing_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    ipo_price = models.FloatField(null=True, blank=True)
    listing_price = models.FloatField(null=True, blank=True)
    current_market_price = models.FloatField(null=True, blank=True)
    rhp_pdf = models.FileField(upload_to='docs/', null=True, blank=True)
    drhp_pdf = models.FileField(upload_to='docs/', null=True, blank=True)

    def __str__(self):
        return self.company_name
