import requests


def get_location(ip):
    response = requests.get(f'https://freeipapi.com/api/json/{ip}')
    data = response.json()
    return data['ipAddress'], data['countryName'], data['regionName'], data['cityName'], data['zipCode']


if __name__ == '__main__':
    ip = input("Enter an IP address: ") or '8.8.8.8'
    ip_address, country, region, city, zip_code = get_location(ip)
    print(f'IP Address: {ip_address}')
    print(f'Country: {country}')
    print(f'Region: {region}')
    print(f'City: {city}')
    print(f'Zip Code: {zip_code}')