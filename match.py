import random
import numpy as np
from team import Team

# کلاس مربوط به مدیریت یک مسابقه بین دو تیم
class Match :

    def __init__(self , team1 , team2 , is_knockout=False):
        self.team1 = team1
        self.team2 = team2
        self.goals1 = 0
        self.goals2 = 0
        self.is_knockout = is_knockout
        self.winner = None
    # اجرای مسابقه و به‌روزرسانی آمار تیم‌ها
    def play(self) :

        self.goals1 , self.goals2 , self.winner = self.team1.simulate_match(self.team2 , self.is_knockout)
        self.team1.for_goals += self.goals1
        self.team1.against_goals += self.goals2
        self.team2.for_goals += self.goals2
        self.team2.against_goals += self.goals1

        # اختصاص امتیاز در مرحله گروهی
        if not self.is_knockout :
            if self.goals1 > self.goals2 :
                self.team1.points += 3
            elif self.goals2 > self.goals1 :
                self.team2.points += 3
            else :
                self.team1.points += 1
                self.team2.points += 1

        return self.winner