from django import forms

from .models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = (
            'user',
            'content',
            'image'
        )

    def clean_content(self):
        content = self.cleaned_data.get('content')

        if len(content) > 30:
            raise forms.ValidationError("Content length is too long")

        return content

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        print(data)
        content = data.get('content')
        print(content)

        if content == "":
            content = None

        image = data.get("image", None)

        if content is None and image is None:
            raise forms.ValidationError('Content or image is required')
        return super().clean(*args, **kwargs)

