# teslaPowerwall
A project to automate switching modes for Tesla Powerwall Owners

Welcome! This is my 1st Python project!
In an attempt to simplify the lack of functionality in the Tesla app, I wanted a way to switch the App's mode from Self-powered (self_consumption) to Advanced time-based control. For my use case, I do not want to export energy back to the grid and want to charge my Powerwalls as much as possible to not consume electricity between 3pm - 12am (my peak price times).

I've created two .py files:

teslatoken.py - A Python script to automate getting a valid oauth token from Tesla
  - Read a .yml file that contains the username and password for the Tesla account
  - Obtain an access_token
  - Save the token file to a token.yml file for use while it's valid (default is 45 days set by Tesla)
  - Check to see if the current token is still valid. If not, get a new token
  
products.py - A Python script to obtain the energy_site_id for the Tesla account
  - Get the products for the Tesla account
  - Gather the "energy_site_id" for the account
  - Take command line arguments to switch the mode of the Solar/Powerwalls to/from self_consumption or autonomous

Usage:

Clone this repository to your host:
'git clone https://github.com/natrlhy/teslaPowerwall.git'

Switch the mode to the Self-powered mode in the app:
python3 products.py self_consumption

Switch the mode to Advanced time-based control in the app:
python3 products.py autonomous
