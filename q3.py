import cse163_utils # UNCOMMENT THIS LINE IF USING MAC
import pandas as pd
import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt

"""
def Question1(data):
    data = data[:, ['attributes.Music.dj', 'attributes.Music.playlist',
                'attributes.Music.video', 'attributes.Music.karaoke',
                    'attributes.Music.background_music',
                    'attributes.Music.live', 'stars']]
    data.fillna('FALSE')
    dj = data[:, 'attributes.Music.dj', 'stars']
    playlist = data[:, 'attributes.Music.playlist', 'stars']
    video = data[:, 'attributes.Music.video', 'stars']
    karaoke = data[:, 'attributes.Music.karaoke', 'stars']
    background = data[:, 'attributes.Music.background_music']
    live = data[:, 'attributes.Music.live']
    stars = data[:, 'stars']
    djModel = learn(dj, stars)
    playlistModel = learn(playlist, stars)
    videoModel = learn(video, stars)
    karaokeModel = learn(karaoke, stars)
    backgroundModel = learn(background, stars)
    liveModel = learn(live, stars)
    djModel['type'] = 'dj'
    playlistModel['type'] = 'playlist'
    videoModel['type'] = 'video'
    karaokeModel['type'] = 'karaoke'
    backgroundModel['type'] = 'background'
    liveModel['type'] = 'live'

    final = pd.concat([djModel, playlistModel, videoModel, karaokeModel,
    backgroundModel, liveModel])
    print(final)


def learn(data, stars):
    data.get_dummies()
    x_train, x_test, y_train, y_test = train_test_split(data, stars,
                                                        test_size=0.2)
    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)
    y_test_predict = model.predict(x_test)
    print(accuracy_score(y_test, y_test_predict))
    return model
"""


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

    # Planning to create a column using these datasets and putting them into
    # find avg ratings per category.

    # avgStateRatings = data.groupby('state')['stars'].mean()
    merged = geodata.merge(new_df, left_on='STATE_ABBR', right_on='state')
    fig, ax = plt.subplots(1)
    geodata.plot(ax=ax, color='#AAAAAA')
    merged.plot(column='mean', legend=True, ax=ax)
    plt.savefig('result/q3.png')


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
