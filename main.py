"""
Author: Tom Liu, Kellie Gui, Timothy Woo
Please manually download data from
1. https://www.kaggle.com/z5025122/yelp-csv#yelp_academic_dataset_business.csv
2. https://www.kaggle.com/z5025122/yelp-csv#yelp_academic_dataset_review.csv
3. https://www.arcgis.com/home/item.html?id=f7f805eb65eb4ab787a0a3e1116ca7e5
And put them into data folder
"""
import cse163_utils
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error


def minify_review_data():
    """
    This function should be run for once to
    remove the resturants comments from yelp_academic_dataset_review.csv
    to make the program faster.
    Saves the new file as yelp_academic_dataset_review_no_comments.csv
    """
    df = pd.read_csv("CSE-163-Final/data/yelp_academic_dataset_review.csv")
    df = df.drop(columns=["text"])
    df.to_csv("CSE-163-Final/data/\
yelp_academic_dataset_review_no_comments.csv", index=False, header=True)


def filter_music_columns(df):
    """
    This function takes in the dataframe of business,
    and will filter out all non-music related and the stars column
    and remove NaNs.
    Returns the filterred dataframe and is ready to be used
    in maching learning model.
    """
    cols = [c for c in df.columns if "music" in c.lower()]
    cols.append("stars")
    df = df[cols]
    cols.remove("stars")
    df = df.dropna(subset=cols, how='all')
    df = df.fillna(False)
    return df


def fit_predict_plot_music_factors(df):
    """

    """
    X = pd.get_dummies(df.loc[:, df.columns != 'stars'])
    y = df['stars']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    m = DecisionTreeRegressor()
    m = m.fit(X_train, y_train)
    X_test_new = []
    X_test_new_inverse = []
    y_test_result = []
    y_test_result_inverse = []
    for a in X_test.columns:
        X_test_new.append([])
        X_test_new_inverse.append([])
        for b in X_test.columns:
            X_test_new[len(X_test_new) - 1].append(1 if a == b else 0)
            X_test_new_inverse[len(X_test_new) - 1].append(0 if a == b else 1)
    for x in X_test_new:
        y_test_result.append(m.predict(np.array(x).reshape(1, -1))[0])
    for x in X_test_new_inverse:
        y_test_result_inverse.append(m.predict(np.array(x).reshape(1, -1))[0])
    temp = {"name": X_test.columns, "result": y_test_result, "Have": "No"}
    temp2 = {"name": X_test.columns, "result": y_test_result_inverse, "Have\
": "Yes"}
    data = pd.DataFrame(data=temp).append(pd.DataFrame(data=temp2))
    plot = sns.catplot(x="name", y="result", hue="Have\
", data=data, legend=True, kind="bar", height=10)
    plt.title("Musical Factors to Restaurants Stars Prediction")
    plt.xlabel("Attributes in a Restaurants")
    plt.xticks(rotation=7)
    plt.ylabel("Predicted Stars (1.0-5.0)")
    plt.ylim((0, 5.5))
    plt.text(0, 5, "mean squared error of the regressor model:\
" + str(mean_squared_error(y_test, m.predict(X_test)))[0:5], style='italic\
', bbox={'facecolor': 'yellow', 'alpha': 0.5, 'pad': 10})
    plt.figure(figsize=(10, 10))
    plot.savefig('result\music_prediction.png',
                 bbox_inches='tight', dpi=188)


def combine_df():
    '''
    This function takes the no comment version review
    and merge them together for question 2
    '''
    review = pd.read_csv("data\yelp_academic_dataset_review_no_comments.csv")
    business = pd.read_csv("data\yelp_academic_dataset_business.csv")
    joined_data = business.merge(review, left_on='business_id',
                    right_on='business_id', how='outer')
    # joined_data = joined_data.dropna()
    rest = joined_data['Restaurants' in joined_data.categories.str]
    print(rest.head())


def main():
    # minify_review_data() # UNCOMMENT THIS LINE FIRST TIME RUNNING
    # business_data = pd.read_csv("data\yelp_academic_dataset_business.csv")
    # review_data_mini = pd.read_csv("CSE-163-Final/data/\
    # yelp_academic_dataset_review_no_comments.csv")
    # df = business_data.merge(review_data_mini, how="outer\
    # ", left_on="business_id", right_on="business_id")
    # music_df = filter_music_columns(business_data)
    # fit_predict_plot_music_factors(music_df)
    combine_df()


if __name__ == '__main__':
    main()
