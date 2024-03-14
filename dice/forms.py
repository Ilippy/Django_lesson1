from django import forms


class ChooseGameForm(forms.Form):
    GAME_CHOICES = (
        ('C', 'Coin'),
        ('D', 'Dice'),
        ('H', 'Hundred'),
    )
    game = forms.ChoiceField(choices=GAME_CHOICES)
    count = forms.IntegerField(max_value=100)
