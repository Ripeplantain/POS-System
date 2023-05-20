from django.forms import ModelForm
from .models import Order, Departments



class DepartmentForm(ModelForm):

    class Meta:
        model = Departments
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-3'


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ['quantity','department']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-3'