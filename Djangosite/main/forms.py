from django import forms
#from captcha.fields import CaptchaField


class FeedbackForm(forms.Form):
    fullName = forms.CharField(max_length=36, required=True ,label="Ваше имя", widget=forms.TextInput(attrs={'type':'text', 'id':'form4Example1', 'class': 'form-control'}))
    mail = forms.EmailField(label="Ваша почта", widget=forms.TextInput(attrs={'type':'email', 'id':'form4Example2', 'class': 'form-control'}))
    #mail = forms.CharField(max_length=36, required=True , label="Ваша почта", widget=forms.TextInput(attrs={'class': 'text_area_small'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'id':'form4Example2', 'class': 'form-control', 'maxlength': 3000,'rows': 4}), required=True , label="Ваше сообщение")
    #captcha = CaptchaField(label="Капча")
    
    

