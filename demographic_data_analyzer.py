import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    dda = pd.read_csv('adult.data.csv')   

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = dda.groupby('race')['race'].count().sort_values(ascending = False)

    # What is the average age of men?
    average_age_men = round(dda.loc[dda['sex']=='Male', 'age'].mean(), 1)
  
    # What is the percentage of people who have a Bachelor's degree?
    df = pd.DataFrame(dda,columns=['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','salary'])
    number_of_people = len(df.index)       
    number_of_bachelors = dda.loc[dda['education']=='Bachelors'].shape[0]
    percentage_bachelors = round(number_of_bachelors/number_of_people * 100 ,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = dda.loc[((dda['education']=='Bachelors') | (dda['education']=='Masters') | (dda['education']=='Doctorate'))].shape[0]
    lower_education = number_of_people - higher_education

    # percentage with salary >50K
    higher_education_table = dda.loc[((dda['education']=='Bachelors') | (dda['education']=='Masters') | (dda['education']=='Doctorate'))]
    higher_amount = higher_education_table.loc[(higher_education_table['salary'] == '>50K')].shape[0]
    higher_education_rich = round(higher_amount/higher_education*100,1)
    
    lower_education_table = dda.loc[((dda['education']!='Bachelors') & (dda['education']!='Masters') & (dda['education']!='Doctorate'))]
    lower_education_rich = lower_education_table.loc[(lower_education_table['salary'] == '>50K')].shape[0]
    lower_education_rich = round(lower_education_rich/lower_education*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = dda['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = dda.loc[(dda['hours-per-week']==min_work_hours)].shape[0]
    num_min_workers_table = dda.loc[(dda['hours-per-week']==min_work_hours)]
    num_min_workers_rich_amount = num_min_workers_table.loc[(num_min_workers_table['salary'] == '>50K')].shape[0]
    rich_percentage = num_min_workers_rich_amount/num_min_workers*100

    # What country has the highest percentage of people that earn >50K?
    rich_people = dda.loc[(dda['salary'] == '>50K')]
    rich_people_with_country = rich_people.groupby('native-country')['native-country'].count()
    people_with_country = dda.groupby('native-country')['native-country'].count()
    answer_full = (rich_people_with_country/people_with_country).sort_values(ascending = False).head(1)
    answer_app = pd.DataFrame(answer_full)
    for idx in answer_app.index:
         highest_earning_country = (idx)
    
    highest_earning_country_percentage = round(answer_full.values[0]*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    condition_table = dda.loc[(dda['salary'] == '>50K') & (dda['native-country'] == "India")]
    solution = condition_table.groupby('occupation')['occupation'].count().sort_values(ascending = False).head(1)
    sol = pd.DataFrame(solution, columns=['occupation'])
    for idx in sol.index:
        top_IN_occupation = (idx)

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
