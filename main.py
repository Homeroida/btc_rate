import requests
import sys

try:
    n = sys.argv[1]
    # conveer to float
    n = float(n)

    # sending requests for data
    response = requests.get(
        'https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()

    # formating json file
    rate = data['bpi']['USD']['rate']

    # conveer to float
    formated_rate = float(rate.replace(',', ''))

    result = formated_rate * n

    print(f'${result:,.4f}')

except ValueError:
    sys.exit('Command-line argument is not a number')

except IndexError:
    sys.exit('Missing command-line argument')
