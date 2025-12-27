# Flight Prediction

## Overview
This folder contains everything required to run and automate daily flight simulations.

- **`balloon_flight_prediction.py`** — Runs the flight simulations and collects the data.
- **`data.xlsx`** — A blank Excel template that the script writes simulation data to.
- **`flight_prediction_agent.plist`** — A macOS LaunchAgent used to automatically run the script on a daily schedule via `launchctl`.

---

## Script
The script retrieves and simulates flights for the following times on the day it is run:
- 12:00 pm
- 6:00 am
- 12:00 am
- 6:00 pm

### Simulation
- Simulations are run using the **Tawhiri API**.  
- Documentation can be found here:  
  https://tawhiri.readthedocs.io/en/latest/introduction.html

### Output
- All simulation results are written to **`data.xlsx`**, which must be located in the same directory as the script.

---

## Excel Spreadsheet Structure
- The Excel file contains **one sheet per day**.
- Each sheet is named using the format **`yyyy-mm-dd`**
- All simulations for that day are stored within the corresponding sheet.

---

## Daily Scheduling
I'm on macOS at home so the following applies for that operating system only.
The script is automated using **`launchctl`** and a **LaunchAgent**.

### Setup
- The LaunchAgent is defined in `flight_prediction_agent.plist`.
- This `.plist` file is placed in `~/Library/LaunchAgents`.
- The script runs automatically according to the schedule defined in the `.plist` file.

### Loading the Agent
Once the file is in the correct directory, the agent can be loaded, unloaded and any active LaunchAgents can be listeded by running the following command in Terminal:

```
launchctl load ~/Library/LaunchAgents/flight_prediction_agent.plist
launchctl load ~/Library/LaunchAgents/flight_prediction_agent.plist
launchctl list | grep flight
