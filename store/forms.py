from django import forms
from wishlist.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rate','content']  