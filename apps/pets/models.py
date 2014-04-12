from django.db import models

PET_KIND = (
    ('dog', 'Dog'),
    ('Cat', 'Cat'),
    ('Lion', 'Lion')
)

class Pet(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    kind = models.CharField(max_length=10, choices=PET_KIND)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

class News(models.Model):
    pet = models.ForeignKey('Pet', related_name='news')
    title = models.CharField(max_length=150)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
