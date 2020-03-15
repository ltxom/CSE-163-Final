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
    # Mean dataframe which computes the average rating for each state
    # (Excluding Georgia since there is only one review)
    temp = data[data['state'] != 'GA']
    mean_df = temp.groupby('state')['stars'].agg(['mean'])

    # Dataframe grouping based on state and categories, creating a new column
    # for the mean of each category and its ratings.
    new_df = data.groupby(['state', 'categories'])['stars'].agg(['mean'])
    states_cate_star_count = data.groupby(['state', 'categories\
'])['stars'].agg(['count'])
    new_df['count'] = states_cate_star_count['count']
    # Saving dataframe into a csv and re-reading to make state and categories
    # as separate columns
    new_df.to_csv("new_df.csv", header=True, index=True)
    new_df = pd.read_csv("new_df.csv")
    # Joining the geography of US with the mean dataframe which includes the
    # average ratings of each state.
    merged = geodata.merge(mean_df, left_on='STATE_ABBR', right_on='state')
    # Plotting the merged dataframe and blank US map on the same axis
    fig, ax = plt.subplots(1)
    geodata.plot(ax=ax, color='#AAAAAA', figsize=(10, 10))
    merged.plot(column='mean', legend=True, ax=ax)
    plt.title('Average Rating By State')
    plt.axis([-130, -65, 20, 55])
    plt.savefig('result/q3.png')
    # Creating separate individual dataframes for each state.
    # (Excluding Georgia since there is only one review)
    state_AZ = new_df[new_df["state"] == "AZ"]
    state_AZ = state_AZ.sort_values(by=['count']).head(10)
    state_NV = new_df[new_df["state"] == "NV"]
    state_NV = state_NV.sort_values(by=['count']).head(10)
    state_WI = new_df[new_df["state"] == "WI"]
    state_WI = state_WI.sort_values(by=['count']).head(10)
    # Arizona Categories
    sns.catplot(x="state", y="mean", hue="categories", data=state_AZ,
                legend=True, kind="bar", height=10)
    plt.title("Rating of Each Category in Arizona")
    plt.savefig('result/AZ.png')
    # Nevada Categories
    sns.catplot(x="state", y="mean", hue="categories", data=state_NV,
                legend=True, kind="bar", height=10)
    plt.title("Rating of Each Category in Nevada")
    plt.savefig('result/NV.png')
    # Wisconsin Categories
    sns.catplot(x="state", y="mean", hue="categories", data=state_WI,
                legend=True, kind="bar", height=10)
    plt.title("Rating of Each Category in Wisconsin")
    plt.savefig('result/WI.png')


def main():
    sns.set()
    geodata = gpd.read_file('data/states/states.shp')
    data = pd.read_csv('data/yelp_academic_dataset_business.csv')
    Question3(data, geodata)


if __name__ == '__main__':
    main()
