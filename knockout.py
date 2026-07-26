from match import Match
# کلاس مدیریت مسابقات مرحله حذفی
class KnockoutStage :
    def __init__(self , round_name):
        self.round_name = round_name
        self.matches = []

    # اضافه کردن یک مسابقه به مرحله حذفی
    def add_match(self , team1 , team2) :
        match = Match(team1 , team2 , True)
        self.matches.append(match)

    # اجرای تمام مسابقات این مرحله
    def play_round(self) :
        for match in self.matches :
            match.play()

    # جمع‌آوری تیم‌های برنده برای صعود به مرحله بعد
    def get_winners(self) :
        winners = []
        for match in self.matches :
            winners.append(match.winner)
        return winners

    # نمایش نتایج مسابقات این مرحله
    def display_results(self) :
        print()
        print("======" , self.round_name , "======" )

        for match in self.matches :
            print(match.team1.name , match.goals1 , "-" , match.goals2 , match.team2.name , "Winner :" , match.winner.name)
