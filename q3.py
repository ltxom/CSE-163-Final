import cse163_utils # UNCOMMENT THIS LINE IF USING MAC
import pandas as pd
import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt

def Question3(data, geodata):
    data = data.loc[:, ['state', 'stars', 'categories']]
    data = data.dropna(subset=["categories"], how="all")
    data = data[data['categories'].str.contains('Restaurants')]
    data = data[(data['categories'].str.contains(';'))]
    for row in data.itertuples():
        data.at[row.Index, 'categories'] = data.at[row.Index, '\
categories'].split(";")[0]
    # Creating separate datasets for each state
    new_df = data.groupby(['state', 'categories'])['stars'].agg(['mean'])
    states_cate_star_count = data.groupby(['state', 'categories\
'])['stars'].agg(['count'])
    new_df['count'] = states_cate_star_count['count']
    new_df.to_csv("new_df.csv", header=True, index=True)
    new_df = pd.read_csv("new_df.csv")
    # Planning to create a column using these datasets and putting them into
    # find avg ratings per category.

    # avgStateRatings = data.groupby('state')['stars'].mean()
    merged = geodata.merge(new_df, left_on='STATE_ABBR', right_on='state')
    fig, ax = plt.subplots(1)
    geodata.plot(ax=ax, color='#AAAAAA', figsize=(10, 10))
    merged.plot(column='mean', legend=True, ax=ax)
    plt.title('Average Rating')
    plt.savefig('result/q3.png')

    state_AZ = new_df[new_df["state"] == "AZ"]
    state_AZ = state_AZ.sort_values(by=['count']).head(10)
    state_EDH = new_df[new_df["state"] == "EDH"]
    state_EDH = state_EDH.sort_values(by=['count']).head(10)
    state_ELN = new_df[new_df["state"] == "ELN"]
    state_ELN = state_ELN.sort_values(by=['count']).head(10)
    state_FIF = new_df[new_df["state"] == "FIF"]
    state_FIF = state_FIF.sort_values(by=['count']).head(10)
    state_GA = new_df[new_df["state"] == "GA"]
    state_GA = state_GA.sort_values(by=['count']).head(10)
    state_KHL = new_df[new_df["state"] == "KHL"]
    state_KHL = state_KHL.sort_values(by=['count']).head(10)
    state_MLN = new_df[new_df["state"] == "MLN"]
    state_MLN = state_MLN.sort_values(by=['count']).head(10)
    state_NV = new_df[new_df["state"] == "NV"]
    state_NV = state_NV.sort_values(by=['count']).head(10)
    state_ON = new_df[new_df["state"] == "ON"]
    state_ON = state_ON.sort_values(by=['count']).head(10)
    state_WI = new_df[new_df["state"] == "WI"]
    state_WI = state_WI.sort_values(by=['count']).head(10)
    state_XGL = new_df[new_df["state"] == "XGL"]
    state_XGL = state_XGL.sort_values(by=['count']).head(10)

    sns.catplot(x="state", y="mean", hue="categories", data=state_AZ, legend=True, kind="bar", height=10)
    plt.title("Rating of Each Category")
    plt.savefig('result/AZ.png')



def Find_Avg_Ratings_Per_Cat(data):
    data['types'] = data['categories'].str.split(';')
    series = data.groupby('types')['stars'].mean()
    return series.max()


def main():
    sns.set()
    geodata = gpd.read_file('data/states/states.shp')
    data = pd.read_csv('data/yelp_academic_dataset_business.csv')
    Question3(data, geodata)


if __name__ == '__main__':
    main()
