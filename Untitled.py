#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. Import required libraries

# 2. Define a function to extend the list of top track schools

def extend_top_track_schools(schools):
    """
    Extend the list of top track schools in the NCAA to the top 200.

    Parameters:
    schools (list of dicts): List of dictionaries containing school names and states.

    Returns:
    list of dicts: Extended list of top track schools in the NCAA.
    """

    # 3. Placeholder for the extended list
    extended_schools = [
        {'Name': 'Oregon', 'State': 'OR'},
        {'Name': 'Michigan', 'State': 'MI'},
        {'Name': 'Tennessee', 'State': 'TN'},
        {'Name': 'South Carolina', 'State': 'SC'},
        {'Name': 'Colorado', 'State': 'CO'},
        {'Name': 'Oklahoma', 'State': 'OK'},
        {'Name': 'Penn State', 'State': 'PA'},
        {'Name': 'Kentucky', 'State': 'KY'},
        {'Name': 'Iowa', 'State': 'IA'},
        {'Name': 'Auburn', 'State': 'AL'},
        {'Name': 'Nebraska', 'State': 'NE'},
        {'Name': 'Virginia', 'State': 'VA'},
        {'Name': 'Missouri', 'State': 'MO'},
        {'Name': 'Connecticut', 'State': 'CT'},
        {'Name': 'Mississippi', 'State': 'MS'},
        {'Name': 'Kansas', 'State': 'KS'},
        {'Name': 'Arizona', 'State': 'AZ'},
        {'Name': 'California', 'State': 'CA'},
        {'Name': 'Florida International', 'State': 'FL'},
        {'Name': 'Houston', 'State': 'TX'},
        {'Name': 'Louisville', 'State': 'KY'},
        {'Name': 'Western Michigan', 'State': 'MI'},
        {'Name': 'Alabama-Birmingham', 'State': 'AL'},
        {'Name': 'Southern California', 'State': 'CA'},
        {'Name': 'Oklahoma State', 'State': 'OK'},
        {'Name': 'Central Florida', 'State': 'FL'},
        {'Name': 'Boise State', 'State': 'ID'},
        {'Name': 'Miami (FL)', 'State': 'FL'},
        {'Name': 'North Carolina', 'State': 'NC'},
        {'Name': 'Marquette', 'State': 'WI'},
        {'Name': 'Virginia Commonwealth', 'State': 'VA'},
        {'Name': 'Texas A&M', 'State': 'TX'},
        {'Name': 'Arkansas-Little Rock', 'State': 'AR'},
        {'Name': 'Southern Methodist', 'State': 'TX'},
        {'Name': 'Central Michigan', 'State': 'MI'},
        {'Name': 'Baylor', 'State': 'TX'},
        {'Name': 'Texas-San Antonio', 'State': 'TX'},
        {'Name': 'Cincinnati', 'State': 'OH'},
        {'Name': 'Ohio', 'State': 'OH'},
        {'Name': 'Louisiana Tech', 'State': 'LA'},
        {'Name': 'Washington State', 'State': 'WA'},
        {'Name': 'Florida Atlantic', 'State': 'FL'},
        {'Name': 'Gonzaga', 'State': 'WA'},
        {'Name': 'Virginia Tech', 'State': 'VA'},
        {'Name': 'Utah', 'State': 'UT'},
        {'Name': 'Wisconsin-Milwaukee', 'State': 'WI'},
        {'Name': 'Memphis', 'State': 'TN'},
        {'Name': 'Pittsburgh', 'State': 'PA'},
        {'Name': 'Georgia State', 'State': 'GA'},
        {'Name': 'Tulsa', 'State': 'OK'},
        {'Name': 'North Carolina-Wilmington', 'State': 'NC'},
        {'Name': 'Northern Iowa', 'State': 'IA'},
        {'Name': 'Rider', 'State': 'NJ'},
        {'Name': 'Dayton', 'State': 'OH'},
        {'Name': 'Oregon State', 'State': 'OR'},
        {'Name': "St. John's (NY)", 'State': 'NY'},
        {'Name': 'Louisiana-Lafayette', 'State': 'LA'},
        {'Name': 'Akron', 'State': 'OH'},
        {'Name': 'New Mexico', 'State': 'NM'},
        {'Name': 'Xavier', 'State': 'OH'},
        {'Name': 'Connecticut', 'State': 'CT'},
        {'Name': 'Florida Gulf Coast', 'State': 'FL'},
        {'Name': 'Saint Louis', 'State': 'MO'},
        {'Name': 'Wichita State', 'State': 'KS'},
        {'Name': 'Iona', 'State': 'NY'},
        {'Name': 'Iowa State', 'State': 'IA'},
        {'Name': 'Texas-Arlington', 'State': 'TX'},
        {'Name': 'Florida State', 'State': 'FL'},
        {'Name': 'California-Santa Barbara', 'State': 'CA'},
        {'Name': 'Albany (NY)', 'State': 'NY'},
        {'Name': 'Old Dominion', 'State': 'VA'},
        {'Name': 'Seton Hall', 'State': 'NJ'},
        {'Name': 'Eastern Michigan', 'State': 'MI'},
        {'Name': 'Long Beach State', 'State': 'CA'},
        {'Name': 'Belmont', 'State': 'TN'},
        {'Name': 'Charlotte', 'State': 'NC'},
        {'Name': 'St. Josephs (PA)', 'State': 'PA'},
        {'Name': 'Vanderbilt', 'State': 'TN'},
        {'Name': 'Middle Tennessee', 'State': 'TN'},
        {'Name': 'Northeastern', 'State': 'MA'},
        {'Name': 'Georgetown', 'State': 'DC'},
        {'Name': 'Loyola Marymount', 'State': 'CA'},
        {'Name': 'Louisiana-Monroe', 'State': 'LA'},
        {'Name': 'San Diego State', 'State': 'CA'},
        {'Name': 'Richmond', 'State': 'VA'},
        {'Name': 'East Carolina', 'State': 'NC'},
        {'Name': 'Washington', 'State': 'WA'},
        {'Name': 'Jackson State', 'State': 'MS'},
        {'Name': 'Houston', 'State': 'TX'},
        {'Name': 'Wisconsin-Green Bay', 'State': 'WI'},
        {'Name': 'Detroit Mercy', 'State': 'MI'},
        {'Name': 'UCF', 'State': 'FL'},
        {'Name': 'North Texas', 'State': 'TX'},
        {'Name': 'Southern Mississippi', 'State': 'MS'},
        {'Name': 'Southern Illinois', 'State': 'IL'},
        {'Name': 'Montana', 'State': 'MT'},
        {'Name': 'Florida A&M', 'State': 'FL'},
        {'Name': 'Rice', 'State': 'TX'},
        {'Name': 'Rhode Island', 'State': 'RI'},
        {'Name': 'Valparaiso', 'State': 'IN'},
        {'Name': 'Northwestern', 'State': 'IL'},
        {'Name': 'Hawaii', 'State': 'HI'},
        {'Name': 'Kent State', 'State': 'OH'},
        {'Name': 'UTEP', 'State': 'TX'},
        {'Name': 'Western Kentucky', 'State': 'KY'},
        {'Name': 'Lamar', 'State': 'TX'},
        {'Name': 'Northern Arizona', 'State': 'AZ'},
        {'Name': 'Texas A&M-Corpus Christi', 'State': 'TX'},
        {'Name': 'Marshall', 'State': 'WV'},
        {'Name': 'Yale', 'State': 'CT'},
        {'Name': 'Columbia', 'State': 'NY'},
        {'Name': 'Massachusetts', 'State': 'MA'},
        {'Name': 'Creighton', 'State': 'NE'},
        {'Name': 'Tulane', 'State': 'LA'},
        {'Name': 'Northern Illinois', 'State': 'IL'},
        {'Name': 'Toledo', 'State': 'OH'},
        {'Name': 'Illinois State', 'State': 'IL'},
        {'Name': 'Eastern Kentucky', 'State': 'KY'},
        {'Name': 'UC Riverside', 'State': 'CA'},
        {'Name': 'Loyola (MD)', 'State': 'MD'},
        {'Name': 'Stephen F. Austin', 'State': 'TX'},
        {'Name': 'Eastern Washington', 'State': 'WA'},
        {'Name': 'Texas State', 'State': 'TX'},
        {'Name': 'North Dakota State', 'State': 'ND'},
        {'Name': 'Jacksonville State', 'State': 'AL'},
        {'Name': 'South Alabama', 'State': 'AL'},
        {'Name': 'Liberty', 'State': 'VA'},
        {'Name': 'Georgia Southern', 'State': 'GA'},
        {'Name': 'Portland', 'State': 'OR'},
        {'Name': 'Drake', 'State': 'IA'},
        {'Name': 'Mercer', 'State': 'GA'},
        {'Name': 'Southern Utah', 'State': 'UT'},
        {'Name': 'Southern Illinois-Edwardsville', 'State': 'IL'},
        {'Name': 'UC Santa Barbara', 'State': 'CA'},
        {'Name': 'Western Carolina', 'State': 'NC'},
        {'Name': 'Long Island University', 'State': 'NY'},
        {'Name': 'North Florida', 'State': 'FL'},
        {'Name': 'Winthrop', 'State': 'SC'},
        {'Name': 'Sam Houston State', 'State': 'TX'},
        {'Name': 'East Tennessee State', 'State': 'TN'},
        {'Name': 'Montana State', 'State': 'MT'},
        {'Name': 'Coastal Carolina', 'State': 'SC'},
        {'Name': 'Eastern Illinois', 'State': 'IL'},
        {'Name': 'James Madison', 'State': 'VA'},
        {'Name': 'Gardner-Webb', 'State': 'NC'},
        {'Name': 'Wofford', 'State': 'SC'},
        {'Name': 'South Dakota State', 'State': 'SD'},
        {'Name': 'Alcorn State', 'State': 'MS'},
        {'Name': 'McNeese State', 'State': 'LA'},
        {'Name': 'Bethune-Cookman', 'State': 'FL'},
        {'Name': 'North Carolina A&T', 'State': 'NC'},
        {'Name': 'Delaware', 'State': 'DE'},
        {'Name': 'Southeast Missouri State', 'State': 'MO'},
        {'Name': 'Southern', 'State': 'LA'},
        {'Name': 'Texas-Pan American', 'State': 'TX'},
        {'Name': 'Coppin State', 'State': 'MD'},
        {'Name': 'Binghamton', 'State': 'NY'},
        {'Name': 'Morehead State', 'State': 'KY'},
        {'Name': 'New Hampshire', 'State': 'NH'},
        {'Name': 'South Dakota', 'State': 'SD'},
        {'Name': 'Fordham', 'State': 'NY'},
        {'Name': 'Sacred Heart', 'State': 'CT'},
        {'Name': 'Alabama State', 'State': 'AL'},
        {'Name': 'UMKC', 'State': 'MO'},
        {'Name': 'Manhattan', 'State': 'NY'},
        {'Name': 'IUPUI', 'State': 'IN'},
        {'Name': 'Alabama A&M', 'State': 'AL'},
        {'Name': 'Alabama-Birmingham', 'State': 'AL'},
        {'Name': 'Murray State', 'State': 'KY'},
        {'Name': 'St. Francis (PA)', 'State': 'PA'},
        {'Name': 'North Carolina Central', 'State': 'NC'},
        {'Name': 'Loyola (IL)', 'State': 'IL'},
        {'Name': 'Chicago State', 'State': 'IL'},
        {'Name': 'Texas A&M-Corpus Christi', 'State': 'TX'},
        {'Name': 'Hampton', 'State': 'VA'},
        {'Name': 'South Carolina State', 'State': 'SC'},
        {'Name': 'Hartford', 'State': 'CT'},
        {'Name': 'Alabama A&M', 'State': 'AL'},
        {'Name': 'Howard', 'State': 'DC'},
        {'Name': 'Charleston Southern', 'State': 'SC'},
        {'Name': 'Princeton', 'State': 'NJ'},
        {'Name': 'Lafayette', 'State': 'PA'},
        {'Name': 'Niagara', 'State': 'NY'},
        {'Name': 'St. Bonaventure', 'State': 'NY'},
        {'Name': 'Texas Southern', 'State': 'TX'},
        {'Name': 'Lipscomb', 'State': 'TN'},
        {'Name': 'Eastern Kentucky', 'State': 'KY'},
        {'Name': 'Stony Brook', 'State': 'NY'},
        {'Name': 'Austin Peay', 'State': 'TN'},
        {'Name': 'UNC Greensboro', 'State': 'NC'},
        {'Name': 'Colgate', 'State': 'NY'},
        {'Name': 'Central Connecticut', 'State': 'CT'},
        {'Name': 'South Florida', 'State': 'FL'},
        {'Name': 'Robert Morris', 'State': 'PA'},
        {'Name': 'Florida A&M', 'State': 'FL'},
        {'Name': 'Bryant', 'State': 'RI'},
        {'Name': 'Radford', 'State': 'VA'},
        {'Name': 'Mount St. Marys', 'State': 'MD'},
        {'Name': 'UMBC', 'State': 'MD'},
        {'Name': 'Jacksonville', 'State': 'FL'},
        {'Name': 'Quinnipiac', 'State': 'CT'},
        {'Name': 'Nicholls State', 'State': 'LA'},
        {'Name': 'Fairleigh Dickinson', 'State': 'NJ'},
        {'Name': 'Texas-Rio Grande Valley', 'State': 'TX'},
        {'Name': 'Florida Atlantic', 'State': 'FL'},
        {'Name': 'Kennesaw State', 'State': 'GA'},
        {'Name': 'Savannah State', 'State': 'GA'},
        {'Name': 'UC Davis', 'State': 'CA'},
        {'Name': 'Texas A&M-Corpus Christi', 'State': 'TX'},
        {'Name': 'Grambling', 'State': 'LA'},
        {'Name': 'Stetson', 'State': 'FL'},
        {'Name': 'Alabama A&M', 'State': 'AL'},
        {'Name': 'Howard', 'State': 'DC'},
        {'Name': 'Charleston Southern', 'State': 'SC'},
        {'Name': 'Princeton', 'State': 'NJ'},
        {'Name': 'Lafayette', 'State': 'PA'},
        {'Name': 'Niagara', 'State': 'NY'},
        {'Name': 'St. Bonaventure', 'State': 'NY'},
        {'Name': 'Texas Southern', 'State': 'TX'},
        {'Name': 'Lipscomb', 'State': 'TN'},
        {'Name': 'Eastern Kentucky', 'State': 'KY'},
        {'Name': 'Stony Brook', 'State': 'NY'},
        {'Name': 'Austin Peay', 'State': 'TN'},
        {'Name': 'UNC Greensboro', 'State': 'NC'},
        {'Name': 'Colgate', 'State': 'NY'},
        {'Name': 'Central Connecticut', 'State': 'CT'},
        {'Name': 'South Florida', 'State': 'FL'},
        {'Name': 'Robert Morris', 'State': 'PA'},
        {'Name': 'Florida A&M', 'State': 'FL'},
        {'Name': 'Bryant', 'State': 'RI'},
        {'Name': 'Radford', 'State': 'VA'},
        {'Name': 'UMBC', 'State': 'MD'},
        {'Name': 'Jacksonville', 'State': 'FL'},
        {'Name': 'Quinnipiac', 'State': 'CT'},
        {'Name': 'Nicholls State', 'State': 'LA'},
        {'Name': 'Fairleigh Dickinson', 'State': 'NJ'},
        {'Name': 'Texas-Rio Grande Valley', 'State': 'TX'},
        {'Name': 'Houston Baptist', 'State': 'TX'},
        {'Name': 'Siena', 'State': 'NY'},
        {'Name': 'Western Illinois', 'State': 'IL'},
        {'Name': 'SIU Edwardsville', 'State': 'IL'},
        {'Name': 'Holy Cross', 'State': 'MA'},
        {'Name': 'Central Arkansas', 'State': 'AR'},
        {'Name': 'Elon', 'State': 'NC'},
        {'Name': 'Delaware State', 'State': 'DE'},
        {'Name': 'Central Michigan', 'State': 'MI'},
        {'Name': 'Cal State Bakersfield', 'State': 'CA'},
        {'Name': 'Florida International', 'State': 'FL'},
        {'Name': 'Idaho', 'State': 'ID'},
        {'Name': 'Northern Colorado', 'State': 'CO'},
        {'Name': 'Utah Valley', 'State': 'UT'},
        {'Name': 'Cal Poly', 'State': 'CA'},
        {'Name': 'New Orleans', 'State': 'LA'},
        {'Name': 'Army', 'State': 'NY'},
        {'Name': 'Nevada', 'State': 'NV'},
        {'Name': 'Southeastern Louisiana', 'State': 'LA'},
        {'Name': 'Troy', 'State': 'AL'},
        {'Name': 'UNC Wilmington', 'State': 'NC'},
        {'Name': 'Binghamton', 'State': 'NY'},
        {'Name': 'Radford', 'State': 'VA'},
        {'Name': 'Saint Peters', 'State': 'NJ'},
        {'Name': 'Gardner-Webb', 'State': 'NC'},
        {'Name': 'Idaho State', 'State': 'ID'},
        {'Name': 'Hofstra', 'State': 'NY'},
        {'Name': 'Charleston', 'State': 'SC'},
        {'Name': 'Campbell', 'State': 'NC'},
        {'Name': 'Presbyterian', 'State': 'SC'},
        {'Name': 'UC Irvine', 'State': 'CA'},
        {'Name': 'Western Carolina', 'State': 'NC'},
        {'Name': 'Northern Kentucky', 'State': 'KY'},
        {'Name': 'Kennesaw State', 'State': 'GA'},
        {'Name': 'UNC Asheville', 'State': 'NC'},
        {'Name': 'Albany', 'State': 'NY'},
        {'Name': 'UC Santa Barbara', 'State': 'CA'},
        {'Name': 'Cleveland State', 'State': 'OH'},
        {'Name': 'Tennessee Tech', 'State': 'TN'},
        {'Name': 'Eastern Illinois', 'State': 'IL'},
        {'Name': 'St. Francis (NY)', 'State': 'NY'},
        {'Name': 'Robert Morris', 'State': 'PA'},
        {'Name': 'Arkansas State', 'State': 'AR'},
        {'Name': 'Chicago State', 'State': 'IL'},
        {'Name': 'LIU', 'State': 'NY'},
        {'Name': 'Charleston Southern', 'State': 'SC'},
        {'Name': 'Tennessee State', 'State': 'TN'},
        {'Name': 'Alabama State', 'State': 'AL'},
        {'Name': 'UMKC', 'State': 'MO'},
        {'Name': 'Norfolk State', 'State': 'VA'},
        {'Name': 'Alabama A&M', 'State': 'AL'},
        {'Name': 'Savannah State', 'State': 'GA'},
        {'Name': 'Coppin State', 'State': 'MD'},
        {'Name': 'Alcorn State', 'State': 'MS'},
        {'Name': 'Delaware State', 'State': 'DE'},
        {'Name': 'Jackson State', 'State': 'MS'},
        {'Name': 'Texas Southern', 'State': 'TX'},
        {'Name': 'Prairie View A&M', 'State': 'TX'},
        {'Name': 'Mississippi Valley State', 'State': 'MS'},
        {'Name': 'Florida A&M', 'State': 'FL'},
        {'Name': 'Grambling', 'State': 'LA'},
        {'Name': 'Maryland Eastern Shore', 'State': 'MD'},
        {'Name': 'Southern', 'State': 'LA'},
        {'Name': 'Alabama A&M', 'State': 'AL'},
        {'Name': 'Howard', 'State': 'DC'},
        {'Name': 'Charleston Southern', 'State': 'SC'},
        {'Name': 'Princeton', 'State': 'NJ'},
        {'Name': 'Lafayette', 'State': 'PA'},
        {'Name': 'Niagara', 'State': 'NY'},
        {'Name': 'St. Bonaventure', 'State': 'NY'},
        {'Name': 'Texas Southern', 'State': 'TX'},
        {'Name': 'Lipscomb', 'State': 'TN'},
        {'Name': 'Eastern Kentucky', 'State': 'KY'},
        {'Name': 'Stony Brook', 'State': 'NY'},
        {'Name': 'Austin Peay', 'State': 'TN'},
        {'Name': 'UNC Greensboro', 'State': 'NC'},
        {'Name': 'Colgate', 'State': 'NY'},
        {'Name': 'Central Connecticut', 'State': 'CT'},
        {'Name': 'South Florida', 'State': 'FL'},
        {'Name': 'Robert Morris', 'State': 'PA'},
        {'Name': 'Florida A&M', 'State': 'FL'},
        {'Name': 'Bryant', 'State': 'RI'},
        {'Name': 'Radford', 'State': 'VA'},
        {'Name': 'UMBC', 'State': 'MD'},
        {'Name': 'Jacksonville', 'State': 'FL'},
        {'Name': 'Quinnipiac', 'State': 'CT'},
        {'Name': 'Nicholls State', 'State': 'LA'},
        {'Name': 'Fairleigh Dickinson', 'State': 'NJ'},
        {'Name': 'Texas-Rio Grande Valley', 'State': 'TX'},
        {'Name': 'Houston Baptist', 'State': 'TX'},
        {'Name': 'Siena', 'State': 'NY'},
        {'Name': 'Western Illinois', 'State': 'IL'},
        {'Name': 'SIU Edwardsville', 'State': 'IL'},
        {'Name': 'Holy Cross', 'State': 'MA'},
        {'Name': 'Central Arkansas', 'State': 'AR'},
        {'Name': 'Elon', 'State': 'NC'},
        {'Name': 'Delaware State', 'State': 'DE'},
        {'Name': 'Central Michigan', 'State': 'MI'},
        {'Name': 'Cal State Bakersfield', 'State': 'CA'},
        {'Name': 'Florida International', 'State': 'FL'},
        {'Name': 'Idaho', 'State': 'ID'},
        {'Name': 'Northern Colorado', 'State': 'CO'},
        {'Name': 'Utah Valley', 'State': 'UT'},
        {'Name': 'Cal Poly', 'State': 'CA'},
        {'Name': 'New Orleans', 'State': 'LA'},
        {'Name': 'Army', 'State': 'NY'},
        {'Name': 'Nevada', 'State': 'NV'},
        {'Name': 'Southeastern Louisiana', 'State': 'LA'},
        {'Name': 'Troy', 'State': 'AL'},
        {'Name': 'UNC Wilmington', 'State': 'NC'},
        {'Name': 'Binghamton', 'State': 'NY'},
        {'Name': 'Radford', 'State': 'VA'},
        {'Name': 'Gardner-Webb', 'State': 'NC'},
        {'Name': 'Idaho State', 'State': 'ID'},
        {'Name': 'Hofstra', 'State': 'NY'},
        {'Name': 'Charleston', 'State': 'SC'},
        {'Name': 'Campbell', 'State': 'NC'},
        {'Name': 'Presbyterian', 'State': 'SC'},
        {'Name': 'UC Irvine', 'State': 'CA'},
        {'Name': 'Western Carolina', 'State': 'NC'},
        {'Name': 'Northern Kentucky', 'State': 'KY'},
        {'Name': 'Kennesaw State', 'State': 'GA'},
        {'Name': 'UNC Asheville', 'State': 'NC'},
        {'Name': 'Albany', 'State': 'NY'},
        {'Name': 'UC Santa Barbara', 'State': 'CA'},
        {'Name': 'Cleveland State', 'State': 'OH'},
        {'Name': 'Tennessee Tech', 'State': 'TN'},
        {'Name': 'Eastern Illinois', 'State': 'IL'},
        {'Name': 'St. Francis (NY)', 'State': 'NY'},
        {'Name': 'Robert Morris', 'State': 'PA'},
        {'Name': 'Arkansas State', 'State': 'AR'},
        {'Name': 'Chicago State', 'State': 'IL'},
        {'Name': 'LIU', 'State': 'NY'},
        {'Name': 'Charleston Southern', 'State': 'SC'},
        {'Name': 'Tennessee State', 'State': 'TN'},
        {'Name': 'Alabama State', 'State': 'AL'},
        {'Name': 'UMKC', 'State': 'MO'},
        {'Name': 'Norfolk State', 'State': 'VA'},
        {'Name': 'Alabama A&M', 'State': 'AL'},
        {'Name': 'Savannah State', 'State': 'GA'},
        {'Name': 'Coppin State', 'State': 'MD'},
        {'Name': 'Alcorn State', 'State': 'MS'},
        {'Name': 'Delaware State', 'State': 'DE'},
        {'Name': 'Jackson State', 'State': 'MS'},
        {'Name': 'Texas Southern', 'State': 'TX'},
        {'Name': 'Prairie View A&M', 'State': 'TX'},
        {'Name': 'Mississippi Valley State', 'State': 'MS'},
        {'Name': 'Florida A&M', 'State': 'FL'},
        {'Name': 'Grambling', 'State': 'LA'},
        {'Name': 'Maryland Eastern Shore', 'State': 'MD'},
        {'Name': 'Southern', 'State': 'LA'}
    ]
    
    # 4. Return the extended list
    return schools + extended_schools

# 5. Call the function to extend the list of top track schools
extended_schools_list = extend_top_track_schools(schools)

import requests
from bs4 import BeautifulSoup
import pandas as pd
from googlesearch import search


def parse_athlete_performance(html_content, team):
    """Parses HTML content to extract athlete performance details
    
    Parameters:
    - html_content (str): HTML content of the web page
    - team (str): The name of the team to include in the performance details
    
    Returns:
    - List[Dict]: A list of dictionaries where each dictionary contains performance details of an athlete """
    
    soup = BeautifulSoup(html_content, 'html.parser')
    performances = []

    table = soup.find('table', {'class': 'tablesaw'})
    if not table:
        return performances

    for row in table.find_all('tr')[1:]:
        columns = row.find_all('td')
        if len(columns) == 4:
            performance = {
                'Event Name': columns[0].text.strip(),
                'Athlete Name': columns[1].text.strip(),
                'Team': team,
                'Mark': columns[3].text.strip(),
                'Event Type': 'Individual' if len(columns[1].find_all('a')) == 1 else 'Relay'
            }
            performances.append(performance)

    return performances

# initialize
all_performances = []

def search_google(query):
    """Search Google and return the top website

    Parameters:
    query (str): The search query

    Returns:
    str: The URL of the top website from the search results """
    
    search_results = search(query, num=1, stop=1, pause=2)
    top_website = next(search_results, None)
    return top_website

# standard formatting of links in tfrrs
base_url = 'https://www.tfrrs.org/teams/tf/{state}_college_{gender}_{school}.html'

# Add a 'URLs' key to each school with an empty list to store multiple URLs
for school in extended_schools_list:
    school['URLs'] = []

# loop through each school and gender to fetch and parse performances
for school in extended_schools_list:
    for gender in ['m', 'f']:
        team_name = f"{school['Name']} ({'Men' if gender == 'm' else 'Women'})"
        url = base_url.format(state=school['State'], gender=gender, school=school['Name'].replace(' ', '_'))
        response = requests.get(url)

        # print if failed
        if response.status_code == 200:
            performances = parse_athlete_performance(response.text, team_name)
            all_performances.extend(performances)
            
            # Append the URL to the list of URLs for the school
            school['URL'].append(url)
            break  # Break the inner loop once URL is successfully retrieved
        else:
            print(f"Failed to retrieve page for {team_name}")
            print('Attempting to search the web to retrieve link')
            search_query = f'{team_name} track and field tfrrs'
            
            top_website = search_google(search_query)
            if top_website:
                url = top_website
                response = requests.get(url)
                
                # print if failed a second time
                if response.status_code == 200:
                    performances = parse_athlete_performance(response.text, team_name)
                    all_performances.extend(performances)
                    print(f'Failed the first time, but link retrieved via Google search for {team_name}')
                    
                    # Append the URL to the list of URLs for the school
                    school['URL'].append(url)
                    break  # Break the inner loop once URL is successfully retrieved
                else:
                    print('Failed again')
            else:
                print('Google search did not return any results for the team')

# Print out the schools dictionary for manual saving
print(schools)
                
# convert it into a dataframe
df = pd.DataFrame(all_performances)
df

