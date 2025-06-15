from django import forms
from .models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['content', 'study_time', 'concentration', 'memo']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': '何を勉強しましたか？ (例: 数学I P.10-15)'}),
            'concentration': forms.NumberInput(attrs={'type': 'range', 'min': '1', 'max': '10', 'class': 'form-range'}),
            'memo': forms.Textarea(attrs={'rows': 2, 'placeholder': '感想や次回の課題など'}),
        }
