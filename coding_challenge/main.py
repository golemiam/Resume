import csv
import pandas as pd
import requests
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from turtle import Turtle

import numpy as np

#from pandas_datareader import data
#from pandas.tseries import offsets


def main():
    """
    Main program for addressing challenge questions
    :return:
    Returns values based on user input
    """

    run_project()
def run_project():
    """
    Chooses a question to address
    :return:
    Returns the function chosen.
    """

    fresh_data_input = input("Would you like a fresh set of data? 1 for yes, 2 for no. ")
    # Obtains user input to determine if the site will pull up.
    if fresh_data_input == "1":
        # If the user chooses one, this will take them to the site. (open_browser below opens, print statement explains)
        print("""
        Export the data in the website and save it as 'COVID_19_Nursing_Home_Data_01_22_2023.csv' 
        then respond to the program.
        """)
        open_browser()
    else:
        # If the user doesn't need fresh data the program continues
        pass

    pd.set_option('display.max_columns', 22)
    # This allows the user to see all 22 of the columns
    question_choice = input("Which question would you like to run? ")
    # This allows the user to determine which challenge question that they want to look into.

    if question_choice == "1":
        read_panda_file_question_1()
        # Looks at the first of the challenge questions provided.
    elif question_choice == "2":
        read_panda_file_question_2()
        # Looks at the second of the challenge questions provided.
    elif question_choice == "3":
        read_panda_file_question_3()
        # Looks at the first bonus question provided.
    elif question_choice == "4":
        read_panda_file_question_4()
        # Looks at the second bonus question.

    draw_something(question_choice)
    # references draw_something function below. Draws based on question. something for fun.



def open_browser():
    """
    Used to open the website.
    :return: Opens either the chrome or the firefox browser depending on the users choice.
    """
    inter_choice = input("Chrome or firefox. 1 for Chrome, 2 for firefox ")
    # Sets up choice for user to determine browser option.
    if inter_choice == "1":
        driver = webdriver.Chrome()
        driver.get(
        "https://data.cms.gov/covid-19/covid-19-nursing-home-data/data?query=%7B%22filters%22%3A%7B%22rootConjunction%22%3A%7B%22label%22%3A%22And%22%2C%22value%22%3A%22AND%22%7D%2C%22list%22%3A%5B%5D%7D%2C%22keywords%22%3A%22%22%2C%22offset%22%3A0%2C%22limit%22%3A10%2C%22sort%22%3A%7B%22sortBy%22%3Anull%2C%22sortOrder%22%3Anull%7D%2C%22columns%22%3A%5B%22week_ending%22%2C%22federal_provider_number%22%2C%22provider_name%22%2C%22provider_city%22%2C%22provider_state%22%2C%22provider_zip_code%22%2C%22provider_phone_number%22%2C%22residents_weekly_confirmed_covid_19%22%2C%22number_of_all_healthcare_personnel_eligible_to_work_in_this_facility_for_at_least_1_day_this_week_who_received_a_completed_covid_19_vaccination_at_any_time%22%2C%22recent_percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time%22%2C%22percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time%22%2C%22percentage_of_current_healthcare_personnel_with_a_completed_vaccination_who_received_a_covid_19_vaccine_booster_at_any_time%22%2C%22Recent_Percentage_of_Current_Healthcare_Personnel_Up_to_Date_with_COVID_19_Vaccines%22%2C%22Percentage_of_Current_Healthcare_Personnel_Up_to_Date_with_COVID_19_Vaccines%22%5D%7D")  # put here the adress of your page
        # Opens chrome browser.

    if inter_choice == "2":
        driver = webdriver.Firefox()
        driver.get(
        "https://data.cms.gov/covid-19/covid-19-nursing-home-data/data?query=%7B%22filters%22%3A%7B%22rootConjunction%22%3A%7B%22label%22%3A%22And%22%2C%22value%22%3A%22AND%22%7D%2C%22list%22%3A%5B%5D%7D%2C%22keywords%22%3A%22%22%2C%22offset%22%3A0%2C%22limit%22%3A10%2C%22sort%22%3A%7B%22sortBy%22%3Anull%2C%22sortOrder%22%3Anull%7D%2C%22columns%22%3A%5B%22week_ending%22%2C%22federal_provider_number%22%2C%22provider_name%22%2C%22provider_city%22%2C%22provider_state%22%2C%22provider_zip_code%22%2C%22provider_phone_number%22%2C%22residents_weekly_confirmed_covid_19%22%2C%22number_of_all_healthcare_personnel_eligible_to_work_in_this_facility_for_at_least_1_day_this_week_who_received_a_completed_covid_19_vaccination_at_any_time%22%2C%22recent_percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time%22%2C%22percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time%22%2C%22percentage_of_current_healthcare_personnel_with_a_completed_vaccination_who_received_a_covid_19_vaccine_booster_at_any_time%22%2C%22Recent_Percentage_of_Current_Healthcare_Personnel_Up_to_Date_with_COVID_19_Vaccines%22%2C%22Percentage_of_Current_Healthcare_Personnel_Up_to_Date_with_COVID_19_Vaccines%22%5D%7D")  # put here the adress of your page
        # Opens firefox browser.

    url = "https://data.cms.gov/covid-19/covid-19-nursing-home-data/data?query=%7B%22filters%22%3A%7B%22rootConjunction%22%3A%7B%22label%22%3A%22And%22%2C%22value%22%3A%22AND%22%7D%2C%22list%22%3A%5B%5D%7D%2C%22keywords%22%3A%22%22%2C%22offset%22%3A0%2C%22limit%22%3A10%2C%22sort%22%3A%7B%22sortBy%22%3Anull%2C%22sortOrder%22%3Anull%7D%2C%22columns%22%3A%5B%22week_ending%22%2C%22federal_provider_number%22%2C%22provider_name%22%2C%22provider_city%22%2C%22provider_state%22%2C%22provider_zip_code%22%2C%22provider_phone_number%22%2C%22residents_weekly_confirmed_covid_19%22%2C%22number_of_all_healthcare_personnel_eligible_to_work_in_this_facility_for_at_least_1_day_this_week_who_received_a_completed_covid_19_vaccination_at_any_time%22%2C%22recent_percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time%22%2C%22percentage_of_current_healthcare_personnel_who_received_a_completed_covid_19_vaccination_at_any_time%22%2C%22percentage_of_current_healthcare_personnel_with_a_completed_vaccination_who_received_a_covid_19_vaccine_booster_at_any_time%22%2C%22Recent_Percentage_of_Current_Healthcare_Personnel_Up_to_Date_with_COVID_19_Vaccines%22%2C%22Percentage_of_Current_Healthcare_Personnel_Up_to_Date_with_COVID_19_Vaccines%22%5D%7D"
    # Creates variable for later use.
    driver.get(url)
    # Gets the driver for the URL
    driver.implicitly_wait(20)
    # Tells the browser to stay open for a little bit.
    element = driver.find_element(By.CLASS_NAME, "open_export_btn")
    # To gather button
    driver.execute_script("arguments[0].click();", element)
    # To click on button


def read_panda_file_question_1():
    """
    This function is used to collect the data, get user input, and give a response based on input.
    The input request gives the details.
    :return:
    Returns percentage values over 80% for the various percentage columns for healthcare personnel.
    """
    covid_df = pd.read_csv('COVID_19_Nursing_Home_Data_01_22_2023.csv')
    # Reads the Nursing Home Data csv for use as a variable.

    provider_df = pd.read_csv('Our_Provider_numbers.csv')
    #converts csv to a variable for use.

    facility_choice = input("""
       Which facility would you like information for? '1' for everything, '2' for everything at ensign. For 
       everything else name the facility you would like listed.
       """)
    # Creates a variable to hold user input for deciding how the user would like to sort the data.

    try:
        int(facility_choice[0])
        # Checks to see if facility choice is a number
        facility_choice_other = 0
        # Sets the facility_choice_other variable to zero so it can be used for sorting below.

    except:
        facility_choice_other = facility_choice.upper()
        # Accepts string input from the user to compare to a facility name
        facility_choice = 3
        # Sets the facility_choice_other to 3 for later sorting below
    try:
        a = [f"{(facility_choice)}", provider_df]
        # Groups the facility choice with the provider to check for similarity.

    except:
        print("That doesn't quite work")
        # Lets the user know that their option doesn't work

    if facility_choice == '1'.lower():
        pass
        # This allows for everything to be included
    elif facility_choice == '2'.lower():
        merger_df = provider_df.merge(right=covid_df, how="left", left_on="our affilitied federal provider numbers", right_on="Federal Provider Number")
        # This selects only the facilities related to ensign.

        covid_df = merger_df
        # This is so that calculations below will be unhindered and will apply everything as normal to the ensign facilities.

    elif facility_choice_other != 0:
        print(covid_df[covid_df["Provider Name"].str.lower() == facility_choice_other.lower()])
        # Isolates a single facility by string value (their name).
        providers = covid_df.groupby("Provider Name")
        # Groups Facilities together by name
        facility_df = providers.get_group(facility_choice_other)
        # Uses groupings to establish facility dataframe
        covid_df = facility_df
        # Sets the DataFrame to covid_df for later calculations previously established.


    elif f"{str(facility_choice)}" in a:
        providers = covid_df.groupby("Federal Provider Number")
        # Groups by the Federal Provider Number
        facility = providers.get_group(facility_choice)
        # Creates DataFrame using Federal Provider Number Groups
        facility_mix = pd.DataFrame({f'{facility["Provider Name"].values}': range(len(facility))})
        # Obtains the number for the index to be set
        facility.index = facility_mix.index
        # Sets the index based on the amount obtained above.
        covid_df = facility
        # Sets the DataFrame to covid_df for later calculations previously established.

    try:
        covid_simple_titles = covid_df.rename(columns= {
    'Week Ending': 'W_End', 
    'Federal Provider Number': 'FP_num', 
    'Provider Name': 'P_name', 
    'Provider City': 'P_city', 
    'Provider State': 'P_state', 
    'Provider Zip Code': 'P_zip', 
    'Provider Phone Number': 'P_Phone_#', 
    'Residents Weekly Confirmed COVID-19': 'Cov_residents', 
    'Number of All Healthcare Personnel Eligible to Work in this Facility for At Least 1 Day This Week who Received a Completed COVID-19 Vaccination at Any Time': 'HCP#_vacc', 
    'Recent Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time': 'Percentage_1', 
    'Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time': 'Percentage_2', 
    'Percentage of Current Healthcare Personnel with No Medical Contraindications who Received a Completed COVID-19 Vaccination at Any Time': 'Percentage_3', 
    'Number of Healthcare Personnel with a Completed Vaccination Eligible to Work in this Facility for At Least 1 Day This Week who Received a COVID-19 Vaccine Booster at Any Time': 'HCP#_2', 
    'Recent Percentage of Current Healthcare Personnel with a Completed Vaccination who Received a COVID-19 Vaccine Booster at Any Time': 'Percentage_4', 
    'Percentage of Current Healthcare Personnel with a Completed Vaccination who Received a COVID-19 Vaccine Booster at Any Time': 'Percentage_5', 
    'Recent Percentage of Current Healthcare Personnel Up to Date with COVID-19 Vaccines': 'Percentage_6', 
    'Percentage of Current Healthcare Personnel Up to Date with COVID-19 Vaccines': 'Percentage_7', 
    'Percentage of Current Healthcare Personnel with a Completed Vaccination Up to Date with COVID-19 Vaccines': 'Percentage_8'
    })
    #Changes column names for easier calculations
    except:
        print("No simple titles")

    user_choice = input("""Which Percentage information would you like? 
    A for 'Recent Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time' 
    B for 'Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time'
    C for 'Percentage of Current Healthcare Personnel with No Medical Contraindications who Received a Completed COVID-19 Vaccination at Any Time'
    D for 'Recent Percentage of Current Healthcare Personnel with a Completed Vaccination who Received a COVID-19 Vaccine Booster at Any Time'
    E for 'Percentage of Current Healthcare Personnel with a Completed Vaccination who Received a COVID-19 Vaccine Booster at Any Time'
    F for 'Recent Percentage of Current Healthcare Personnel Up to Date with COVID-19 Vaccines'
    G for 'Percentage of Current Healthcare Personnel Up to Date with COVID-19 Vaccines'
    H for 'Percentage of Current Healthcare Personnel with a Completed Vaccination Up to Date with COVID-19 Vaccines'
    """)
    # prompts the user for a selection
    if user_choice == 'A'.lower():
        #Uses selection A
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_1 > 80]
        # Collects over 80 percent values for selection
        print(f"Week: {percent_a['W_End']} : Percent: {percent_a['Percentage_1']}")
    if user_choice == 'B'.lower():
        # user gets results for choice B
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_2 > 80]
        # Collects over 80 percent values for selection
        print(f"{percent_a['W_End']} : {percent_a['Percentage_2']}")

    if user_choice == 'C'.lower():
        # user gets results for choice C
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_3 > 80]
        # Collects over 80 percent values for selection
        print(f"{percent_a['W_End']} : {percent_a['Percentage_3']}")
    if user_choice == 'D'.lower():
        # user gets results for choice D
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_4 > 80]
        # Collects over 80 percent values for selection
        print(f"{percent_a['W_End']} : {percent_a['Percentage_4']}")
    if user_choice == 'E'.lower():
        # user gets results for choice E
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_5 > 80]
        # Collects over 80 percent values for selection
        print(f"{percent_a['W_End']} : {percent_a['Percentage_5']}")
    if user_choice == 'F'.lower():
        # user gets results for choice F
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_6 > 80]
        # Collects over 80 percent values for selection
        print(f"{percent_a['W_End']} : {percent_a['Percentage_6']}")
    if user_choice == 'G'.lower():
        # user gets results for choice G
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_7 > 80]
        # Collects over 80 percent values for selection
        print(f"{percent_a['W_End']} : {percent_a['Percentage_7']}")
    if user_choice == 'H'.lower():
        # user gets results for choice H
        percent_a = covid_simple_titles[covid_simple_titles.Percentage_8 > 80]
        # Collects over 80 percent values for selection
        print(f"Week: {percent_a['W_End']} : Percent: {percent_a['Percentage_8']}")
    data = percent_a
    # Prepares the data variable for saving to a file with the function call below.

    save_to_file(data)
    # Calls the save_to_file function so that the information gathered for question one will be saved to a file.


def read_panda_file_question_2():
    """
    Helps answer the question regarding the longest streak of residents not testing
    positive for covid.
    :return:
    returns the value of the longest streaks.
    """

    covid_df = pd.read_csv('COVID_19_Nursing_Home_Data_01_22_2023.csv')
    # Reads the csv file
    covid_simple_titles = covid_df.rename(columns={
        'Week Ending': 'W_End',
        'Federal Provider Number': 'FP_num',
        'Provider Name': 'P_name',
        'Provider City': 'P_city',
        'Provider State': 'P_state',
        'Provider Zip Code': 'P_zip',
        'Provider Phone Number': 'P_Phone_#',
        'Residents Weekly Confirmed COVID-19': 'covid_weekly_count',
        'Number of All Healthcare Personnel Eligible to Work in this Facility for At Least 1 Day This Week who Received a Completed COVID-19 Vaccination at Any Time': 'HCP#_vacc',
        'Recent Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time': 'Percentage_1',
        'Percentage of Current Healthcare Personnel who Received a Completed COVID-19 Vaccination at Any Time': 'Percentage_2',
        'Percentage of Current Healthcare Personnel with No Medical Contraindications who Received a Completed COVID-19 Vaccination at Any Time': 'Percentage_3',
        'Number of Healthcare Personnel with a Completed Vaccination Eligible to Work in this Facility for At Least 1 Day This Week who Received a COVID-19 Vaccine Booster at Any Time': 'HCP#_2',
        'Recent Percentage of Current Healthcare Personnel with a Completed Vaccination who Received a COVID-19 Vaccine Booster at Any Time': 'Percentage_4',
        'Percentage of Current Healthcare Personnel with a Completed Vaccination who Received a COVID-19 Vaccine Booster at Any Time': 'Percentage_5',
        'Recent Percentage of Current Healthcare Personnel Up to Date with COVID-19 Vaccines': 'Percentage_6',
        'Percentage of Current Healthcare Personnel Up to Date with COVID-19 Vaccines': 'Percentage_7',
        'Percentage of Current Healthcare Personnel with a Completed Vaccination Up to Date with COVID-19 Vaccines': 'Percentage_8'
    })
    # The above makes the column names manageable.

    max_count_list = []
    # Creates an empty list for maximum counts for later use
    provider_list = []
    # Creates an empty list for providers for later use
    provider = ''
    # creates an empty variable for a provider for later use
    count_list = []
    # creates an empty list for counts for later use
    count = 0
    # Creates count variable for later use
    max_count = 0
    # Creates max_count variable for later use
    for row, counter in zip(covid_simple_titles['P_name'], covid_simple_titles['covid_weekly_count']):
        # Used to iterate 2 new variables through 2 columns 'P_name' and 'covid_weekly_count'
        if provider == row:
            if counter < 1:
                count += 1
                # Used to iterate a count
            else:
                count_list.append(count)
                # Adds to the highest final count for each facility.

                count = 0
                # Resets the count.

        else:
            if provider_list != [] and max_count != max(count_list):
                print(f"Provider: {provider}, Weeks without Covid: {max(count_list)} ")
                max_count = max(count_list)
                # This helps identify the highest count at a facility
            provider = row
            # This resets the provider so that it will iterate through the next facility
            provider_list.append(provider)
            # This adds to the list of facilities
            max_count_list.append(max_count)
            # This adds to the list of highest facility counts.
            count_list = [0]
            # This resets the count list so that the current highest count won't inhibit the next count.

    data = [f"{provider_list}, {max_count_list}"]
    # Prepares data variable for the save to file function using the information gathered from the provider_list and max_count_list variables.

    save_to_file(data)
    # Uses the save to the "save_to_file" function created. Saves the file according to user preference.

def read_panda_file_question_3():
    """
    No inputs are needed for this, it is chosen by by selecting the user choice.
    Also known as bonus question 1.
    :return:
    Returns optional data for cleaning up data, or isolating some of the bad data
    """
    bonus_df = pd.read_csv('bonus_challenge.csv', parse_dates= ["date_last_administered"])
    # Reads in the DataFrame for the Bonus question

    filled_nan = bonus_df.fillna(-1)
    # Replaces NaN values with -1

    no_dates = filled_nan["date_last_administered"] == -1
    # gathers all of the data where no date was input

    medically_exempt = filled_nan["medically_exempt"] == 1
    # gathers all of the data where someone was medically exempt

    refused = filled_nan["refused"] == 1
    # gathers all of the data where someone refused

    xor_group_1 = filled_nan[no_dates^medically_exempt^refused]
    # Attempt to isolate information

    pfizer_one = filled_nan["got_pfizer1"] == 1
    pfizer_two = filled_nan["got_pfizer2"] == 1
    pfizer_three = filled_nan["got_pfizer3"] == 1
    # The above 3 each identify where pfizer vaccines were administered

    moderna_one = filled_nan["got_moderna1"] == 1
    moderna_two = filled_nan["got_moderna2"] == 1
    moderna_three = filled_nan["got_moderna3"] == 1
    # The above 3 each identify where moderna vaccines were administered

    janssen_one = filled_nan["got_janssen1"] == 1
    janssen_two = filled_nan["got_janssen2"] == 1
    # The above 3 each identify where janssen vaccines were administered

    unknown_one = filled_nan["got_unknown1"] == 1
    unknown_two = filled_nan["got_unknown2"] == 1
    unknown_three = filled_nan["got_unknown3"] == 1
    # The above 3 each identify where unknown vaccines were administered

    xor_group_2 = filled_nan[(moderna_one|moderna_two|moderna_three)^(janssen_one|janssen_two)^(pfizer_one|pfizer_two|pfizer_three)^(unknown_one|unknown_two|unknown_three)^refused^medically_exempt]
    # Used to verify that multiple types were not administered, count comes up as 99, suggests that there's only one in this category, probably same as xor_group_1

    sorted_employees = filled_nan.sort_values("employee_id")
    # Sorts the Employee ID's in ascending order
    sorted_dates = bonus_df.sort_values("date_last_administered")
    # Sorts the dates where the vaccines were last administered
    sorted_dates.reset_index(inplace=True)
    # Creates a new index for the sorted dates
    sorted_employees.reset_index(inplace=True)
    # Creates a new index for the sorted employee ID's
    user_choice = input("""
    How would you like to see the data? 
    1 for employee ID numbers sorted. 
    2 for Dates sorted.
    3 for unsorted with -1 for NaN
    4 for no recorded information on employee """)
    # Sets up User options

    if user_choice == '1':
        print(f"List of sorted Employee ID numbers: {sorted_employees}")
        # Prints out with the employee IDs sorted in ascending order
        data = [f"{sorted_employees}"]
        # Prepares data variable for the save to file function using the information gathered from the sorted_employees variables.

    elif user_choice == '2':
        print(f"List of sorted dates: {sorted_dates}")
        # Prints out with the Dates sorted in ascending order
        data = [f"{sorted_dates}"]
        # Prepares data variable for the save to file function using the information gathered from the sorted_dates variables.

    elif user_choice == '3':
        print(xor_group_2)
        #Prints out all of the data, without anything sorted, but has the NaN's replaced.
        data = [f"{xor_group_2}"]
        # Prepares data variable for the save to file function using the information gathered from the xor_group_2 variables.

    elif user_choice == '4':
        print(xor_group_1)
        # Isolates the one piece of illogical data (No information is really gathered from it)


    save_to_file(data)
    # Uses the save to the "save_to_file" function created. Saves the file according to user preference.

def read_panda_file_question_4():
    """
    This function just prints out the SQL query needed to be included in a SQL query.
    I imported the data from the excel spreadsheet named "bonus_challenge.xlsx" into a database
    and named the database "Bonus", then into a sheet named "Sheet1$" (I left the name the same)
    :return:
    When you run the query it will create 4 different views with fully vaccinated employees.
    1 view for each type of vaccination.
    """
    print("""Question 4 (Bonus question 2)
    

  SELECT employee_id as 'Fully_vaccinated_pfizer' FROM [Bonus].[dbo].[Sheet1$]
    WHERE got_pfizer1 = 1 AND got_pfizer3 = 1 OR got_pfizer1 = 1 AND got_pfizer2 = 1  AND got_pfizer3 = 1
    OR got_pfizer2 = 1 AND got_pfizer3 = 1 /* I included 2 and 3 because 2 in the timeline would be more beneficial then 1 anyway.*/
    
  SELECT employee_id AS 'fully_vaccinated_moderna' FROM [Bonus].[dbo].[Sheet1$]
    WHERE (got_moderna1 = 1 AND got_moderna2 = 1) OR (got_moderna2 = 1 AND got_moderna3 = 1) /* I included 2 and 3 because 3 in the timeline would be more beneficial then 1 anyway.*/
    OR (got_moderna1 = 1 AND got_moderna3 = 1) /* I included 1 and 3 because 3 in the timeline would be more beneficial then 2 anyway.*/
    OR (got_moderna1 = 1 AND got_moderna2 = 1 AND got_moderna3 = 1) OR (got_unknown1 = 1 AND got_unknown2 = 1);
  SELECT employee_id AS 'fully_vaccinated_unknown' FROM [Bonus].[dbo].[Sheet1$]  
    WHERE (got_unknown1 = 1 AND got_unknown3 = 1) /* I included 1 and 3 because 3 in the timeline would be more beneficial then 2 anyway. */
    OR (got_unknown2 = 1 AND got_unknown3 = 1) /* I included 2 and 3 because 3 in the timeline would be more beneficial then 1 anyway.*/
    OR (got_unknown1 = 1 AND got_unknown2 = 1 AND got_unknown3 = 1)
  SELECT employee_id AS 'fully_vaccinated_Janssen' FROM [Bonus].[dbo].[Sheet1$]
    WHERE (got_Janssen1 = 1 AND got_Janssen2 = 1) 
    """)
    # Input the above into SQL (See main doc string for this function)

def save_to_file(data):
    """
    Takes data collected from the questions above and saves it to a file for the users convenience.
    :param data: This is a parameter auto generated by the various questions above.
    :return: Saves the file to the name given by the user.
    """
    out_file_choice = input("What would you like to name the file? ")
    # Allows the user to name the file.
    try:
        with open(out_file_choice, "x") as out_file:
            # Checks for file name duplicate
            print(data, file= out_file)
            # Saves the file
    except:
        out_file_placer = "placer.txt"
        # creates a variable for the duplicates new location to avoid saving over another file.
        with open(out_file_placer, "w") as out_file:
            print(data, file= out_file)
            # Saves the file to the placer.txt
            print("""
                You chose a file name that has already been taken, 
            your data has been placed in placer.txt and will be 
            overwritten when this program runs again. Either choose 
            a new file name where you would like this saved, or view 
            the data now before it gets removed. 
            """)
            # Describes to the user regarding the duplicate file name.

def draw_something(question_choice):
    """
    Draws something for each of the questions, used to add a little flair.
    :param question_choice: Uses the chosen question that was requested by the user.
    :return: Draws something (Multiple options)
    """
    t = Turtle()
    # Creates a variable for the turtle drawing module.

    def draw_small_circle():
        """
        Draws a small circle for the 80+ eight, 2 are used.
        :return: Draws a small hard set circle
        """
        t.down()
        # Puts the "pen down" which makes it start drawing at whatever position the "pen" is.
        t.circle(50, 360, 20)
        # Draws a circle with a 50 pixel radius.
        t.up()
        # lifts "the pen up" to stop drawing at the point where it is.

    def draw_oval():
        """
        Draws a zero for the 80
        :return: Draws an Oval
        """
        t.setheading(45)
        # Tells the pen the direction to face when it starts drawing.
        t.down()
        # Puts the "pen down" which makes it start drawing at whatever position the "pen" is.

        for i in range(2):
            # Sets up iteration (to iterate twice)
            t.circle(110, 90)
            # Draws a quarter circle with larger radius
            t.circle(110//2, 90)
            #Draws a quarter circle with smaller radius
        t.up()
        # lifts "the pen up" to stop drawing at the point where it is.

    def draw_plus(x, y):
        """
        Draws a plus for the 80+, length of each line hard coded to 100.
        Heading hard coded to 0 and 90
        :param x: Indicates the starting X coordinate
        :param y: Indicates the starting Y coordinate
        :return: Draws a plus sign
        """
        t.goto(x, y)
        # Moves "the pen" to the coordinate x,y
        t.down()
        # Puts the "pen down" which makes it start drawing at whatever position the "pen" is.
        t.setheading(90)
        # Tells the pen the direction to face when it starts drawing.
        t.forward(100)
        # Draws a straight line.
        t.up()
        # lifts "the pen up" to stop drawing at the point where it is.
        t.goto(x-50, y+50)
        # Moves "the pen" to the coordinate x,y using adjustments
        t.setheading(0)
        # Tells the pen the direction to face when it starts drawing.
        t.down()
        # Puts the "pen down" which makes it start drawing at whatever position the "pen" is.
        t.forward(100)
        # Draws a straight line.

    def draw_line(x, y, length, direction):
        """
        Draws a line, for whenever it is needed
        :param x: Indicates the starting X coordinate
        :param y: Indicates the starting Y coordinate
        :param length: Indicates the size or length of the line (no variations on width)
        :param direction: Indicates which direction the line will draw towards
        :return: Draws a line
        """
        t.up()
        # lifts "the pen up" to stop drawing at the point where it is.
        t.goto(x,y)
        # Moves "the pen" to the coordinate x,y
        t.setheading(direction)
        # Tells the pen the direction to face when it starts drawing.
        t.down()
        # Puts the "pen down" which makes it start drawing at whatever position the "pen" is.
        t.forward(length)
        # Draws a straight line. The "length" gives the length of the line.
        t.up()
        # lifts "the pen up" to stop drawing at the point where it is.

    def draw_variable_circle(x, y, tilt=None, radius=None, extent=None, steps=None):
        """
        Draws the circle that can be adjusted
        :param x: Indicates the starting X coordinate
        :param y: Indicates the starting Y coordinate
        :param tilt: Indicates the direction it faces when it begins to draw (Or heading)
        :param radius: Indicates the radius of the circle you want
        :param extent: Indicates how much of the circle you want. (360 being a full circle)
        :param steps: Indicates the smoothness of the circle (360 for a perfectly smooth circle, but will draw slowly)
        :return: Returns a drawing of a black circle.
        """
        t.up()
        # lifts "the pen up" to stop drawing at the point where it is.
        if x != "0" or y != "0":
            t.goto(x,y)
            # Moves "the pen" to the coordinate x,y
        if tilt != "0":
            t.setheading(tilt)
            # Tells the pen the direction to face when it starts drawing. (tilt gives the direction)
        t.down()
        # Puts the "pen down" which makes it start drawing at whatever position the "pen" is.
        t.circle(radius, extent, steps)
        # Draws a circle with variables assigned
        t.up()
        # lifts "the pen up" to stop drawing at the point where it is.



    if question_choice == "1":
        # Draws 80+ to indicate the 80% and above.

        t.up()
        # lifts "the pen up" to stop drawing at the point where it is.
        t.goto(-80, 80)
        # Moves "the pen" to the coordinate x,y
        draw_small_circle()
        # Draws a small circle
        t.goto(-80, -20)
        # Moves "the pen" to the coordinate x,y
        draw_small_circle()
        # The above lines draw the 8

        t.goto(80, -10)
        # Moves "the pen" to the coordinate x,y
        draw_oval()
        # Draws the zero

        draw_plus(180, 20)
        # Draws the plus sign

    if question_choice == "2":
        # Draws MAX to indicate maximums

        draw_line(x = -100, y=-50, length=100, direction=90)
        draw_line(-100, 50, 100, -60)
        draw_line(0, -50, 100, 90)
        draw_line(0, 50, 100, 240)
        # Draws the M

        draw_line(x= 30, y=-50, length=100, direction=70)
        draw_line(100, -50, 100, 110)
        draw_line(45, 0, 40, 0)
        # Draws the A

        draw_line(x=110, y=-50, length=150, direction=45)
        draw_line(110, 50, 150, 315)
        # Draws the X

    if question_choice == "3":
        #This option draws a broom to symbolize cleaning of the data.

        draw_variable_circle(x=-100,y=100, tilt=135, radius=6, extent=90)
        draw_variable_circle(x="0", y="0", tilt="0", radius=6, extent=90)
        #Draws the rounded top of the broom

        draw_line(-100, 100, 100, 300)
        draw_line(-108, 92, 100, 300)
        #Draws the lines for the stick portion of the broom

        draw_variable_circle(-32, 10, 135, 16, 90)
        draw_variable_circle(x="0", y="0", tilt="0", radius=16, extent=90)
        # Draws the rounded top of the broom

        draw_line(-32, 10, 100, 300)
        draw_line(-56, -12, 100, 300)
        draw_line(-22, -10, 32, 210)
        draw_line(16, -78, 36, 220)
        # The four lines above draw the bottom of the broom

    if question_choice == "4":
        draw_variable_circle(x=-100, y=100, tilt=135, radius=30, extent=90)
        draw_variable_circle(x="0", y="0", tilt="0", radius=30, extent=90)
        draw_variable_circle(x="0", y="0", tilt="0", radius=30, extent=90)
        draw_variable_circle(x=-100, y=0, tilt=0, radius=30, extent=90)
        draw_variable_circle(x="0", y="0", tilt="0", radius=30, extent=90)
        # Draws the S in the lines above

        draw_variable_circle(0, 0, 0, 60, 360)
        draw_line(15, 15, 60, 330)
        # Draws the Q with 2 lines above

        draw_line(100, 0, 120, 90)
        draw_line(100, 0, 60, 0)
        # Draws the L with the 2 lines above










if __name__ == "__main__":
    main()

