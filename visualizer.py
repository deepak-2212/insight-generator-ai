import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_charts(df, output_folder='outputs'):
    os.makedirs(output_folder, exist_ok=True)
    chart_info = []

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    categorical_cols = df.select_dtypes(exclude='number').columns.tolist()

    # Histogram + Line for each numeric column
    for col in numeric_cols:
        # Histogram
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col], kde=True, color='skyblue')
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        filename = f"{col}_hist.png"
        plt.tight_layout()
        plt.savefig(os.path.join(output_folder, filename))
        plt.close()
        chart_info.append({
            "title": f"Distribution of {col}",
            "filename": filename,
            "desc": f"Histogram showing distribution of '{col}'."
        })

        # Line Chart (Trend)
        plt.figure(figsize=(6, 4))
        sns.lineplot(x=df.index, y=df[col], marker="o", color="orange")
        plt.title(f"Trend of {col} over rows")
        plt.xlabel("Row Index")
        plt.ylabel(col)
        filename = f"{col}_line.png"
        plt.tight_layout()
        plt.savefig(os.path.join(output_folder, filename))
        plt.close()
        chart_info.append({
            "title": f"Trend of {col}",
            "filename": filename,
            "desc": f"Line chart showing how '{col}' changes over rows."
        })

    # Pie + Bar for first categorical column
    if categorical_cols:
        col = categorical_cols[0]
        value_counts = df[col].value_counts().head(6)

        # Pie Chart
        plt.figure(figsize=(6, 6))
        value_counts.plot.pie(autopct='%1.1f%%')
        plt.title(f"Pie Chart of {col}")
        plt.ylabel("")  # Hide Y label for pie
        filename = f"{col}_pie.png"
        plt.tight_layout()
        plt.savefig(os.path.join(output_folder, filename))
        plt.close()
        chart_info.append({
            "title": f"Pie Chart of {col}",
            "filename": filename,
            "desc": f"Pie chart showing top 6 values in '{col}'."
        })

        # Bar Chart
        plt.figure(figsize=(6, 4))
        sns.barplot(x=value_counts.index, y=value_counts.values, palette='pastel')
        plt.title(f"Bar Chart of {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        filename = f"{col}_bar.png"
        plt.tight_layout()
        plt.savefig(os.path.join(output_folder, filename))
        plt.close()
        chart_info.append({
            "title": f"Bar Chart of {col}",
            "filename": filename,
            "desc": f"Bar chart showing frequency of top 6 '{col}' values."
        })

    # Scatter Plot: Use first two numeric columns if available
    if len(numeric_cols) >= 2:
        x_col, y_col = numeric_cols[:2]
        plt.figure(figsize=(6, 4))
        sns.scatterplot(x=df[x_col], y=df[y_col], color='green')
        plt.title(f"Scatter: {x_col} vs {y_col}")
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        filename = f"scatter_{x_col}_vs_{y_col}.png"
        plt.tight_layout()
        plt.savefig(os.path.join(output_folder, filename))
        plt.close()
        chart_info.append({
            "title": f"Scatter Plot: {x_col} vs {y_col}",
            "filename": filename,
            "desc": f"Scatter plot comparing '{x_col}' and '{y_col}'."
        })

    return chart_info
