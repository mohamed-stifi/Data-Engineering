import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def read_csv(path) -> pd.DataFrame:
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        ValueError(f"path [{path}] not exist.")

def print_from_df(df: pd.DataFrame, num: int, is_last = False):
    if not is_last:
        return df.head(num)
    else:
        return df.tail(num)

def descreption_of_columns(df: pd.DataFrame):
    print(df.info())
    return df.dtypes

def Separate_columns_by_dtype(df: pd.DataFrame):
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()

    # Count the types
    print(f"Numeric columns: {len(numeric_cols)}")
    print(f"Categorical columns: {len(categorical_cols)}")
    return numeric_cols, categorical_cols

def bar_for_distribution_of_attack_types(df: pd.DataFrame):
    plt.figure(figsize=(10, 6))
    df['AttackType'].value_counts().plot(kind='bar', color='skyblue')
    plt.title('Distribution of Attack Types')
    plt.xlabel('Attack Type')
    plt.ylabel('Frequency')
    plt.show()

def add_hour_column(df):
    df['timestamp'] = pd.to_datetime(df['Timestamp'])

    df['Hour'] = df['timestamp'].dt.hour

    df = df.drop('timestamp', axis=1)  


def frequency_of_attacks_by_hour(df):
    # Bar chart for attack frequency by hour
    plt.figure(figsize=(10, 6))
    df['Hour'].value_counts().sort_index().plot(kind='bar', color='lightgreen')
    plt.title('Frequency of Attacks by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Attacks')
    plt.show()

def add_date_column(df):
    df['timestamp'] = pd.to_datetime(df['Timestamp'])

    df['Date'] = df['timestamp'].dt.date

    df = df.drop('timestamp', axis=1)

def frequency_of_attacks_by_day(df):
    # Bar chart for attack frequency by day
    plt.figure(figsize=(10, 6))
    df['Date'].value_counts().sort_index().plot(kind='bar', color='salmon')
    plt.title('Frequency of Attacks by Day')
    plt.xlabel('Date')
    plt.ylabel('Number of Attacks')
    plt.show()

def pie_chart_for_types_of_attacks(df: pd.DataFrame, date: str = '2023-01-05'):
    # Filter attacks on date
    attacks_on_date = df[pd.to_datetime(df['Timestamp']).dt.date == pd.to_datetime(date).date()]

    # Pie chart for attack types on 05/01/2023
    plt.figure(figsize=(8, 8))
    attacks_on_date['AttackType'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette("coolwarm"))
    plt.title('Types of Attacks on 05/01/2023')
    plt.ylabel('')
    plt.show()


def heatmap_of_attack_frequency_by_hour(df: pd.DataFrame):
    # Create a pivot table for heatmap
    heatmap_data = df.pivot_table(index=pd.to_datetime(df['Timestamp']).dt.date, columns='Hour', aggfunc='size', fill_value=0)

    # Heatmap visualization
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap="YlGnBu", linewidths=0.5)
    plt.title('Attack Frequency by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Date')
    plt.show()


def pie_chart_of_sourcesIP_of_attacks(df: pd.DataFrame, n = None):
    plt.figure(figsize=(8, 8))
    if n is not None:
        df['SourceIP'].value_counts().nlargest(n).plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette("pastel"))
        plt.title(f'Top {n} Source IPs of Attacks')
        plt.ylabel('')
        plt.show()
    else:
        df['SourceIP'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette("pastel"))
        plt.title('Source IPs of Attacks')
        plt.ylabel('')
        plt.show()

def pie_chart_targetsIP_of_attacks(df: pd.DataFrame, n: int = None):
    plt.figure(figsize=(8, 8))
    if n is not None:
        df['TargetIP'].value_counts().nlargest(n).plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette("pastel"))
        plt.title(f'Top {n} Target IPs of Attacks')
        plt.ylabel('')
        plt.show()

    else:
        df['TargetIP'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette("pastel"))
        plt.title(f'Target IPs of Attacks')
        plt.ylabel('')
        plt.show()

def box_violin_plot_for_attack_durations_by_type(df: pd.DataFrame):
    # Box and Violin plot for duration of attacks
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='AttackType', y='AttackDurationHours', data=df)
    plt.title('Boxplot of Attack Durations by Attack Type')
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.violinplot(x='AttackType', y='AttackDurationHours', data=df)
    plt.title('Violin Plot of Attack Durations by Attack Type')
    plt.xticks(rotation=45)
    plt.show()




