# vista shahbazi
# 404130873
# worldcup 2026 simulator

from simulator import WorldCupSimulator
def main():

    simulator = WorldCupSimulator()

    while True:

        print("\n===== World Cup 2026 Simulator =====")
        print("1. Load Teams")
        print("2. Draw Groups")
        print("3. Run Group Stage")
        print("4. Run Full Tournament")
        print("5. Simulate 1000 Times")
        print("6. Display Bracket")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":

            filename = input("CSV File Name: ")

            try:
                simulator.load_teams_from_csv(filename)
            except FileNotFoundError:
                print("File Not Found!")

        elif choice == "2":

            if len(simulator.teams) == 0:

                print("Load teams first.")

            else:

                simulator.draw_groups_seed()

                simulator.display_groups()

        elif choice == "3":

            if len(simulator.groups) == 0:

                print("Draw groups first.")

            else:

                simulator.run_group_stage()

        elif choice == "4":

            if len(simulator.teams) == 0:

                print("Load teams first.")

            else:

                simulator.full_simulation()

        elif choice == "5":

            if len(simulator.teams) == 0:

                print("Load teams first.")

            else:

                number = int(input("Number of Simulations: "))

                if number <= 0:

                    print("Invalid Number")

                else:

                    simulator.most_likely_champion(number)

        elif choice == "6":

            simulator.display_bracket()

        elif choice == "7":

            print("Good Bye")

            break

        else:

            print("Invalid Choice")


if __name__ == "__main__":

    main()
