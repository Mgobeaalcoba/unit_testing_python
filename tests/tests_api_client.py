import unittest
from unittest.mock import patch
from unit_testing_python.api_client import get_location


class ApiClientTests(unittest.TestCase):
    """
    The mock object is used to replace the real requests.get function.

    The patch function is used as a context manager to replace the real requests.get function.

    The patch function is used as a decorator to replace the real requests.get function.
    """

    def test_get_location(self):
        """
        Test the get_location function with real api calls.
        """
        ip_data = get_location('8.8.8.8')
        self.assertEqual(ip_data, ('8.8.8.8', 'United States of America', 'California', 'Mountain View', '94035'))

    def test_get_location_mocked(self):
        """
        Test the get_location function with patch used as a context manager.
        """
        with patch('requests.get') as mocked_get:
            mocked_get.return_value.json.return_value = {'ipVersion': 4, 'ipAddress': '8.8.8.8', 'latitude': 37.386051,
                                                         'longitude': -122.083847,
                                                         'countryName': 'United States of America', 'countryCode': 'US',
                                                         'timeZone': '-07:00', 'zipCode': '94035',
                                                         'cityName': 'Mountain View', 'regionName': 'California',
                                                         'isProxy': False, 'continent': 'Americas',
                                                         'continentCode': 'AM',
                                                         'currency': {'code': 'USD', 'name': 'US Dollar'},
                                                         'language': 'English',
                                                         'timeZones': ['America/Adak', 'America/Anchorage',
                                                                       'America/Boise', 'America/Chicago',
                                                                       'America/Denver', 'America/Detroit',
                                                                       'America/Indiana/Indianapolis',
                                                                       'America/Indiana/Knox',
                                                                       'America/Indiana/Marengo',
                                                                       'America/Indiana/Petersburg',
                                                                       'America/Indiana/Tell_City',
                                                                       'America/Indiana/Vevay',
                                                                       'America/Indiana/Vincennes',
                                                                       'America/Indiana/Winamac', 'America/Juneau',
                                                                       'America/Kentucky/Louisville',
                                                                       'America/Kentucky/Monticello',
                                                                       'America/Los_Angeles', 'America/Menominee',
                                                                       'America/Metlakatla', 'America/New_York',
                                                                       'America/Nome', 'America/North_Dakota/Beulah',
                                                                       'America/North_Dakota/Center',
                                                                       'America/North_Dakota/New_Salem',
                                                                       'America/Phoenix', 'America/Sitka',
                                                                       'America/Yakutat', 'Pacific/Honolulu'],
                                                         'tlds': ['.us']}
            ip_data = get_location('8.8.8.8')
            self.assertEqual(ip_data, ('8.8.8.8', 'United States of America', 'California', 'Mountain View', '94035'))
            # Validate that the url was called with the correct ip address
            mocked_get.assert_called_once()
            mocked_get.assert_called_with('https://freeipapi.com/api/json/8.8.8.8')

    @patch('unit_testing_python.api_client.requests.get')
    def test_get_location_mocked_2(self, mock_get):
        """
        Test the get_location function with patch used as a decorator.
        """
        mock_get.return_value.json.return_value = {'ipVersion': 4, 'ipAddress': '8.8.8.8', 'latitude': 37.386051,
                                                   'longitude': -122.083847, 'countryName': 'United States of America',
                                                   'countryCode': 'US', 'timeZone': '-07:00', 'zipCode': '94035',
                                                   'cityName': 'Mountain View', 'regionName': 'California',
                                                   'isProxy': False, 'continent': 'Americas', 'continentCode': 'AM',
                                                   'currency': {'code': 'USD', 'name': 'US Dollar'},
                                                   'language': 'English',
                                                   'timeZones': ['America/Adak', 'America/Anchorage', 'America/Boise',
                                                                 'America/Chicago', 'America/Denver', 'America/Detroit',
                                                                 'America/Indiana/Indianapolis', 'America/Indiana/Knox',
                                                                 'America/Indiana/Marengo',
                                                                 'America/Indiana/Petersburg',
                                                                 'America/Indiana/Tell_City', 'America/Indiana/Vevay',
                                                                 'America/Indiana/Vincennes', 'America/Indiana/Winamac',
                                                                 'America/Juneau', 'America/Kentucky/Louisville',
                                                                 'America/Kentucky/Monticello', 'America/Los_Angeles',
                                                                 'America/Menominee', 'America/Metlakatla',
                                                                 'America/New_York', 'America/Nome',
                                                                 'America/North_Dakota/Beulah',
                                                                 'America/North_Dakota/Center',
                                                                 'America/North_Dakota/New_Salem', 'America/Phoenix',
                                                                 'America/Sitka', 'America/Yakutat',
                                                                 'Pacific/Honolulu'], 'tlds': ['.us']}
        ip_data = get_location('8.8.8.8')
        self.assertEqual(ip_data, ('8.8.8.8', 'United States of America', 'California', 'Mountain View', '94035'))
        # Validate that the url was called with the correct ip address
        mock_get.assert_called_once()
        mock_get.assert_called_with('https://freeipapi.com/api/json/8.8.8.8')
