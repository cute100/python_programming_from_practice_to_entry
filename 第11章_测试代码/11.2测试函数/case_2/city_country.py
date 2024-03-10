def get_city_country(city,country,population=''):
    if population:
        citycountry=f"{city} {country}-population={population}"
    else:
        citycountry = f"{city} {country}"
    return citycountry.title()

