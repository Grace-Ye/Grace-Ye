"""
this task used to produce plots to show the speed of daily cases increasing trend
and i think the most of results match the predictions because the number of days is large,
which means we can track for a long time. if the number of days is small and simple size
is small, the results are often not match prediction.
"""
"""
the input number type is only number!
"""

from a2_28049918_task2 import *
import matplotlib.pyplot as plt


def visual_curve(days, meeting_probability, patient_zero_health):
    day_list = []
    for day in range(1, days + 1):
        day_list.append(day)
    daily_list = run_simulation(days, meeting_probability, patient_zero_health)

    plt.plot(day_list, daily_list)
    plt.title('Virus Spreading Curve in ' + str(days) + " days")
    plt.xlabel("no. of days")
    plt.ylabel("no. of daily cases")
    plt.show()


if __name__ == '__main__':
    days = int(input("Enter days number: "))
    probability = float(input("Enter probability number: "))
    zero_health = int(input("Enter zero health number: "))
    visual_curve(days, probability, zero_health)
