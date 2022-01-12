import time
import pandas as pd
import numpy as np
#this declares the data lists for the program
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
Month_list = ["january","febraury","march","april",",may", "june","all" ]
day_list = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday","all"]


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
    city = input ("What city would you like to explore? chicago, new york or washington?" ).lower().strip()
    while city not in CITY_DATA:
        print("oops! that's not a valid input")
        city = input ("What city would you like to explore? chicago, new york or washington?" ).lower().strip()
        continue

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input ("What month would you like to explore?" ).lower().strip()
    while month not in Month_list:
        print("oops! that's not a valid input")
        month = input ("What month would you like to explore?" ).lower().strip()
        continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input ("What day would you like to explore?" ).lower().strip()
    while day not in day_list:
        print("oops! that's not a valid input")
        day = input ("What day would you like to explore?" ).lower().strip()
        continue
       
    return city, month,day

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

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start month:', popular_month)
    print('Most Popular Start day of the week:', popular_day_of_week)
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    popular_Start_Station = df['Start Station'].mode()[0]

    print('Most Popular Start Station:', popular_Start_Station)

    # TO DO: display most commonly used end station
    popular_End_Station = df['End Station'].mode()[0]

    print('Most Popular End Station:', popular_End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    df["combo"] = df['Start Station'] + "to"+ df['End Station']
    popular_combo =   df["combo"].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    
    print(total_travel_time)
    print(mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()

        print(gender_count)
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_bith_year = df['Birth Year'].min()
        most_recent_bith_year = df['Birth Year'].max()
        most_common_bith_year = df['Birth Year'].mode()[0]
 
        print("earliest birth year:", earliest_bith_year)
        print("most_recent_bith_year:", most_recent_bith_year)
        print("most_common_bith_year:", most_common_bith_year)
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def nextfive(df):
    #this returns five rows at the request of the user
    display_five = input ("Do you want to see the next five rows? yes or no").lower().strip()
    start = 0
    end = 5
    while display_five == 'yes':
        print(df.iloc[start:end,:])
        start+= 5
        end+= 5
        display_five = input("Do you wish to continue?: ").lower()
    
    
def main():
    #this calls all other functions and establish sequence of the codes
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)                                                                                                                     
        user_stats(df)
        nextfive(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
