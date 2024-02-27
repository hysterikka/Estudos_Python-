import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("medical_examination.csv")
#Create a chart similar to examples/Figure_1.png, where we show the counts of good and bad outcomes for the cholesterol, gluc, alco, active, and smoke variables for patients with cardio=1 and cardio=0 in different panels.

#Use the data to complete the following tasks in medical_data_visualizer.py:

#Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
df ['overweight'] = df['weight')]/((df["height"]/100)**2)
df.loc [df['overweight'] >= 25, 'overweight'] = 1
df.loc [df['overweight']!=1 , 'overweight'] = 0
#Normalize the data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc [df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc [df['cholesterol']>1, 'cholesterol'] = 1
df.loc [df['gluc'] == 1, 'gluc'] = 0
df.loc [df['gluck'] > 1, 'gluc'] =1
#Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's catplot(). The dataset should be split by 'Cardio' so there is one chart for each cardio value. The chart should look like examples/Figure_1.png.
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = 'cardio', var_name = 'variable', value_vars = ['alco', 'active','cholesterol', 'gluc', 'overweight','smoke'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = pd.melt(df, var_name = 'variable', value_vars = ['active','alco','cholesterol', 'gluc','overweight','smoke'], id_vars = 'cardio')

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(data=df_cat, kind="count",  x="variable",hue="value", col="cardio").set_axis_labels("variable", "total")
    fig = fig.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig
#Clean the data. 
   def draw_heat_map
  #Filter out the following patient segments that represent incorrect data:
#diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
  df_heat = df [(df(df['ap_lo'] <= df['ap_hi']) &

#height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
(df ['height']<= df ['height'].quantile (0.025))&
#height is more than the 97.5th percentile
(df ['height']<= df ['height'].quantile (0.975))&
#weight is less than the 2.5th percentile
(df ['weight']<= df ['height'].quantile (0.025))&
#weight is more than the 97.5th percentile
(df ['weight']<= df ['height'].quantile (0.0.975))
                 ]
#Create a correlation matrix using the dataset. 
corr = df_heat.corr ()
#Plot the correlation matrix using seaborn's heatmap().
#Mask the upper triangle. The chart should look like examples/Figure_2.png.
mask = np.triu(corr)
fig, ax = plt.subplots(figsize =(7,5))
#Any time a variable is set to None, make sure to set it to the correct code.
sns.heatmap (corr, mask = mask, fmt ='1f', vmax = .3, linewidths =.5, square = True, cbar_kms = {'shrink':0.5}, annot = True, center = 0)
fig.savefig ('heatmap.png')
return fig
