import requests
import time
import json
from datetime import datetime
import logging

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def fetch_proxies():
    """Fetch proxies from the GeoNode API"""
    url = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        
        # Extract IPs from the response
        proxy_ips = [proxy['ip'] for proxy in data['data']]
        
        # Save IPs to file
        with open('proxy.txt', 'w') as f:
            f.write('\n'.join(proxy_ips))
        
        logging.info(f"Successfully saved {len(proxy_ips)} proxy IPs to proxy.txt")
        
    except requests.RequestException as e:
        logging.error(f"Error fetching proxies: {e}")
    except (KeyError, json.JSONDecodeError) as e:
        logging.error(f"Error parsing response: {e}")
    except IOError as e:
        logging.error(f"Error writing to file: {e}")

def main():
    logging.info("Starting proxy scraper...")
    
    while True:
        fetch_proxies()
        time.sleep(300)  # Wait for 5 minutes (300 seconds)

if __name__ == "__main__":
    main() 