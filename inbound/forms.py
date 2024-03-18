from django import forms


class CSVUploadForm(forms.Form):
    file = forms.FileField(label="Select a CSV file")

    def clean_file(self):
        file = self.cleaned_data.get("file")
        if not file.name.endswith(".csv"):
            raise forms.ValidationError("Please upload a CSV file")
        return file
