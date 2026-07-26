
import random
import numpy as np

# کلاس مربوط به نگهداری اطلاعات و آمار هر تیم
class Team :



    def __init__(self , name , attack , defense , rank):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.rank = rank

        self.for_goals = 0
        self.against_goals = 0
        self.points = 0
        self.group = ""

    # محاسبه تفاضل گل تیم
    def goal_difference(self):
        return self.for_goals - self.against_goals

    def reset_stats(self):
        self.for_goals = 0
        self.against_goals = 0
        self.points = 0

    # شبیه‌سازی ضربات پنالتی در صورت مساوی بودن مسابقه
    def simulate_penalties(self , opponent):
        my_score = 0
        op_score = 0

        my_probability = 0.75 + (self.attack - opponent.defense) / 250
        op_probability = 0.75 + (opponent.attack - self.defense) / 250

        my_probability = max(0.6 , min(0.9 , my_probability))
        op_probability = max(0.6 , min(0.9 , op_probability))

        # اجرای پنج ضربه پنالتی برای هر تیم
        for _ in range(5) :
            if random.random() < my_probability :
                my_score += 1

            if random.random() < op_probability :
                op_score += 1

        # در صورت مساوی بودن، پنالتی‌ها تا مشخص شدن برنده ادامه پیدا می‌کند
        while my_score == op_score:

            if random.random() < my_probability :
                my_score += 1
            if random.random() < op_probability :
                op_score += 1

        if my_score > op_score :
            return self

        return opponent

    # شبیه‌سازی نتیجه یک مسابقه فوتبال
    def simulate_match( self, opponent , is_knockout=False):
    
        # محاسبه احتمال گلزنی هر تیم بر اساس قدرت حمله و دفاع
        lambda_self = (self.attack / 100) * 1.5 + (1 - opponent.defense / 100) * 0.8
        lambda_opponent = (opponent.attack / 100) * 1.5 + (1 - self.defense / 100) * 0.8
        goals_self = np.random.poisson(lambda_self)
        goals_opponent = np.random.poisson(lambda_opponent)
    
        # بررسی اینکه مسابقه در مرحله حذفی است یا خیر
        if is_knockout:
    
            # در صورت مساوی شدن بازی، وقت اضافه برگزار می‌شود
            if goals_self == goals_opponent:
                extra_self = np.random.poisson(lambda_self * 0.33)
                extra_op = np.random.poisson(lambda_opponent * 0.33)
                goals_self += extra_self
                goals_opponent += extra_op
    
                if goals_self == goals_opponent :
                    winner = self.simulate_penalties(opponent)
    
                elif goals_self > goals_opponent :
                    winner = self
    
                else :
                    winner = opponent
    
            elif goals_self > goals_opponent:
                winner = self
    
            else:
                winner = opponent

        else :
            winner = None
    
        return goals_self , goals_opponent , winner
    