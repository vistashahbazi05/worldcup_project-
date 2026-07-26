import csv
import random

from team import Team
from group import Group
from knockout import KnockoutStage

# کلاس اصلی مدیریت شبیه‌سازی جام جهانی
class WorldCupSimulator :
    def __init__(self):
        self.teams = []
        self.groups =[]
        self.round_of_16 = None
        self.quarterfinals = None
        self.semifinals = None
        self.final = None
        self.champion = None

    # خواندن اطلاعات تیم‌ها از فایل CSV
    def load_teams_from_csv(self, filename):
        self.teams.clear()
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # خواندن اطلاعات هر تیم و ایجاد شیء Team
            for row in reader:
                team = Team(
                    row["name"],
                    int(row["attack"]),
                    int(row["defense"]),
                    int(row["rank"]))
                self.teams.append(team)
        print("Teams Loaded Successfully")

    def reset_all_stats(self) :
        for team in self.teams :
            team.reset_stats()

    # تشکیل گروه‌ها بر اساس سیدبندی تیم‌ها
    def draw_groups_seed(self):

        self.groups = []

        group_names = ["A", "B", "C", "D", "E", "F", "G", "H"]

        for name in group_names:
            self.groups.append(Group(name))

        teams = sorted(self.teams, key=lambda x: x.rank)

        # تقسیم تیم‌ها به چهار سید
        pot1 = teams[0:8]
        pot2 = teams[8:16]
        pot3 = teams[16:24]
        pot4 = teams[24:32]

        # به هم زدن ترتیب تیم‌های هر سید
        random.shuffle(pot1)
        random.shuffle(pot2)
        random.shuffle(pot3)
        random.shuffle(pot4)

        # اختصاص یک تیم از هر سید به هر گروه
        for i in range(8):
            self.groups[i].add_team(pot1[i])
            self.groups[i].add_team(pot2[i])
            self.groups[i].add_team(pot3[i])
            self.groups[i].add_team(pot4[i])
        print("Groups Created Successfully")

    # نمایش تیم‌های هر گروه
    def display_groups(self):
        for group in self.groups:
            print()
            print("===== Group", group.name, "=====")
            for team in group.teams:
                print(team.name)

    # اجرای مسابقات مرحله گروهی
    def run_group_stage(self):
        for group in self.groups:
            group.play_all_matches()
            group.display_table()

    # انتخاب تیم‌های صعودکننده از هر گروه
    def get_qualified_teams(self):
        qualified = []
        for group in self.groups:
            first, second = group.advance_teams()
            qualified.append(first)
            qualified.append(second)
        return qualified

    # تشکیل جدول مسابقات مرحله حذفی
    def setup_knockout_bracket(self):
        first = {}
        second = {}
        for group in self.groups:
            a, b = group.advance_teams()
            first[group.name] = a

            second[group.name] = b

        self.round_of_16 = KnockoutStage("Round Of 16")

        self.round_of_16.add_match(first["A"], second["B"])
        self.round_of_16.add_match(first["C"], second["D"])
        self.round_of_16.add_match(first["E"], second["F"])
        self.round_of_16.add_match(first["G"], second["H"])

        self.round_of_16.add_match(first["B"], second["A"])
        self.round_of_16.add_match(first["D"], second["C"])
        self.round_of_16.add_match(first["F"], second["E"])
        self.round_of_16.add_match(first["H"], second["G"])

    # اجرای تمام مراحل حذفی تا مشخص شدن قهرمان
    def run_knockout_stage(self):

        # Round of 16
        self.round_of_16.play_round()
        self.round_of_16.display_results()

        winners = self.round_of_16.get_winners()

        # Quarterfinals
        self.quarterfinals = KnockoutStage("Quarterfinals")

        for i in range(0, len(winners), 2):
            self.quarterfinals.add_match(winners[i], winners[i + 1])

        self.quarterfinals.play_round()
        self.quarterfinals.display_results()

        winners = self.quarterfinals.get_winners()

        # Semifinals
        self.semifinals = KnockoutStage("Semifinals")

        for i in range(0, len(winners), 2):
            self.semifinals.add_match(winners[i], winners[i + 1])

        self.semifinals.play_round()
        self.semifinals.display_results()

        winners = self.semifinals.get_winners()

        # Final
        self.final = KnockoutStage("Final")

        self.final.add_match(winners[0], winners[1])

        self.final.play_round()
        self.final.display_results()

        self.champion = self.final.get_winners()[0]

        print()
        print("Champion:", self.champion.name)

    # اجرای کامل شبیه‌سازی جام جهانی
    def full_simulation(self):

        self.reset_all_stats()

        self.draw_groups_seed()

        self.run_group_stage()

        self.setup_knockout_bracket()

        self.run_knockout_stage()

        return self.champion

    # اجرای چندباره مسابقات برای محاسبه احتمال قهرمانی تیم‌ها
    def most_likely_champion(self, simulations=1000):

        champions = {}

        for team in self.teams:
            champions[team.name] = 0

        # اجرای شبیه‌سازی به تعداد دفعات درخواستی
        for _ in range(simulations):

            champion = self.full_simulation()

            champions[champion.name] += 1

        print()

        print("Champion Percentages")

        for team, count in sorted(
                champions.items(),
                key=lambda x: x[1],
                reverse=True):

            print(team, ":", round(count * 100 / simulations, 2), "%")

    # نمایش نتایج تمام مراحل حذفی
    def display_bracket(self):

        if self.round_of_16:

            self.round_of_16.display_results()

        if self.quarterfinals:

            self.quarterfinals.display_results()

        if self.semifinals:

            self.semifinals.display_results()

        if self.final:

            self.final.display_results()
