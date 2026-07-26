from match import Match
import random

# کلاس مدیریت گروه‌های مسابقات
class Group :
    def __init__(self , name):
        self.name = name
        self.teams = []

    # اضافه کردن یک تیم به گروه
    def add_team(self , team):
        team.group = self.name
        self.teams.append(team)

    # برگزاری تمام مسابقات بین تیم‌های گروه
    def play_all_matches(self) :

        # بررسی تمام حالت‌های مسابقه بین تیم‌های گروه
        for i in range(len(self.teams)) :
            for j in range(i + 1 , len(self.teams)) :
                match = Match(self.teams[i] , self.teams[j])
                match.play()

    # مرتب‌سازی تیم‌ها بر اساس امتیاز، تفاضل گل و گل زده
    def get_ranking(self) :
        ranking = sorted(self.teams , key = lambda team: ( team.points , team.goal_difference() , team.for_goals , random.random())
 , reverse=True)
        return ranking

    # انتخاب دو تیم برتر گروه
    def advance_teams(self) :
        ranking = self.get_ranking()
        return ranking[0] , ranking[1]

    # نمایش جدول گروه
    def display_table(self) :
        print()
        print("===== Group" , self.name , "=====")
        ranking = self.get_ranking()
        for i , team in enumerate(ranking) :
            print(i + 1 , team.name , "-" , team.points , "pts" , "GD" , team.goal_difference() , "GF" , team.for_goals)
