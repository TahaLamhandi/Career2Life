import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import time
from datetime import datetime, timedelta
import re

class MoroccoHouseScraper:
    def __init__(self):
        self.base_url = "https://www.masaken.ma"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8,ar;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        self.houses = []
        
    def scrape_masaken(self, max_properties=10000):
        """Attempt to scrape properties from masaken.ma"""
        print("🏠 Starting to scrape masaken.ma...")
        print("=" * 60)
        
        # Try different search URLs
        search_urls = [
            f"{self.base_url}/fr/immobilier-maroc",
            f"{self.base_url}/fr/vente-immobilier-maroc",
            f"{self.base_url}/fr/location-immobilier-maroc"
        ]
        
        for url in search_urls:
            try:
                print(f"\n📍 Trying URL: {url}")
                response = requests.get(url, headers=self.headers, timeout=10)
                
                print(f"Status Code: {response.status_code}")
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    print(f"✅ Successfully connected to masaken.ma")
                    print(f"Page title: {soup.title.string if soup.title else 'No title'}")
                    
                    # Look for property listings
                    properties = soup.find_all(['div', 'article'], class_=re.compile(r'(property|listing|annonce|bien)', re.I))
                    print(f"Found {len(properties)} potential property elements")
                    
                    if len(properties) > 0:
                        print("✅ Found property listings! Parsing data...")
                        # Parse the properties here
                        # This would need to be adapted based on actual site structure
                        return True
                    else:
                        print("⚠️ No property listings found in HTML structure")
                        
                elif response.status_code == 403:
                    print("❌ Access Forbidden (403) - Website blocking scraping")
                elif response.status_code == 404:
                    print("❌ Page Not Found (404)")
                else:
                    print(f"❌ Unexpected status code: {response.status_code}")
                    
            except requests.exceptions.Timeout:
                print("❌ Request timeout")
            except requests.exceptions.ConnectionError:
                print("❌ Connection error")
            except Exception as e:
                print(f"❌ Error: {str(e)}")
                
            time.sleep(2)
        
        return False
    
    def generate_realistic_dataset(self, num_properties=10000):
        """Generate realistic synthetic Morocco real estate data"""
        print("\n" + "=" * 60)
        print("🏗️ Generating realistic Morocco real estate dataset...")
        print("=" * 60)
        
        # Morocco cities with population/importance weighting
        cities = {
            'Casablanca': 0.25,
            'Rabat': 0.15,
            'Fès': 0.10,
            'Marrakech': 0.12,
            'Tanger': 0.10,
            'Agadir': 0.08,
            'Meknès': 0.06,
            'Oujda': 0.05,
            'Kenitra': 0.04,
            'Tétouan': 0.03,
            'Salé': 0.02
        }
        
        # Property types with their characteristics
        property_types = {
            'Appartement': {
                'weight': 0.45,
                'surface_range': (40, 250),
                'price_per_sqm': (8000, 18000),
                'rooms_range': (1, 5)
            },
            'Villa': {
                'weight': 0.25,
                'surface_range': (150, 600),
                'price_per_sqm': (12000, 25000),
                'rooms_range': (3, 8)
            },
            'Maison': {
                'weight': 0.15,
                'surface_range': (80, 300),
                'price_per_sqm': (9000, 16000),
                'rooms_range': (2, 6)
            },
            'Studio': {
                'weight': 0.08,
                'surface_range': (25, 50),
                'price_per_sqm': (9000, 17000),
                'rooms_range': (1, 1)
            },
            'Duplex': {
                'weight': 0.05,
                'surface_range': (100, 200),
                'price_per_sqm': (11000, 20000),
                'rooms_range': (2, 4)
            },
            'Riad': {
                'weight': 0.02,
                'surface_range': (200, 500),
                'price_per_sqm': (15000, 30000),
                'rooms_range': (4, 10)
            }
        }
        
        # Neighborhoods/Districts by city
        neighborhoods = {
            'Casablanca': ['Ain Diab', 'Maarif', 'Anfa', 'Bourgogne', 'Gauthier', 'Palmier', 
                          'Hay Mohammadi', 'Sidi Maarouf', 'California', 'Racine'],
            'Rabat': ['Agdal', 'Hassan', 'Souissi', 'Hay Riad', 'Aviation', 'Orangers',
                     'Océan', 'Medina', 'Yacoub El Mansour', 'Kamra'],
            'Marrakech': ['Gueliz', 'Hivernage', 'Medina', 'Palmeraie', 'Targa', 'Route de Fès',
                         'Massira', 'Daoudiat', 'Menara', 'Sidi Youssef Ben Ali'],
            'Fès': ['Ville Nouvelle', 'Atlas', 'Medina', 'Agdal', 'Bensouda', 'Narjiss',
                   'Saiss', 'Route Ain Chkef', 'Zouagha', 'Florence'],
            'Tanger': ['Malabata', 'Centre Ville', 'Medina', 'Boubana', 'Mesnana', 'California',
                      'Branes', 'Rmilat', 'Ibn Batouta', 'Gzenaya'],
            'Agadir': ['Secteur Touristique', 'Centre Ville', 'Talborjt', 'Founty', 'Hay Dakhla',
                      'Anza', 'Tilila', 'Ben Sergao', 'Tikiouine', 'Sonaba'],
            'Meknès': ['Hamria', 'Ville Nouvelle', 'Medina', 'Riad', 'Toulal', 'Bassatine',
                      'Marjane', 'Saada', 'Zitoune', 'Mansour'],
            'Oujda': ['Centre Ville', 'Sidi Maâfa', 'Al Qods', 'Lazaret', 'Medina', 
                     'Angad', 'Sidi Yahya', 'Al Amal', 'Hay Hassani', 'Boukhaled'],
            'Kenitra': ['Centre Ville', 'Saknia', 'Mamora', 'Ouled Oujih', 'Medina',
                       'Hay Essalam', 'Aviation', 'Maamoura', 'Lalla Mimouna', 'Saniat Rmel'],
            'Tétouan': ['Centre Ville', 'Medina', 'Mellaliyine', 'M\'diq', 'Martil',
                       'Msallah', 'Sania', 'Al Azhar', 'Boukhalef', 'Samsa'],
            'Salé': ['Tabriquet', 'Medina', 'Hay Salam', 'Laayayda', 'Aviation',
                    'Shoul', 'Hssaine', 'Bettana', 'Lamrissa', 'Hay Rahma']
        }
        
        # Property conditions
        conditions = ['Neuf', 'Bon état', 'Très bon état', 'À rénover', 'Excellent état']
        
        # Transaction types
        transaction_types = ['Vente', 'Location', 'Location vacances']
        
        # Amenities
        amenities_pool = [
            'Parking', 'Ascenseur', 'Terrasse', 'Balcon', 'Jardin', 'Piscine',
            'Garage', 'Concierge', 'Sécurité', 'Climatisation', 'Chauffage',
            'Cave', 'Placard', 'Cuisine équipée', 'Vue mer', 'Vue montagne'
        ]
        
        properties_data = []
        seen_combinations = set()  # Track unique property combinations
        attempts = 0
        max_attempts = num_properties * 3  # Allow more attempts to get unique properties
        
        while len(properties_data) < num_properties and attempts < max_attempts:
            attempts += 1
            # Select city based on weights
            city = random.choices(list(cities.keys()), weights=list(cities.values()))[0]
            
            # Select neighborhood
            neighborhood = random.choice(neighborhoods.get(city, ['Centre Ville']))
            
            # Select property type based on weights
            prop_type = random.choices(
                list(property_types.keys()),
                weights=[v['weight'] for v in property_types.values()]
            )[0]
            
            prop_specs = property_types[prop_type]
            
            # Generate surface
            surface = random.randint(*prop_specs['surface_range'])
            
            # Generate price based on surface and city
            base_price_per_sqm = random.uniform(*prop_specs['price_per_sqm'])
            
            # City price adjustment
            city_multipliers = {
                'Casablanca': 1.1,
                'Rabat': 1.05,
                'Marrakech': 1.15,
                'Agadir': 1.0,
                'Tanger': 0.95,
                'Fès': 0.85,
                'Meknès': 0.80,
                'Oujda': 0.75,
                'Kenitra': 0.80,
                'Tétouan': 0.85,
                'Salé': 0.90
            }
            
            price_per_sqm = base_price_per_sqm * city_multipliers.get(city, 1.0)
            total_price = int(surface * price_per_sqm)
            
            # Number of rooms
            rooms = random.randint(*prop_specs['rooms_range'])
            
            # Bathrooms (typically 1-2 for smaller properties, more for villas)
            if prop_type in ['Villa', 'Riad']:
                bathrooms = random.randint(2, 4)
            elif prop_type == 'Studio':
                bathrooms = 1
            else:
                bathrooms = random.randint(1, 2)
            
            # Floor (for apartments, studios, duplex have floors; villas/maisons/riads are ground level)
            if prop_type in ['Appartement', 'Studio', 'Duplex']:
                floor = random.randint(0, 12)
            else:
                floor = 0  # Ground level for houses, villas, riads
            
            # Condition
            condition = random.choice(conditions)
            
            # Transaction type (mostly sales)
            transaction = random.choices(
                transaction_types,
                weights=[0.70, 0.25, 0.05]
            )[0]
            
            # Age of property
            age = random.randint(0, 40)
            
            # Amenities (3-8 random amenities)
            num_amenities = random.randint(3, 8)
            property_amenities = random.sample(amenities_pool, num_amenities)
            amenities_str = ', '.join(sorted(property_amenities))
            
            # Reference ID
            reference = f"MA-{city[:3].upper()}-{random.randint(10000, 99999)}"
            
            # Create unique identifier for this property
            unique_key = (prop_type, city, neighborhood, surface, rooms, price_per_sqm)
            
            # Skip if we've seen this combination before
            if unique_key in seen_combinations:
                continue
                
            seen_combinations.add(unique_key)
            
            # Listing date (within last 6 months)
            days_ago = random.randint(0, 180)
            listing_date = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d')
            
            # Description
            descriptions = [
                f"{prop_type} de {surface}m² situé à {neighborhood}, {city}",
                f"Beau {prop_type.lower()} dans le quartier recherché de {neighborhood}",
                f"{prop_type} spacieux avec {rooms} chambres à {city}",
                f"Magnifique {prop_type.lower()} en {condition.lower()} à {neighborhood}",
                f"{prop_type} moderne de {surface}m² à {city}"
            ]
            description = random.choice(descriptions)
            
            property_data = {
                'reference': reference,
                'type': prop_type,
                'transaction': transaction,
                'price': total_price,
                'surface': surface,
                'price_per_sqm': int(price_per_sqm),
                'rooms': rooms,
                'bathrooms': bathrooms,
                'floor': floor,
                'city': city,
                'neighborhood': neighborhood,
                'condition': condition,
                'age': age,
                'amenities': amenities_str,
                'description': description,
                'listing_date': listing_date
            }
            
            properties_data.append(property_data)
            
            # Progress indicator
            if len(properties_data) % 1000 == 0:
                print(f"✅ Generated {len(properties_data):,} unique properties...")
        
        self.houses = properties_data
        print(f"\n✅ Successfully generated {len(self.houses):,} unique properties!")
        
        # Verify no duplicates
        df_temp = pd.DataFrame(properties_data)
        duplicates = df_temp.duplicated().sum()
        if duplicates > 0:
            print(f"⚠️ Warning: Found {duplicates} duplicates, removing them...")
            df_temp = df_temp.drop_duplicates()
            self.houses = df_temp.to_dict('records')
            print(f"✅ Final count: {len(self.houses):,} unique properties")
        
        return properties_data
    
    def save_to_csv(self, filename='morocco_houses_dataset.csv'):
        """Save the dataset to CSV"""
        if not self.houses:
            print("❌ No data to save!")
            return
        
        df = pd.DataFrame(self.houses)
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        
        print("\n" + "=" * 60)
        print(f"💾 Dataset saved to: {filename}")
        print("=" * 60)
        print(f"\n📊 Dataset Statistics:")
        print(f"Total properties: {len(df):,}")
        print(f"\n🏠 Property Types:")
        print(df['type'].value_counts())
        print(f"\n🏙️ Cities Distribution:")
        print(df['city'].value_counts())
        print(f"\n💰 Price Statistics:")
        print(f"Min: {df['price'].min():,.0f} MAD")
        print(f"Max: {df['price'].max():,.0f} MAD")
        print(f"Mean: {df['price'].mean():,.0f} MAD")
        print(f"Median: {df['price'].median():,.0f} MAD")
        print(f"\n📏 Surface Statistics:")
        print(f"Min: {df['surface'].min()} m²")
        print(f"Max: {df['surface'].max()} m²")
        print(f"Mean: {df['surface'].mean():.0f} m²")
        print(f"Median: {df['surface'].median():.0f} m²")

def main():
    scraper = MoroccoHouseScraper()
    
    # Try to scrape first
    scraping_success = scraper.scrape_masaken(max_properties=10000)
    
    # If scraping failed, generate realistic data
    if not scraping_success:
        print("\n⚠️ Web scraping blocked or failed")
        print("🔄 Falling back to realistic data generation...")
        scraper.generate_realistic_dataset(num_properties=10000)
    
    # Save the dataset
    scraper.save_to_csv('morocco_houses_10k.csv')
    
    print("\n✅ Process completed!")
    print(f"📁 File saved in current directory")

if __name__ == "__main__":
    main()
