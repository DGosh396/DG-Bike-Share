import time
import pandas as pd

CITY_DATA = {'Chicago': 'chicago.csv',
             'New York City': 'new_york_city.csv',
             'washington': 'washington.csv'}
MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
              'november', 'december']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def display_raw_data(city):
    pass


def main():
    while True:
        city, month, day = get_filters()
        print(city, month, day)

        df = load_data(city, month, day)
        print(df)

        # time_stats(df)
        # station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)


def get_filters():
    """
     Asks user to specify a city, month, and day to analyze.

     Returns:
             (str) city - name of the city to analyze
             (str) month - name of the month to filter by, or "all" to apply no month filter
             (str) day - name of the day of week to filter by, or "all" to apply no day filter
     """

    print('Hello! Let us explore some US bike_share data!')

    # TO DO:get user input for city (chicago,new york city,washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("\nwhat city would you like to filter by? New York City, Chicago, or Washington?\n").lower()
        if city not in ('new york city', 'chicago', 'washington'):
            print("Sorry, I do not understand, Please try again.")
            continue
        else:
            break

            # TO DO: get user input for month (all, January, February, ... , June)

    while True:
        month = input("\nwhat month would you like to filter by? January, February, March, April, May, June or type all if you do not have any preference.\n")
        if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
            print("Sorry, I do not understand, Please try again.")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, Monday, Tuesday, ... Sunday)

    while True:
        day = input("\nwhat day are you looking for? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type all if you do not have any preference.\n")
        if day not in ('all', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
          print("Sorry, I do not understand, Please try again.")
          continue
        else:
            break

            print('-' * 40)
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

    # TO DO: display the most common month

    popular_month = df[month], mode()[0]
    print('Common Month:', popular_month)

    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('Common Day:', popular_day)

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Common Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

    # TO DO: display most commonly used start station

    start_station = df['start_station'].value_counts().idxmax()
    print('Most used start station:', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End_Station'].value_counts().idxmax()
    print('\nMost used end station:', end_station)

    # TO DO: display most frequent combination of start station and end station trip

    combination_station = df.groupby(['Start_Station', 'End_Station']).size().idxmax()
    print('\nCommonly used combination of start station and end station trip:', start_station, " & ", end_station)

    # print("\nThis took %s seconds." % (time.time() - start_time))
    # print('-' * 40)


def trip_duration_stats(df, n=None):
    """Displays the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['trip_duration']/60
    print('total_travel_time:', Total_Travel_Time, " seconds")

    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time / 60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

    """Displays bike_share users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    # print(user_types)
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender

    try:
        gender_types = df['Gender'].value_counts()
        print('\nGender Types:\n', gender_types)
    except KeyError:
        print("\nGender Types:\nNO data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        earliest_year = df['year_of_birth'].min()
        print('\nEarliest Year:', earliest_year)
    except KeyError:
        print("\nearliest_year:\nno_data_available_for_this_month.")

    try:
        most_recent_year = df['birth_year'].max()
        print('\nmost_recent_year:', most_recent_year)
    except KeyError:
        print("\nmost_recent_year:\nNO data available for this month.")

    try:
        most_common_year = df['birth_year'].value_counts().idmxmax()
        print('\nmost_common_year:', most_common_year)
    except KeyError:
        print("\nmost_common_year:\nno_data_available_for_this_month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

    data = input('\nWould you like to display the first 5 rows of data? Type yes or no.\n').lower()
    while True:
        if data == 'no':
            break
    print(df.iloc[n:n + 5])
    input('\nWould you like to see the next 5 rows of data? Type yes or no.\n').lower()
    n += 5

    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes':

        while True:
            city, month, day = get_filters()

        time_stats(df, n)
        station_stats(df, n)
        trip_duration_stats(df, n)
        user_stats(df, n)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            main()


if __name__ == "__main__":
    main()
