
from django.forms import ModelForm
from .models import News

class NewsForm(ModelForm):
    class Meta:
        model = News
