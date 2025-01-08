import requests
from bs4 import BeautifulSoup

def get_medicament_leaflet(medicament_name:str)->str:
    # Base URL for the CIMA API
    BASE_URL = "https://cima.aemps.es/cima"

    try:
        # Step 1: Search for medicament matching the name
        search_url = f"{BASE_URL}/rest/medicamentos"
        response = requests.get(search_url, params={"nombre": medicament_name})

        if response.status_code != 200:
            return f"Error: Unable to fetch medicament. Status code {response.status_code}"

        medicament = response.json()

        if not medicament:
            return f"No medicament found for '{medicament_name}'."

        # Step 2: Take the first matching medicament and get its registration number
        first_medicament = medicament["resultados"][0]
        registration_number = first_medicament.get("nregistro")

        if not registration_number:
            return f"No registration number found for the medicament '{medicament_name}'."

        # Step 3: Fetch the leaflet (prospectus) using the registration number
        leaflet_url = f"{BASE_URL}/dochtml/p/{registration_number}/P_{registration_number}.html"
        leaflet_response = requests.get(leaflet_url)

        if leaflet_response.status_code != 200:
            return f"Error: Unable to fetch leaflet. Status code {leaflet_response.status_code}"

        # Parse the HTML content of the leaflet
        soup = BeautifulSoup(leaflet_response.text, "html.parser")
        leaflet_text = soup.get_text(strip=True)  # Extract only the text content

        return leaflet_text

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage:
if __name__ == "__main__":
    medicament_name = "enantyum"
    leaflet = get_medicament_leaflet(medicament_name)
    print(leaflet)

