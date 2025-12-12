import csv
import requests
import datetime
from io import StringIO

def fetch_prediction(
	launch_position: dict[str, float],
	launch_altitude: float,
	ascent_rate: float,
	burst_altitude: float,
	descent_rate: float,
	use_current_time: bool
) -> list[dict]:
	"""
	Fetch a flight prediction from the SondeHub Tawhiri API and return the CSV
	data as a list of dictionaries.

	Parameters:
	    launch_position (dict[str, float]): Launch position as {"lat": float, "lon": float}.
	    launch_altitude (float): Launch altitude (m)
	    ascent_rate (float): Ascent rate (ms⁻¹)
	    burst_altitude (float): Burst altitude (m)
	    descent_rate (float): Descent rate (ms⁻¹)
	    use_current_time (bool): If true, uses the current time for launch. If false, uses a default of 12:00 am

	Returns:
	     Prediction results as list[dict]
	"""
	if use_current_time:
		launch_time = datetime.datetime.now()
	else:
		launch_time = datetime.datetime.now().replace(hour=12, minute=0, second=0, microsecond=0)
	params = {
		"profile": "standard_profile",
		"pred_type": "single",
		"launch_datetime": launch_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
		"launch_latitude": launch_position["lat"],
		"launch_longitude": launch_position["lon"],
		"launch_altitude": launch_altitude,
		"ascent_rate": ascent_rate,
		"burst_altitude": burst_altitude,
		"descent_rate": descent_rate,
		"format": "csv",
	}
	response = requests.get("https://api.v2.sondehub.org/tawhiri", params=params)
	response.raise_for_status()
	return list(csv.DictReader(StringIO(response.text)))

def save_prediction(prediction: list[dict]) -> None:
	raise NotImplementedError()
	# To add in excel handling later once fully complete.

def main():
	# Default values
		# launch_position = {"lat":54.66864, "lon":356.6498}    Cockermouth school astro coordinates
		# launch_altitude = 81.0                                Altitude on the astro
		# ascent_rate = 6.0
		# burst_altitude = 35000                                Based on kaymont balloon's specs
		# descent_rate = 6.0
		# use_current_time = False                              Calculates for 12:00am on current day
	data = fetch_prediction(
		{"lat":54.66864, "lon":356.6498},
		81.0,
		6.0,
		30000,
		6.0,
		False
	)
	save_prediction(data)

if __name__ == "__main__":
	main()
