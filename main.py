import pandas as pd
import matplotlib.pyplot as plt

# Reading files
path = "medallists.csv"
df = pd.read_csv(path)
headdata = df.head()
summary = df.describe()


def aboutdata():
    print(headdata)
    print(summary)
    return "checked"


def createplots():
    # PLOT 1
    country_medals = df.groupby("country").size()

    country_medals = country_medals[country_medals > 0]

    plt.figure(figsize=(20, 6))
    plt.bar(country_medals.index, country_medals, color="blue")

    plt.xlabel("Country")
    plt.ylabel("Total Number of Medals Won")
    plt.title("Medals won per country")

    plt.grid(True)
    plt.minorticks_on()
    plt.grid(which="major", linestyle="-", linewidth=0.4)
    plt.grid(which="minor", linestyle=":", linewidth=0.4)

    plt.xticks(rotation=90)

    plt.savefig("medals_per_country.png")

    # PLOT 2
    medal_counts = df.groupby("medal_date").size()

    plt.figure(figsize=(20, 6))
    medal_counts.plot()
    medal_counts.plot(marker="o")
    plt.xlabel("Date")
    plt.ylabel("Total Number of Medals Won")
    plt.title("Number of Medals Won Over Time")
    plt.grid(True)

    plt.minorticks_on()
    plt.grid(which="major", linestyle="-", linewidth=0.7)
    plt.grid(which="minor", linestyle=":", linewidth=0.7)

    plt.savefig("medals_over_time.png")
    return "checked"


def createsummary():
    with open("summary_report.md", "w", encoding="utf-8") as file:
        file.write("""# Mini Project: Pandas Descriptive Statistics\n\n""")
        file.write("""Adil Keku Gazder <br>""")
        file.write(""" ag825, adil.gazder@duke.edu <br>""")
        file.write("""IDS 706: Data Engineering Systems <br>""")
        file.write("""Duke University, Fall 2024\n\n""")
        file.write(
            """The aim with this project was to read a .csv file and generate summary statistics and plots describing the data. The dataset used for this project was acquired from Kaggle (Olympic Summer Games - Paris 2024 -> medallists.csv) <br>"""
        )
        file.write(
            """\n\nLink to the dataset: (https://www.kaggle.com/datasets/muhammadehsan02/olympic-summer-games-paris-2024?select=medallists.csv)\n\n"""
        )
        file.write("## Head of dataset used:\n")
        file.write(headdata.to_markdown())
        file.write("\n\n## Summary Statistics:\n")
        file.write(summary.to_markdown())
        file.write(
            "\n\n## Distribution of total medals achieved totally over each day of the olympics\n"
        )
        file.write("![Data Visualization](medals_over_time.png)")
        file.write("\n\n## Distribution of total medals achieved per each country\n")
        file.write("![Data Visualization](medals_per_country.png)")
        return "checked"


if __name__ == "__main__":
    aboutdata()
    createplots()
    createsummary()
