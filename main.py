from application.salary import calculate_salary
from application.db.people import get_employees
import datetime

from miptlabs.plotter import pretty_plot, show
from numpy import linspace

# точки для построения графика
x = linspace(0, 5, 20)
y = x * x

pretty_plot(x, y)
show()

print(datetime.datetime.date(datetime.datetime.today()))

if __name__ == '__main__':
    calculate_salary()
    get_employees()
