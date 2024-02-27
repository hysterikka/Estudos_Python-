#Use the data to complete the following tasks:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column.
df = pd.read_csv('fcc-forum-pageviews.csv')
df ['date'] = pd.to_datetime (df['date'])
df = df.set_index('date')
#Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df.loc[(df['value'] >= df ['value'].quantile(0.025))& df['value']<= df ['value'].quantile(0.975))]

#Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". 
def draw_line_plot():
  fig,ax = plt.subplots (figsize = (32,10), dpi =100)
  #The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the y axis should be Page Views.
ax.settitle('Daily freeCodeCamp Forum Page Views 5/2016-12/2019"')
ax.set_xlabel('Date')
ax.set_ylabel ('Page Views')
sns.lineplot(data=df, legend = False)
#Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png".
dig.savefig ('line_plot.png')
return fig

def draw_bar_plot ():
  df_bar =df.copy()
df_bar ['Years'] = df_bar.index.year
df_bar ['Months'] = df_bar.index.month_name()
df_bar = pd.DataFrame (df_bar.groupby(['Years', 'Months'], sort = False)['value'].mean().round().astype(int))
df_bar = df_bar.rename(columns = {'value':'Average Page Views'})
df_bar = df_bar.reset_index ()
missing_data= {
  "Years":[2016, 2016,2016, 2016],
  "Months": ['Janyary', "February", 'March', 'April'],
  "Average Page Views": [0,0,0,0]
}
#It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of Months. On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.
df_bar = pd.concat([pd.DataFrame(missing_data), df_bar])
fig,ax = plt.subplots(figsize = (19.2, 10.8), dpi = 100)
ax.set_title ('Daily freeCodeCamp Forum A per Month')
#Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png"
chart = sns.barplot(data=df_bar, x = 'Years', y = 'verage Page Views', hue = 'Months', palette = 'tab10')
chart.set_xticklabels(chart.get_xticklabels (), rotation = 90, horizontalaligment = 'center')
fig.savefig ('bar_plot.png')

#These box plots should show how the values are distributed within a given year or month and how it compares over time. 

def draw_box_plot ():
  df_box = df.copy ()
  df_box = df.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box ['months'] = [d.strftime ('%b') for d in df_box.date]
  fig,axes = plt.subplots (1,2,figsize=(32,10), dpi = 100)
#The title of the first chart should be Year-wise Box Plot (Trend) and the title of the second chart should be Month-wise Box Plot (Seasonality). 
  sns.boxplot(data = df_box, x='year', y='value', ax = axes [0])
  axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
#Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly. The boilerplate includes commands to prepare the data.
  month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(data=df_box, x="month", y="value", order=month_order, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

