from django import forms


class FeedbackForm(forms.Form):
    fullName = forms.CharField(max_length=36, required=True ,label="Ваше ФИО", widget=forms.TextInput(attrs={'class': 'text_area_small'}))
    mail = forms.CharField(max_length=36, required=True , label="Ваша почта", widget=forms.TextInput(attrs={'class': 'text_area_small'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'text_area_large', 'maxlength': 3000, 'cols': 60, 'rows': 10}), required=True , label="Сообщение")

    

