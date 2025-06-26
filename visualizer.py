import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_charts(df, output_folder='outputs'):
    os.makedirs(output_folder, exist_ok=True)
    chart_info = []

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    categorical_cols = df.select_dtypes(exclude='number').columns.tolist()

    # Histogram + line for each numeric column
    for col in numeric_cols:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col], kde=True, color='skyblue')
        title = f"Distribution of {col}"
        filename = f"{col}_hist.png"
        path = os.path.join(output_folder, filename)
        plt.title(title)
        plt.savefig(path)
        plt.close()
        chart_info.append({"title": title, "filename": filename, "desc": f"Histogram of {col}."})

        plt.figure(figsize=(6, 4))
        sns.lineplot(x=df.index, y=df[col], marker="o", color="orange")
        title = f"Trend of {col} over rows"
        filename = f"{col}_line.png"
        path = os.path.join(output_folder, filename)
        plt.title(title)
        plt.savefig(path)
        plt.close()
        chart_info.append({"title": title, "filename": filename, "desc": f"Trend line of {col}."})

    # Pie + bar chart for categorical column (first one)
    if categorical_cols:
        col = categorical_cols[0]
        value_counts = df[col].value_counts().head(6)

        # Pie chart
        plt.figure(figsize=(6, 6))
        value_counts.plot.pie(autopct='%1.1f%%')
        title = f"Pie Chart of {col}"
        filename = f"{col}_pie.png"
        path = os.path.join(output_folder, filename)
        plt.title(title)
        plt.ylabel("")
        plt.savefig(path)
        plt.close()
        chart_info.append({"title": title, "filename": filename, "desc": f"Top categories in {col}."})

        # Bar chart
        plt.figure(figsize=(6, 4))
        sns.barplot(x=value_counts.index, y=value_counts.values, palette='pastel')
        title = f"Bar Chart of {col}"
        filename = f"{col}_bar.png"
        path = os.path.join(output_folder, filename)
        plt.title(title)
        plt.savefig(path)
        plt.close()
        chart_info.append({"title": title, "filename": filename, "desc": f"Bar chart of {col} frequency."})

    # Scatter plot if 2+ numeric columns
    if len(numeric_cols) >= 2:
        plt.figure(figsize=(6, 4))
        sns.scatterplot(x=df[numeric_cols[0]], y=df[numeric_cols[1]], color='green')
        title = f"Scatter: {numeric_cols[0]} vs {numeric_cols[1]}"
        filename = f"scatter_{numeric_cols[0]}_{numeric_cols[1]}.png"
        path = os.path.join(output_folder, filename)
        plt.title(title)
        plt.savefig(path)
        plt.close()
        chart_info.append({
            "title": title,
            "filename": filename,
            "desc": f"Scatter plot of {numeric_cols[0]} vs {numeric_cols[1]}"
        })

    return chart_info
