import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_charts(df, output_folder='outputs'):
    os.makedirs(output_folder, exist_ok=True)

    chart_info = []

    for column in df.select_dtypes(include='number').columns:
        title = f"Distribution of {column}"
        description = f"This chart shows how values are distributed in the column '{column}'."

        plt.figure(figsize=(8, 4))
        sns.histplot(df[column], kde=True, color='skyblue')
        plt.title(title)
        plt.xlabel(column)
        plt.ylabel("Frequency")

        filename = f"{column}_histogram.png"
        filepath = os.path.join(output_folder, filename)
        plt.savefig(filepath)
        plt.close()

        chart_info.append({
            "title": title,
            "description": description,
            "filename": filename
        })

    return chart_info
