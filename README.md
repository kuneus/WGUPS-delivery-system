# WGUPS Routing Program
Welcome to the Western Governors University Parcel Service (WGUPS) Routing Program, a project created for WGU's C950 -
Data Structures and Algorithms II. This delivery application takes in CSV data for packages and their distances 
from each other and produces a delivery route divided among 3 delivery trucks and 2 drivers. For this assignment, the 
following requirements and constraints must have been met:
- Each truck can carry a maximum of 16 packages.
- There are 40 packages with unique package IDs.
- All packages must be delivered by their deadline.
- Total mileage traveled by all trucks combined must be under 140 miles.
- Average truck speed is 18 miles per hour.
- The trucks may not leave the hub earlier than 8:00 a.m.
- There is at least 1 package with the wrong address whose address must be updated at 10:20 a.m.
- Some packages must be delivered on the same truck as others, on a specific truck, or are delayed and cannot be loaded 
until they have arrived to the hub.

## Features
- Uses the nearest neighbor algorithm to find an efficient route to deliver the packages.
- Using each package's notes, it parses for constraints and prioritizes those packages first. 
- Tracks total mileage driven by each truck and returns its current location.
- Search for a specific package or packages to find package data and estimated delivery time.
- Get status and data of all packages at once .

## Installation
- Confirm Python 3.16 or later is installed.
- Clone this repository using the command: `git clone https://github.com/kuneus/WGUPS-delivery-system.git`

## Usage
Run the main file via `python3 main.py` in the root directory to start the program.
Input one of the 4 responses for the initial prompt:
- '1' to view the status of a specific package or packages.
- '2' to view the status of all packages.
- '3' to view total miles by all trucks.
- 'q' to quit the program.  

For options 1-3, input the time to view one of the options. For option 1, follow the prompt to input a package or 
multiple package IDs. After fulfillment of the request, the application will return to the main menu with the initial 
prompt.

![](https://github.com/kuneus/gif-repo/blob/main/wgups-routing-program/wgups-demo.gif)

