import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
  

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    index = df['race']
    race_count=pd.Series(index).value_counts()
    

    # What is the average age of men?
    male_data=df[df['sex']=='Male']
    men = male_data['age'].mean()
    average_age_men=round(men,1)

    # What is the percentage of people who have a Bachelor's degree?
    count_edu=df['education'].count()
    select_bachelor=df[df['education']=='Bachelors']
    count_bachelor=select_bachelor['education'].count()
    bachelor=(count_bachelor/count_edu)*100
    percentage_bachelors = round(bachelor,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    advance=df[df['education'].isin(['Bachelors','Masters','Doctorate'])]
    only=advance['salary'].count()
    money=advance[advance['salary']=='>50K']
    dollars=money['salary'].count()
    
    
    higher_education =(dollars/only)*100

    not_advance=df[~df['education'].isin(['Bachelors','Masters',
                                      'Doctorate'])]
    all=not_advance['salary'].count()
    paisa=not_advance[not_advance['salary']=='>50K']
    how=paisa['salary'].count()



  
    lower_education = (how/all)*100

    # percentage with salary >50K
    higher_education_rich = round(higher_education,1) 
    lower_education_rich = round(lower_education,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    
    least=df[df['hours-per-week']==1]
    per_week=least['hours-per-week'].count()
    mini=df[(df['hours-per-week']==df['hours-per-week'].min()) & (df['salary']=='>50K')]
    nini=mini['hours-per-week'].count()
    
    num_min_workers = (nini/per_week)*100

    rich_percentage = round(num_min_workers,1)

    # What country has the highest percentage of people that earn >50K?
    
  
    filtered_df = df[df['salary'] == '>50K']


    country_stats = filtered_df.groupby('native-country').size() / df.groupby('native-country').size() * 100


    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(country_stats.max(), 1)


    # Identify the most popular occupation for those who earn >50K in India.
    popu=df[df['salary']=='>50K']
    indi=popu[popu['native-country']=='India']
    occu=indi['occupation'].value_counts()
        
    top_IN_occupation = occu.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
