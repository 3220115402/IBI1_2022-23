import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir('.')

covid_data = pd.read_csv("full_data.csv")
covid_data.head(5)
covid_data.info()
covid_data.describe()
print('\n')

for index, value in covid_data.iloc[range(0,1000,100),1].iteritems():
    print(value)
print('\n')

afghanistan_bool = covid_data.loc[:,"location"] == "Afghanistan"
afghanistan_data = covid_data.loc[afghanistan_bool,"total_cases"]
print('All rows corresponding to Afghanistan:')
for index, value in afghanistan_data.iteritems():
    print(value)
print('\n')

new_data = covid_data[covid_data["date"] == "2020-03-31"][["location", "new_cases", "new_deaths"]]
mean_new_cases = np.mean(new_data["new_cases"])
mean_new_deaths = np.mean(new_data["new_deaths"])
print("Mean new cases on 31 March 2020:", mean_new_cases)
print("Mean new deaths on 31 March 2020:", mean_new_deaths)
proportion_new_deaths = mean_new_deaths / mean_new_cases
print("Proportion of new deaths as a proportion of new cases on 31 March 2020:", proportion_new_deaths)
print('\n')

new_cases = covid_data.loc[covid_data["date"]=="2020-03-31","new_cases"].values
new_deaths = covid_data.loc[covid_data["date"]=="2020-03-31","new_deaths"].values
plt.boxplot([new_cases, new_deaths])
plt.title("New Cases and Deaths on March 31, 2020")
plt.xticks([1, 2], ["New Cases", "New Deaths"])
plt.ylabel("Number of Cases/Deaths")
plt.show()

world_data = covid_data[["date", "new_cases", "new_deaths"]]
grouped_data = world_data.groupby("date").sum()
plt.figure(figsize=(15,8))
plt.plot(grouped_data.index, grouped_data["new_cases"], label="New Cases")
plt.plot(grouped_data.index, grouped_data["new_deaths"], label="New Deaths")
plt.xlabel("Date")
plt.ylabel("Number of Cases/Deaths")
plt.xticks(fontsize=8,rotation=90)
plt.title("New Cases and New Deaths Worldwide over Time")
plt.legend()
plt.show()

filtered_data = covid_data[(covid_data["total_cases"] > 10000) & (covid_data["date"] == "2020-03-31")]
print("Locations with more than 10,000 total infections as of 31 March:")
print(filtered_data["location"].unique())