class Country:

    def __init__(self, name, area, population, official_language, capital_city):
        self.name = name
        self.area = area
        self.population = population
        self.official_language = official_language
        self.capital_city = capital_city


countries = [
Country("Poland", 312696, 37950802, "Polish", "Warsaw"),
Country("Germany", 357022, 83149300, "German", "Berlin"),
Country("France", 551695, 67081000, "French", "Paris"),
Country("Japan", 377975, 126010000, "Japanese", "Tokyo"),
Country("USA", 9629091, 331002651, "English", "Washington, D.C."),
]

for country in countries:
    print(country.name, country.area, country.population, country.official_language, country.capital_city)
