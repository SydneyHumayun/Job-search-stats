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


def bar_chart():
    plt.bar(df["Response Type"], df["Number of Responses"], color=['red', 'steelblue', 'green', 'gray'])
    plt.title("Responses to Applications", fontsize=18)
    plt.xlabel("Response Type", fontsize=14)
    plt.ylabel("Amount of Responses", fontsize=14)
    plt.grid(False)
    plt.show()


def donut_chart():
    df.groupby(['Response Type']).sum().plot(kind='pie', y='Number of Responses', autopct='%1.0f%%',
                                             colors=['green', 'red', 'gray', 'steelblue'],
                                             title='Types of Responses')
    my_circle = plt.Circle((0,0), 0.7, color='white')
    p=plt.gcf()
    p.gca().add_artist(my_circle)
    plt.show()


# view_dataframe()
# pie_chart()
# bar_chart()
donut_chart()

