from parser import load_data
from analyzer import analyze_data
from visualizer import generate_visualizations
import sys

def main(input_file):
    data = load_data(input_file)
    insights = analyze_data(data)
    generate_visualizations(data, insights)

if __name__ == "__main__":
    input_path = sys.argv[1] if len(sys.argv) > 1 else "sample_data/sample.csv"
    main(input_path)
