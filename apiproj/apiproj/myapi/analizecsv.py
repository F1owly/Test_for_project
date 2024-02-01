import apiproj.wsgi
from myapi.models import Room
import pandas as pd

MyModel = Room

rooms = MyModel.objects.all()

data = {
    'Number_of_room': [room.Number_of_room for room in rooms],
    'Type_of_room': [room.Type_of_room for room in rooms],
}

df = pd.DataFrame(data, dtype=int)

df0 = df.loc[df['Type_of_room'] == 0].reset_index()['Number_of_room'].dropna()
df1 = df.loc[df['Type_of_room'] == 1].reset_index()['Number_of_room'].dropna()
df2 = df.loc[df['Type_of_room'] == 2].reset_index()['Number_of_room'].dropna()
df3 = df.loc[df['Type_of_room'] == 3].reset_index()['Number_of_room'].dropna()
df4 = df.loc[df['Type_of_room'] == 4].reset_index()['Number_of_room'].dropna()
df5 = df.loc[df['Type_of_room'] == 5].reset_index()['Number_of_room'].dropna()

df_result = pd.concat([df0, df1, df2, df3, df4, df5], axis=1)

df_result.columns = ['0', '1', '2', '3', '4', '5']

df_result.loc[len(df_result.index)] = [df_result['0'].value_counts().sum(),
                                         df_result['1'].value_counts().sum(),
                                         df_result['2'].value_counts().sum(),
                                         df_result['3'].value_counts().sum(),
                                         df_result['4'].value_counts().sum(),
                                         df_result['5'].value_counts().sum()]

df_result['Total'] = pd.Series(dtype='int')

df_result.loc[len(df_result.index) - 1, 'Total'] = df_result.sum(axis=1)[len(df_result.index) - 1]