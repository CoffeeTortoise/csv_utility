from collections import namedtuple


CountryData = namedtuple(
	'CountryData',
	[
		'country', 'year', 'gdp',
		'gdp_growth', 'inflation',
		'unemployment', 'population',
		'continent'
	]
)

AvgGDP = namedtuple(
	'AvgGDP',
	[
		'country',
		'avg_gdp'
	]
)
