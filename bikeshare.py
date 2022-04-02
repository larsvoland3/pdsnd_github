import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ("chicago", "new york city", "washington")
months = ("all", "january", "february", "march", "april", "may", "june")
daysofweek = ("all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    while city not in cities:
        city = input("Please choose a city you want to explore (Chicago, New York City or Washington)?:").lower()
        if city not in cities:
            print("City name you entered ({}) not founchicagod in the database.".format(city))
            
    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    while month not in months:
        month = input("Please choose the month you want to check (all, january, february, march, april, may, june)?:").lower()
        if month not in months:
            print("Month you entered ({})not found in the database.".format(month)) 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    while day not in daysofweek:
        day = input("Please choose the day of the week you want to check (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)?:").lower()
        if day not in daysofweek:
            print("Day you entered ({})not found in the database.".format(day))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month)

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most common month: {}'.format(months[popular_month]))
    
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.dayofweek
    popular_day = df['day'].mode()[0] + 1
    print('Most common day of week: {}'.format(daysofweek[popular_day]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

     # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station: ', popular_start_station) 
    
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Common End Station: ', popular_end_station) 


    # TO DO: display most frequent combination of start station and end station trip
    print('Most frequent combination of start and end station: ', df.groupby(['Start Station','End Station']).size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = round((df['Trip Duration'].sum()/3600),2)
    print('Total duration of all trips with the selcted parameters (in hours): ', total_travel,'\n')

    # TO DO: display mean travel time
    average_travel_time = round((df['Trip Duration'].mean()/60),1)
    print('Average travel time (in minutes): ',average_travel_time, '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types:\n', user_types.to_string(), '\n')

    # TO DO: Display counts of gender
    try:
        genders = df['Gender'].value_counts()
        print('User genders:\n', genders.to_string(), '\n')
    except:
        print('No gender data available in the database for this city.')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('Earliest birth year:', df['Birth Year'].min(), '\n')
        print('Most recent birth year:', df['Birth Year'].max(), '\n')
        print('most common birth year:', df['Birth Year'].mode()[0], '\n')
    except:
        print('No birth year data available in the database for this city.')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays example data for the selected data"""
    display_data = False
    user_input = ""
    
    while user_input not in ('yes', 'no'):
        user_input = input("Do you want to see the first 5 rows of the filtered data? (yes or no)").lower()
        if user_input not in ('yes', 'no'):
            print("Please answer with yes or no.") 
    
    display_data = user_input=="yes"
    range_start = (-5)
    range_stop = (-1)
    
    while display_data:
        range_start += 5
        range_stop += 5
        for i in range(range_start, range_stop+1):
            print(df.iloc[i])
            print('\n ----------------------------')
        display_data = input("Do you want to see the next 5 rows of the filtered data? (yes or no)").lower()=="yes"
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
