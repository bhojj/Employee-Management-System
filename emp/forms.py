from django import forms


class FeedbackForm(forms.Form):
    email=forms.EmailField(label="Enter your email",max_length=100)
    name=forms.CharField(label="Enter your name",max_length=100)
    feedback=forms.CharField(label="Your Feedback",widget=forms.Textarea)


def __init__(self, *args, **kwargs):
  form = super(FeedbackForm, self).__init__(*args, **kwargs)
  for visible in form.visible_fields():
    visible.field.widget.attrs['class'] = 'form-control'