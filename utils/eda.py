import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def run_eda(df):
    """
    Perform EDA visualizations for housing dataset.

    Parameters:
        df (pd.DataFrame): Input dataframe (raw or clean).
        label (str): String label to indicate dataset type for titles (e.g., 'Raw Data' or 'Clean Data').
    """
    # Sampling for large visualizations
    sample_df = df.sample(n=min(50_000, len(df)), random_state=42)

    # Set plot style
    custom_color = "#FFB6C1"  # light pink
    sns.set(style="whitegrid", palette="pastel")

    # 1. Distribution of Price and Log-Price
    plt.figure(figsize=(10,5))
    sns.histplot(df['price'], bins=50, kde=True, color=custom_color)
    plt.title(f"Price Distribution")
    plt.show()
    print('-'*200)

    plt.figure(figsize=(10,5))
    sns.histplot(np.log1p(df['price']), bins=50, kde=True, color=custom_color)
    plt.title(f"Log-Price Distribution")
    plt.show()
    print('-'*200)

    # 2. Scatter Plot: Area vs Price
    plt.figure(figsize=(10,5))
    sns.scatterplot(x='total_area', y='price', data=sample_df, alpha=0.5, color=custom_color)
    plt.title(f"House Size vs Price")
    plt.xlabel("House Size / Area")
    plt.ylabel("Price")
    plt.show()
    print('-'*200)

    # 3. Relationships: Bedrooms, Bathrooms vs Price
    fig, axes = plt.subplots(1, 2, figsize=(15,5))
    sns.boxplot(x='bed', y='price', data=df, ax=axes[0], color=custom_color)
    axes[0].set_title(f"Price by Bedrooms")

    sns.boxplot(x='bath', y='price', data=df, ax=axes[1], color=custom_color)
    axes[1].set_title(f"Price by Bathrooms")
    plt.show()
    print('-'*200)

    # 4. Boxplots of Price by State
    if 'state' in df.columns:
        plt.figure(figsize=(15,5))
        sns.boxplot(x='state', y='price', data=df, color=custom_color)
        plt.title(f"Price by State")
        plt.xticks(rotation=90)
        plt.show()
    print('-'*200)

  # 5. Correlation Heatmap (sampled for speed)
    plt.figure(figsize=(10,5))
    corr = sample_df[['price','total_area','bed','bath']].corr()
    sns.heatmap(corr, annot=True, cmap="RdPu", fmt=".2f")
    plt.title(f"Correlation Heatmap (50k samples)")
    plt.show()