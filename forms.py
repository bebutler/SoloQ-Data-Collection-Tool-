from django import forms
from django.http import HttpResponseRedirect
from .models import AddData,Games,FullBuild
#Define Choices for fields
##Rune_Choices = (
##    ('OFF','+10 Adaptive Force' ),
##    ('OFF', '+9% Attack Speed'),
##    ('OFF', '+1-10% CDR'),
##    )
##
##Rune_Choices2 = (
##    ('FLEX','+10 Adaptive Force' ),
##    ('FLEX', '+9% Attack Speed'),
##    ('FLEX', '+1-10% CDR'),
##    )
##
##Rune_Choices3 = (
##    ('DEF','+10 Adaptive Force' ),
##    ('DEF', '+9% Attack Speed'),
##    ('DEF', '+1-10% CDR'),
##    )

Outcome_Choices = (
    ('Win','Win' ),
    ('Loss', 'Lose'),
    )
Mute_choices = (
    ('Y', 'Yes'),
    ('N', 'No'),
    )

positions = (
    ('TOP','Top' ),
    ('JNG', 'Jungle'),
    ('MID', 'Midlane'),
    ('ADC', 'Marksmen'),
    ('SUPP', 'Support'),
    )



#Define Fields
class DataForm(forms.Form):
    your_name = forms.CharField(max_length=30,help_text="What is your Ingame name?")
    champion = forms.CharField(max_length=20, help_text="What champion did you play this game?")
    role = forms.ChoiceField(choices=positions,help_text="What role did you play in this game?")
    teammate_1 = forms.CharField(max_length=30,help_text="Enter a teammate's Ingame name here.")
    teammate_2= forms.CharField(max_length=30,help_text="Enter a teammate's Ingame name here.")
    teammate_3 = forms.CharField(max_length=30,help_text="Enter a teammate's Ingame name here.")
    teammate_4 = forms.CharField(max_length=30,help_text="Enter a teammate's Ingame name here.")
    outcome = forms.ChoiceField(choices=Outcome_Choices)
    mute = forms.ChoiceField(choices=Mute_choices, help_text="Did you mute anyone this game?")
    attitude_Score = forms.IntegerField(help_text="Enter a number between 0 and 100. 100 means you're feeling great, 0 means you're very angry/upset.")
    comments = forms.CharField(widget=forms.Textarea,help_text="How are you feeling after the game? Why'd you win or lose?")
    #date = forms.DateField(input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y'], help_text= "Enter in MM-DD-YYYY format")

class DataForm2(forms.ModelForm):
    class Meta:
        model = AddData
        fields = ["your_name", "champion", "role", "teammate_1", "teammate_2", "teammate_3", "teammate_4", "outcome", "mute", "attitude_Score","comments"]

class BuildForm(forms.ModelForm):
    class Meta:
        model = FullBuild
        fields = ["Champion","Rune_ID", "primary", "secondary", "stat1", "stat2", "stat3", "items", "date"]

class GamesForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = ["champ", "build", "outcome", "promotion_series", "premoted", "demoted", "date"]





