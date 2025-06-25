import matplotlib.pyplot as plt
import seaborn as sns
import os

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_visualizations(df, insights):
    sns.set(style="darkgrid")
    
    # Line chart for trends
    if "monthly_trends" in insights:
        plt.figure(figsize=(10, 6))
        insights["monthly_trends"].plot()
        plt.title("Monthly Trends")
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/monthly_trends.png")
        plt.close()

    # Pie chart (for categorical count)
    for col in df.select_dtypes(include='object').columns:
        plt.figure(figsize=(6, 6))
        df[col].value_counts().head(5).plot.pie(autopct='%1.1f%%')
        plt.title(f"Top {col} Distribution")
        plt.ylabel("")
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/{col}_pie.png")
        plt.close()
