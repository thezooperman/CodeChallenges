from calculator import Calculator
import datetime


class MathOps:
	def __init__(self):
		self.calc = Calculator()

	def number_add(self, x, y):
		return self.calc.add(x, y)

	def date_add(self, date_from, days):
		if isinstance(date_from, datetime.date):
			return (date_from + datetime.timedelta(days=days)).strftime("%Y-%m-%d")


if __name__ == "__main__":
	obj = MathOps()
	print(obj.number_add(2, 3))
	print(obj.date_add(datetime.date(2020, 5, 21), 11))
