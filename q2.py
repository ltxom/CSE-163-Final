# import cse163_utils # UNCOMMENT THIS LINE IF USING MAC
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()


def combine_df():
    '''
    This function merge the review and business data and select
    the rows which business categorizes as "Restaurants",
    and write the restuarant to a new csv called
    "yelp_academic_dataset_restaurants.csv"
    '''
    business = pd.read_csv("data/yelp_academic_dataset_business.csv")
    rest = business[business['categories'].str.contains('Restaurants\
', na=False)]
    rest.to_csv("data/yelp_academic_dataset_restaurants.csv\
", index=False, header=True)


def attributes(df):
    '''
    This functions takes in the restuarant data,
    filters columns that are attributes and stars,
    and drop NA.
    Return the filtered dataframe
    '''
    cols = [c for c in df.columns if "attributes" in c.lower()]
    cols.append("stars")
    df = df[cols]
    return df


def compare_attribute(df):
    '''
    Takes in a dataframe with all attributes and
    filtered to the main attributes that has valid data
    And plot the graph to show the correlation between
    stars and these attributes
    '''
    data = pd.DataFrame()
    for c in df.columns:
        if df[c].isna().sum() < 1500:
            data[c] = df[c]
    data = data.dropna()
    return data


def plot(df):
    # atts = df.loc[:, df.columns != 'stars']
    # names = list(atts.columns.values)
    # df.plot(x='stars', y=names, kind='bar')
    df_dict = df.to_dict('index')
    temp = {}
    i = 0
    for k in df_dict:
        temp[i] = {"attribute": "attributes.Price Range", 'star\
': df_dict[k]["stars"], "condition": df_dict[k]["attributes.Price Range"]}
        i += 1
        temp[i] = {"attribute": "attributes.Accepts Credit Cards", 'star\
': df_dict[k]["stars"], "condition": str(df_dict[k]["attributes.\
Accepts Credit Cards"]).lower()}
        i += 1
        temp[i] = {"attribute": "attributes.Take-out", 'star': df_dict[k]["stars\
"], "condition": str(df_dict[k]["attributes.Take-out\
"]).lower() if str(df_dict[k]["attributes.Take-out"]) == "False" else "true"}
        i += 1
        temp[i] = {"attribute": "attributes.Good for Kids", 'star\
': df_dict[k]["stars"], "condition": str(df_dict[k]["attributes.Good for\
Kids"]).lower() if str(df_dict[k]["attributes.Good for Kids"]) == "False\
" else "true"}
        i += 1
        temp[i] = {"attribute": "attributes.Attire", 'star\
': df_dict[k]["stars"], "condition": df_dict[k]["attributes.Attire"]}
        i += 1
        temp[i] = {"attribute": "attributes.Good For Groups", 'star\
': df_dict[k]["stars"], "condition": str((df_dict[k]["attributes.Good For\
Groups"])).lower() if str(df_dict[k]["attributes.Good For Groups"]) == "\
False" else "true"}
        i += 1
    temp = pd.DataFrame.from_dict(temp, 'index')
    temp = temp.groupby(['attribute', 'condition'])['star\
'].agg('mean').to_dict()
    d_1 = {}
    d_2 = {}
    d_3 = {}
    i = 0
    for k in temp:
        if (k[1] == 'true' or k[1] == 'false') and not k[1] == '{}':
            d_1[i] = {"attribute": k[0], 'star': temp[k], "condition": k[1]}
            i += 1
        if k[0] == 'attributes.Attire':
            d_2[i] = {"attribute": k[0], 'star': temp[k], "condition": k[1]}
            i += 1
        if k[0] == 'attributes.Price Range':
            d_3[i] = {"attribute": k[0], 'star': temp[k], "condition\
": int(k[1]) * "\$"}
            i += 1
    plt_1 = pd.DataFrame.from_dict(d_1, 'index')
    plt_2 = pd.DataFrame.from_dict(d_2, 'index')
    plt_3 = pd.DataFrame.from_dict(d_3, 'index')
    sns.set_palette("pastel")
    sns.catplot(x="attribute", y="star", hue="condition\
", data=plt_1, legend=True, kind="bar", height=10, aspect=1)

    plt.title('Have or Have not Attributes to Stars Correlations')
    plt.xlabel('attributes')
    plt.ylabel('stars')
    plt.savefig('result/att1.png', bbox_inches='tight')

    sns.catplot(x="attribute", y="star", hue="condition\
", data=plt_2, legend=True, kind="bar", height=5, aspect=1)

    plt.title('Attire to Stars Correlations')
    plt.xlabel('Attire')
    plt.ylabel('stars')
    plt.savefig('result/att2.png', bbox_inches='tight')

    sns.catplot(x="attribute", y="star", hue="condition\
", data=plt_3, legend=True, kind="bar", height=10, aspect=1)

    plt.title('Price Range to Stars Correlation')
    plt.xlabel('Price Range')
    plt.ylabel('stars')
    plt.savefig('result/att3.png', bbox_inches='tight')


def main():
    # combine_df() # UNCOMMENT THIS LINE FIRST TIME RUNNING
    rest_data = pd.read_csv("data/yelp_academic_dataset_restaurants.csv")
    filtered = attributes(rest_data)
    data = compare_attribute(filtered)
    plot(data)


if __name__ == "__main__":
    main()
