import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
city_name = ['chicago', 'new york',  'washington']
chosen_filter = ['month', 'day', 'no']
month_name = ['january', 'february', 'march', 'april', 'may', 'june']
day_name = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    city = input('\nWould you like to see data for Chicago, New York, or Washington?\n').lower()
    while city not in city_name:
        print('\nInvalid input please try again\n')
        city = input('\nWould you like to see data for Chicago, New York, or Washington?\n').lower()

    data_filter=input('\nWould you like to filter the data by month, day, or not at all? Type No if you do not want to filter\n').lower()
    while data_filter not in chosen_filter:
        print('\nInvalid input please try again\n')
        data_filter = input('Would you like to filter the data by month, day, or not at all? Type No if you do not want to filter\n').lower()

    if data_filter == 'month':
        day = 'all'
        month= input('\nWhich month - January, February, March, April, May, or June?\n').lower()
        while month not in month_name:
            print('\nInvalid input please try again\n')
            month = input('Which month - January, February, March, April, May, or June?\n').lower()

    elif data_filter.lower() == 'day':
        month = 'all'
        day = input('\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').lower()
        while day not in day_name:
            print('\nInvalid input please try again\n')
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').lower()

    else:
        month = 'all'
        day = 'all'
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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    df['hour'] = df['Start Time'].dt.hour


    if month != 'all':
        month = month_name.index(month) + 1
        df = df[df['month'] == month]


    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_month = df['month'].mode()[0]


    common_day_of_week = df['day_of_week'].mode()[0]


    common_start_hour = df['hour'].mode()[0]

    print('\nThe most common month is {}\n'.format(common_month))
    print('The most common day of week is {}\n'.format(common_day_of_week))
    print('The most common start hour is {}'.format(common_start_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    Popular_start_station = df['Start Station'].mode()[0]


    Popular_end_station = df['End Station'].mode()[0]

    df['start_end_stations'] = df['Start Station'] + ',' + df['End Station']

    Popular_trip = df['start_end_stations'].mode()[0]

    print('\nThe most popular start station is {}\n'.format(Popular_start_station))
    print('\nThe most popular end station is {}\n'.format(Popular_end_station))
    print('\nThe most popular trip is {}\n'.format(Popular_trip))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()


    average_travel_time = df['Trip Duration'].mean()

    print('\nThe total travel time is {}\n'.format(total_travel_time))
    print('\nThe average travel time is {}\n'.format(average_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_type = df['User Type'].value_counts()

    if city != 'washington':
        gender = df['Gender'].value_counts()

    else:
       gender = '\nThere are no data about gender in washington city'

    if city != 'washington':
        earliest_year_of_birth = df['Birth Year'].min()

        recent_year_of_birth = df['Birth Year'].max()

        common_year_of_birth = df['Birth Year'].mode()[0]

    else:
        earliest_year_of_birth = '\nThere are no data about earliest year of birth in washington city'
        recent_year_of_birth = '\nThere are no data about recent year of birth in washington city'
        common_year_of_birth = '\nThere are no data about common year of birth in washington city'


    print('\nThe count of user types is {}\n'.format(user_type))
    print('\nThe count of gender is {}\n'.format(gender))
    print('\nThe earliest year of birth is {}\n'.format(earliest_year_of_birth))
    print('\nThe recent year of birth is {}\n'.format(recent_year_of_birth))
    print('\nThe most common year of birth is {}\n'.format(common_year_of_birth))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(city):
    """Displays raw data for the specified city"""

    rdf = pd.read_csv(CITY_DATA[city])
    i = 0
    j = i+5
    answer = input('\nDo you want to see the first 5 rows from the raw data?(yes or no)\n').lower()
    while answer == "yes":
        print(rdf[i:j])
        i += 5
        answer = input('\nDo you want to see 5 more rows from the raw data?(yes or no)\n').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
