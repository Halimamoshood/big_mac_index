from flask import render_template
import nasdaqdatalink

nasdaqdatalink.ApiConfig.api_key = "d1CBfhYCC9SWQKy2_LyX"

def get_country_data():

    eur_data = nasdaqdatalink.get("ECONOMIST/BIGMAC_EUR", start_date="2022-01-31", end_date="2022-01-31")
    dnk_data = nasdaqdatalink.get("ECONOMIST/BIGMAC_DNK", start_date="2022-01-31", end_date="2022-01-31")
    pol_data = nasdaqdatalink.get("ECONOMIST/BIGMAC_POL", start_date="2022-01-31", end_date="2022-01-31")

    eur_ham_price = eur_data['local_price'].values[0]
    dnk_ham_price = dnk_data['local_price'].values[0]
    pol_ham_price = pol_data['local_price'].values[0]

    ham_prices = {'EUR': eur_ham_price, 'DNK': dnk_ham_price, 'POL': pol_ham_price}

    return render_template('index.html', BMI=ham_prices)