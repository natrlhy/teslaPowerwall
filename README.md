# teslaPowerwall
A project to automate switching modes for Tesla Powerwall Owners

Welcome! This is my 1st Python project!
In an attempt to simplify the lack of functionallity in the Tesla app, I wanted a way to switch the App's mode from Self-powered (self_consumption) to Advanced time-based control.

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
