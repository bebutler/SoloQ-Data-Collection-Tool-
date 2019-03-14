from django.db import models
import datetime

# Create your models here.
class DataForm(models.Model):
    your_name = models.CharField(max_length=30)
    champion = models.CharField(max_length=30, default = '')
    role = models.CharField(max_length=7)
    teammate_1 = models.CharField(max_length=30)
    teammate_2= models.CharField(max_length=30)
    teammate_3 = models.CharField(max_length=30)
    teammate_4 = models.CharField(max_length=30)
    outcome = models.CharField(max_length=4)
    mute = models.CharField(max_length=3)
    attitude_Score = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return 'Player was: ' + self.your_name + ' | ' + self.role + ' | ' + self.outcome




class Games(models.Model):
    builds = (
    ('STRD','Standard' ),
    ('MAG', 'Magic Resistance'),
    ('AD', 'Attack Damage'),
    ('RDM', 'Random'),
    ('HYD', 'Hybrid'),
    )

    promos = (
    ('PRO','Promoted'),
    ('F', 'Failed'),
        )
    yorn = (
    ('Y', 'Yes'),
    ('N', 'No'),
        )
    Outcome_Choices = (
    ('Win','Win' ),
    ('Loss', 'Lose'),
    )
    
    class Meta:
        verbose_name_plural = "Games"
    
    champ = models.CharField(max_length=30)
    build = models.CharField(max_length=50, choices=builds, help_text="What kind of build did you use?")
    outcome = models.CharField(max_length=30, choices=Outcome_Choices, help_text="Did you win or lose?")
    promotion_series = models.CharField(max_length=30,choices= yorn, help_text="Where you in a series or not? (Yes or No)")
    premoted = models.CharField(max_length=30, choices=yorn, default="" ,help_text="Were you premoted after this game?")
    demoted = models.CharField(max_length=30, choices=yorn, default="",help_text="Were you demoted after this game?")
    date = models.DateField(default="", help_text="Enter MM/DD/YYYY")

    def __str__(self):
        return "Your Champ was: " + self.champ + " | " + "Build was: " + self.build + " | Played on: "+ str(self.date)


class AddData(models.Model):
    class Meta:
        verbose_name_plural = "Player Data"
    positions = (
    ('TOP','Top' ),
    ('JNG', 'Jungle'),
    ('MID', 'Midlane'),
    ('ADC', 'Marksmen'),
    ('SUPP', 'Support'),
    )

    
    Outcome_Choices = (
    ('Win','Win' ),
    ('Loss', 'Lose'),
    )

    Mute_choices = (
    ('Y', 'Yes'),
    ('N', 'No'),
    )
    
    your_name = models.CharField(max_length=30, help_text="Enter your summoner name")
    champion = models.CharField(max_length=30, default = '', help_text="Enter your champion name")
    role = models.CharField(max_length=7, choices=positions, help_text="Select the position you played")
    teammate_1 = models.CharField(max_length=30, help_text="Enter your teammate's name")
    teammate_2= models.CharField(max_length=30, help_text="Enter your teammate's name")
    teammate_3 = models.CharField(max_length=30, help_text="Enter your teammate's name")
    teammate_4 = models.CharField(max_length=30, help_text="Enter your teammate's name")
    outcome = models.CharField(max_length=4, choices=Outcome_Choices, help_text="Did you win or lose?")
    mute = models.CharField(max_length=3, choices=Mute_choices, help_text="Did you mute anyone?")
    attitude_Score = models.IntegerField(help_text="Enter a number to represent how you feel right now. 0 is horrible, and 100 is fantastic")
    comments = models.TextField(help_text="Give a summary of the game, and why you won or lost.")

    def __str__(self):
        return 'Player was: ' + self.your_name + ' | ' + self.role + ' | ' + self.outcome

class FullBuild(models.Model):
    Rune_Choices = (
    ('Force','+10 Adaptive Force' ),
    ('AttkSpd', '+10% Attack Speed'),
    ('CDR', '+1-10% CDR'),
    )

    Rune_Choices2 = (
    ('Force','+10 Adaptive Force' ),
    ('Armor', '+5 Armor'),
    ('MR', '+6 Magic Resist'),
    )

    Rune_Choices3 = (
    ('HP','+15-90 Health' ),
    ('Armor', '+5 Armor'),
    ('MR', '+6 Magic Resist'),
    )
    Champion = models.CharField(max_length=30, default="")
    Rune_ID = models.CharField(max_length=50, help_text="Enter like: 'Champion Name Page' eg. Alistar Page or Fiora AD Page")
    primary = models.TextField(help_text="Enter the parts of your primary tree like this: 'Resolve: Aftershock, Font of Life...'")
    secondary = models.TextField(help_text="Enter the parts of your secondary tree like this: 'Sorcery: Summon Aery, Manaflow Band...'")
    stat1 = models.CharField(max_length=20, choices=Rune_Choices, help_text = "Offense")
    stat2 = models.CharField(max_length=20, choices=Rune_Choices2, help_text = "Flex")
    stat3 = models.CharField(max_length=20, choices=Rune_Choices3, help_text = "Defense")
    items = models.TextField(help_text="Enter the items you used")
    date = models.DateField(default="", help_text="Enter MM/DD/YYYY")
    


    def __str__(self):
        return self.Rune_ID + " | Stats: " + self.stat1 + ", " + self.stat2 + ", " + self.stat3 + " |"
        
