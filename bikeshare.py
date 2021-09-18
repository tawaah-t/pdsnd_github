import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello and welcome! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York, or Washington?\n")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Invalid input. Please enter a valid input")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("For which month Would you like to see data? January, February, March, April, May, or June? or type all.\n")
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Invalid input. Please enter a valid input")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Do you want details about specific day of the week? If yes, type name of any day of the week or type all.\n")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Invalid input. Please enter a valid input")

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month

    # find the most popular month
    popular_month = df['month'].mode()[0]

    print('Most Popular Start month:', popular_month)

    # extract day from the Start Time column to create an day column
    df['day'] = df['Start Time'].dt.day_name()

    # find the most popular day
    popular_day = df['day'].mode()[0]

    print('Most Popular day of the week:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    start_station = df['Start Station'].mode()[0]
    print('Commonly Used Start Station:',start_station)

    # TO DO: display most commonly used end station

    end_station = df['End Station'].mode()[0]
    print('Commonly Used End Station:',end_station)

    # TO DO: display most frequent combination of start station and end station trip
    com = df['Start Station'] + " " + df['End Station'].mode()[0]
    print('Most frequent combination of start station and end station trip:',com)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print('Total travel time',total)
    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print('Average travel time',mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()

    print('Users Types:',user_types)

     # TO DO: Display counts of gender

    if city == 'chicago' or city == 'new york city':
        user_gender = df['Gender'].value_counts()
        print('Users Gender:',user_gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        oldest = df['Birth Year'].min()

        youngest = df['Birth Year'].max()

        common = df['Birth Year'].mode()[0]

        print('Oldest Users:',oldest)
        print('youngest Users:',youngest)
        print('Most common age of Users:',common)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        x=input('Do you want to see the raw data ? Type: yes or no.\n').lower()
        index=0
        while x == "yes":
            print(df.iloc[index:index+5])
            index+=5
            x=input('Do you want to print more raw data ? Type: yes or no.\n').lower()
            if x == 'no':
                break



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
