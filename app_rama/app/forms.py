from django import forms
from .models import PolishCV

class PLFormCV(forms.ModelForm):
    class Meta:
        model = PolishCV
        fields = ( 'sex',
                   'name',
                   'surname',
                   'city',
                   'street',
                   'zip_code',
                   'phone_number',
                   'e_mail',
                   'massage_skills',
                   'cv',
                   'photo_1',
                   'photo_2',
                   'photo_3',
                   # start change
                   'privacy_policy',
                   'work_experience_in_year',
                   'classic_massage',
                   'relaks_massage',
                   'sport_massage',
                   'taj_massage',
                   'checolate_massage',
                   'limfatic_massage',
                   )
        labels = {
            'sex': 'Wybierz prawidłową formę:',
            'name': 'Poda imie:',
            'surname': 'Podaj nazwisko:',
            'city': 'Miasto zamieszkania:',
            'street': 'Ulica i numer domu:',
            'zip_code': 'Kod pocztowy:',
            'phone_number': 'Numer telefonu:',
            'e_mail': 'Adres e-mail:',
            'work_experience_in_year':'Podaj ile masz lat doświadczenia na stanowisku masażysty',
            'classic_massage': 'Znajomość technik masażu klasycznego:',
            'relaks_massage': 'Znajomość technik masażu relaksacyjnego:',
            'sport_massage': 'Znajomość technik masażu sportowego:',
            'taj_massage': 'Znajomość technik masażu tajskiego:',
            'checolate_massage': 'Znajomość technik masażu z użyciem czekolady:',
            'limfatic_massage': 'Znajomość technik masażu odchudzającego:',
            'massage_skills': 'Podaj, jakie znasz dodatkowe techniki masażu (np. masaż gorącymi kamieniami itp.):',
            'cv': 'Dodaj swoje CV (pole opcjonalne):',
            'photo_1': '',
            'photo_2': '',
            'photo_3': '',
            'privacy_policy': 'Akceptuje regulamin portalu'
        }