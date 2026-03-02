import random


from shared import COUNTRIES_LST


from app.datatypes import AvgGDP


def create_random_avg_gdp():
	return AvgGDP(
		country=random.choice(
			COUNTRIES_LST
		),
		avg_gdp=(
			random.random()
			+ random.randint(1567, 30000)
		)
	)


def iter_random_avg_gdp(num):
	for _ in range(num):
		yield create_random_avg_gdp()
