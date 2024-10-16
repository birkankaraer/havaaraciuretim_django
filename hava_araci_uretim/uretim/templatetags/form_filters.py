from django import template

# Django template tag kütüphanesini kaydediyoruz
register = template.Library()

# 'add_class' adında bir filter tanımlıyoruz. Bu filter, bir form alanına ek CSS sınıfları eklememizi sağlar.
@register.filter(name='add_class')
def add_class(value, css_class):
    # 'as_widget' metodu kullanılarak, mevcut form widget'ına yeni bir CSS sınıfı eklenir
    return value.as_widget(attrs={'class': css_class})
