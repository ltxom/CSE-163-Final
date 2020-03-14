import pandas as pd
import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    sns.set()
    geodata = gpd.read_file('states.shp')
    data = pd.read_csv('yelp_academic_dataset_business.csv')
    Question3(data, geodata)


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
    data = data[:, ['state', 'stars', 'categories']]
    data = data['Restuarants' in data['categories']]
    # Creating separate datasets for each state
    Alabama = data[(data['state'] == 'AL')]
    Alaska = data[(data['state'] == 'AK')]
    Arizona = data[(data['state'] == 'AZ')]
    Arkansas = data[(data['state'] == 'AR')]
    California = data[(data['state'] == 'CA')]
    Colorodo = data[(data['state'] == 'CO')]
    Connecticut = data[(data['state'] == 'CT')]
    Delaware = data[(data['state'] == 'DE')]
    Florida = data[(data['state'] == 'FL')]
    Georgia = data[(data['state'] == 'GA')]
    Hawaii = data[(data['state'] == 'HI')]
    Idaho = data[(data['state'] == 'ID')]
    Illinois = data[(data['state'] == 'IL')]
    Indiana = data[(data['state'] == 'IN')]
    Iowa = data[(data['state'] == 'IA')]
    Kansas = data[(data['state'] == 'KS')]
    Kentucky = data[(data['state'] == 'KY')]
    Louisiana = data[(data['state'] == 'LA')]
    Maine = data[(data['state'] == 'ME')]
    Maryland = data[(data['state'] == 'MD')]
    Massachusetts = data[(data['state'] == 'MA')]
    Michigan = data[(data['state'] == 'MI')]
    Minnesota = data[(data['state'] == 'MN')]
    Mississippi = data[(data['state'] == 'MS')]
    Missouri = data[(data['state'] == 'MO')]
    Montana = data[(data['state'] == 'MT')]
    Nebraska = data[(data['state'] == 'NE')]
    Nevada = data[(data['state'] == 'NV')]
    NewHampshire = data[(data['state'] == 'NH')]
    NewJersey = data[(data['state'] == 'NJ')]
    NewMexico = data[(data['state'] == 'NM')]
    NewYork = data[(data['state'] == 'NY')]
    NorthCarolina = data[(data['state'] == 'NC')]
    NorthDakota = data[(data['state'] == 'ND')]
    Ohio = data[(data['state'] == 'OH')]
    Oklahoma = data[(data['state'] == 'OK')]
    Oregon = data[(data['state'] == 'OR')]
    Pennsylvania = data[(data['state'] == 'PA')]
    RhodeIsland = data[(data['state'] == 'RI')]
    SouthCarolina = data[(data['state'] == 'SC')]
    SouthDakota = data[(data['state'] == 'SD')]
    Tennessee = data[(data['state'] == 'TN')]
    Texas = data[(data['state'] == 'TX')]
    Utah = data[(data['state'] == 'UT')]
    Vermont = data[(data['state'] == 'VT')]
    Virginia = data[(data['state'] == 'VA')]
    Washington = data[(data['state'] == 'WA')]
    WestVirginia = data[(data['state'] == 'WV')]
    Wisconsin = data[(data['state'] == 'WI')]
    Wyoming = data[(data['state'] == 'WY')]
    # Planning to create a column using these datasets and putting them into
    # find avg ratings per category.
    avgStateRatings = data.groupby('state')['stars'].mean()
    merged = geodata.merge(avgStateRatings, left_on='STATE_ABBR',
                           right_on='state')
    fig, ax = plt.subplots(1)
    geodata.plot(ax=ax, color='#AAAAAA')
    merged.plot(column='stars', legend=True, ax=ax)
    plt.savefig('temp.png')


def Find_Avg_Ratings_Per_Cat(data):
    data['types'] = data['categories'].str.split(';')
    series = data.groupby('types')['stars'].mean()
    return series.max()


if __name__ == '__main__':
    main()
