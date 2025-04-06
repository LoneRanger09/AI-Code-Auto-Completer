import json
import os

def preprocess_dataset():
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script directory
    input_path = os.path.join(script_dir, "code_samples.json")  # Correct file path
    output_path = os.path.join(script_dir, "preprocessed_data.json")

    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found. Please check the file path.")
        return

    with open(input_path, "r") as f:
        data = json.load(f)

    processed_data = [{"input": item["input"], "output": item["output"]} for item in data]

    with open(output_path, "w") as f:
        json.dump(processed_data, f, indent=4)

    print("Dataset Preprocessed Successfully!")

if __name__ == "__main__":
    preprocess_dataset()
