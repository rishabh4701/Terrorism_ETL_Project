# Analyzing Global Terrorism

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://rishabh4701-terrorism-etl-project-app-4lfdz3.streamlit.app/)

## What This Is

Hey there! This is my first major data analysis project. I wanted to take a large, messy, real-world dataset and see if I could handle the entire process from start to finish: cleaning the data, finding interesting patterns, and building something cool to show my findings.

I chose the Global Terrorism Database (GTD), which has over 180,000 records of terrorist events. My goal was to turn this massive spreadsheet into a simple, interactive dashboard that anyone could use to explore the data.



---

## What I Did

* **Cleaned Up a Huge, Messy Dataset:** I built a full **ETL pipeline** with Python and Pandas to clean all 180,000+ records. This meant dealing with lots of missing values, fixing data types, and making the data actually usable.
* **Found Interesting Trends:** I used **Seaborn** and **Matplotlib** to dig into the data. I was able to find the peak years for terrorism, identify the most targeted countries, and see which weapon types were most common.
* **Mapped the Data:** A bar chart can only tell you so much. I used **Folium** to create an interactive map showing the actual locations of attacks in India, which gave a much clearer picture of the hotspots.
* **Built a Live Dashboard:** I used **Streamlit** to build a simple web app from my analysis. It lets you filter the data by country and see the top affected regions instantly.

---

## Tech I Used

* Python
* Pandas
* Seaborn & Matplotlib
* Folium
* Streamlit
* VS Code

---

## Want to Run It Yourself?

You can run the dashboard on your own machine. Here's how:

### Prerequisites

You'll need Python installed.

### Get It Running

1.  Clone this repository:
    ```sh
    git clone [https://github.com/rishabh4701/Terrorism_ETL_Project.git](https://github.com/rishabh4701/Terrorism_ETL_Project.git)
    ```
2.  Go into the project folder:
    ```sh
    cd Your-Repository-Name
    ```
3.  Install all the libraries it needs:
    ```sh
    pip install -r requirements.txt
    ```
4.  Launch the app:
    ```sh
    streamlit run app.py
    ```
That's it! It should open in your web browser.

---

##  Acknowledgments

* This whole project was only possible because of the amazing work from the team at the **National Consortium for the Study of Terrorism and Responses to Terrorism (START)**. You can find the data they provide on [Kaggle](https://www.kaggle.com/datasets/START-UMD/gtd).