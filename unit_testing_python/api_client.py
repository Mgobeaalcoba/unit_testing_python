import requests


def get_location(ip):
    response = requests.get(f'https://freeipapi.com/api/json/{ip}')
    data = response.json()
    return data['ipAddress'], data['countryName'], data['regionName'], data['cityName'], data['zipCode']


if __name__ == '__main__':
    ip = input('Enter the IP address: ') or '8.8.8.8'
    ip_data = get_location(ip)
    print(ip_data)

