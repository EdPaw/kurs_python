import datetime as dat
import calendar as cal


class Clock:
    def act_time(self):
        current_time = dat.datetime.now().time()
        return current_time


class Calendar:
    def act_date(self):
        current_date = dat.date.today()
        return current_date

    def how_many_days_act_month(self):
        now = dat.datetime.now()
        year = now.year
        month = now.month
        #monthrange zwraca krotkę (pierwszy dzień tygodnia, liczba dni w miesiącu). Tu odwołujemy się do indeksu 1
        days = cal.monthrange(year, month)[1]
        return days

    def week_view(self):
        now = dat.datetime.now()
        year = now.year
        month = now.month
        #rozpakowanie krotki
        first_day, days_in_m = cal.monthrange(year, month)

        days_in_m = days_in_m

        days = []
        for i in range(1, days_in_m+1):
            days.append(i)

        weeks = []
        for i in range(0, days_in_m, 7):
            week = days[i:i + 7]
            weeks.append(week)

        formatted_weeks = []
        for week in weeks:
            formatted_week = ""
            for day in week:
                formatted_week += "{:^3}".format(day)
            formatted_weeks.append(formatted_week)

        return formatted_weeks


class ClockCalendar(Clock, Calendar):
    pass

    def act_date(self):
        return super().act_date()

    def how_many_days_act_month(self):
        return super().how_many_days_act_month()

    def week_view(self):
        return super().week_view()


def main():
    clocal = ClockCalendar()

    print("Current Date:", clocal.act_date())
    print("Current Time:", clocal.act_time())
    print("Days in Actual Month:", clocal.how_many_days_act_month())
    print("Week View:")
    weeks = clocal.week_view()
    for week in weeks:
        print(week)


if __name__ == '__main__':
    main()
