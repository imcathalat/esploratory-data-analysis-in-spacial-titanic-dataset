# %%
## preciso entender as relações entre os dados que me possam me fornecer entender o que fez um passageiro ser atirado pra fora do navio ou não

import pandas as pd 
import numpy as np 
import seaborn as sns 


initial_df = pd.read_csv('data/train.csv')

initial_df.head()


# %%
initial_df.info()
# %%

initial_df.describe()

# %%
initial_df['Transported'].value_counts()
initial_df['CryoSleep'].value_counts()
# %%

contingency_table = pd.crosstab(initial_df['CryoSleep'], initial_df['Transported'])

contingency_table

# %%

# CryoSleep Passagers Not Transported
cs_not_transported = initial_df[(initial_df['CryoSleep'] == True) & (initial_df['Transported'] == False)]
cs_not_transported

cs_not_transported_sum = cs_not_transported.shape[0]
cs_not_transported_sum

# %%
# CryoSleep Passagers Transported
cs_transported = initial_df[(initial_df['CryoSleep'] == True) & (initial_df['Transported'] == True)]
cs_transported

cs_transported_sum = cs_transported.shape[0]
cs_transported_sum

# %%

# VIP and CryoSleep Passagers Transported
vip_cs_trasported = initial_df[(initial_df['CryoSleep'] == True) & (initial_df['VIP'] == True) & (initial_df['Transported'] == True)]

print(vip_cs_trasported.shape[0])

# Not VIP and CryoSleep Passagers Transported

not_vip_cs_trasported = initial_df[(initial_df['CryoSleep'] == True) & (initial_df['VIP'] == False) & (initial_df['Transported'] == True)]

print(not_vip_cs_trasported.shape[0])

# VIP and not CryoSleep Passagers Transported

vip_not_cs_trasported = initial_df[(initial_df['CryoSleep'] == False) & (initial_df['VIP'] == False) & (initial_df['Transported'] == True)]

print(vip_not_cs_trasported.shape[0])

# %%

pd.crosstab(initial_df['Transported'], initial_df['CryoSleep']).plot(kind='bar', stacked=True)
plt.title('Relation between CryoSleep Passagers and Transported Status')
plt.xlabel('Transported')
plt.ylabel('Count')
plt.show()

# %%

num_df = initial_df.select_dtypes(include=['float64'])

sns.displot(num_df)





# %%
initial_df['HomePlanet'].value_counts()

initial_df['Destination'].value_counts()
# %%
initial_df['Cabin'].value_counts()

# %%
initial_df['Transported'].value_counts()
# %%
initial_df['CryoSleep'].value_counts()

# %%
## média das idades, média de quanto gastou

bills_travel = initial_df.set_index('PassengerId')[['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']]
bills_travel.head()

bills_travel.describe()

data = initial_df

data.head()

bills_travel.head()


# %%

bills_travel.drop(columns='BillsTravel')

bills_travel['BillsTravel'] = bills_travel.sum(axis=1)

bills_travel.head()


# %%
bills_travel['RoomService']

# %%

initial_df['Age'].describe().round(3)

# %%

count_P = initial_df['Cabin'].str.endswith('P').sum()
count_P

# %%
count_S = initial_df['Cabin'].str.endswith('S').sum()
count_S


# %%

duplicated_data = initial_df[initial_df.duplicated(['HomePlanet', 'CryoSleep', 'Cabin', 'Destination', 'Age', 'VIP', 'Name', 'Transported'])]

duplicated_data.head()

# %%

initial_df.index.is_unique

# %%

total_null = initial_df.isnull().sum().sort_values(ascending=False)
total_null
total_null.plot(kind="bar", figsize = (8, 6), fontsize = 10)

plt.xlabel("Features", fontsize = 20)
plt.ylabel("Count", fontsize = 20)
plt.title("Total Missing Values", fontsize = 20)

# %%
