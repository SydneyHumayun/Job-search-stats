import pandas as pd
import matplotlib.pyplot as plt

# create data frame
df = pd.DataFrame({'Response Type': ["No", "Viewed, No Response", "Next Stage", "No Response"],
                    'Number of Responses': [41, 15, 4, 114]})
# view Data frame


def view_dataframe():
    print(df)


def pie_chart():
    df.groupby(['Response Type']).sum().plot(kind='pie', y='Number of Responses', autopct='%1.0f%%',
                                        colors=['green', 'red', 'gray', 'steelblue'],
                                        title='Types of Responses')
    plt.show()


view_dataframe()
pie_chart()

