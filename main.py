import requests


class Bored:
    def __init__(self) -> None:
        self.url = 'http://www.boredapi.com/api/'

    def get_activity(self) -> str:
        '''get activity from bored
        
        Returns:
            str: text of activity
        '''
        response = requests.get(self.url)
        data = response.json()
        return data

    def get_activity_by_type(self, type: str) -> dict:
        '''get activity by type

        Note:
            Type of the activity: ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]
        
        Args:
            type (str): type
        
        Returns:
            dict: activity data
        '''
        response = requests.get(f'{self.url}?type={activity_type}')
        data = response.json()
        return data

    def get_activity_by_id(self, key: int) -> dict:
        '''get activity by key

        Note:
            A unique numeric id: [1000000, ..., 9999999]
        
        Args:
            key (int): key
        
        Returns:
            dict: activity data
        '''
        response = requests.get(f'{self.url}/{activity_id}')
        data = response.json()
        return data

    def get_activity_by_accessibility(self, accessibility: float) -> dict:
        '''get activity by accessibility

        Note:
            A factor describing how possible an event is to do with zero being the most accessible
            [0.0, ..., 1.0]
        
        Args:
            accessibility (float): accessibility
        
        Returns:
            dict: activity data
        '''
        response = requests.get(f'{self.url}?accessibility={accessibility}')
        data = response.json()
        return data

    def get_activity_by_price(self, price: float) -> dict:
        '''get activity by price

        Note:
            A factor describing the cost of the event with zero being free
            [0, 1]
        
        Args:
            price (float): price
        
        Returns:
            dict: activity data
        '''
        response = requests.get(f'{self.url}?price={price}')
        data = response.json()
        return data

    def get_activity_by_price_range(self, minprice: float, maxprice: float) -> dict:
        '''get activity by price

        Note:
            A factor describing the cost of the event with zero being free
            [0, 1]
        
        Args:
            minprice (float): min price
            maxprice (float): max price
        
        Returns:
            dict: activity data
        '''
        response = requests.get(f'{self.url}?minprice={min_price}&maxprice={max_price}')
        data = response.json()
        return data
    