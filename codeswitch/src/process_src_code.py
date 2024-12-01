import os

def process_code_file(input_path: str, output_path: str, write=True):
    # Ensure the input file exists
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"The file {input_path} does not exist.")

    # Read the content of the input file
    with open(input_file_path, 'r') as input_file:
        content = input_file.read()

    # Process the content
    # For this example, we will just copy the content as is
    processed_content = process_code(content)

    # Write the processed content to the output file
    if write:
        with open(output_path, 'w') as output_file:
            output_file.write(processed_content)

        print(f"Processed content has been written to {output_path}")
    else:
        print(processed_content)

def process_code(content: str) -> str:
    # Process the content

    # convert keywords
    processed_content = content
    return processed_content

if __name__ == "__main__":
    input_file_path = "main.java"  # Change this to your input file path
    output_file_path = "out/french.java"  # Change this to your desired output file path

    process_code_file(input_file_path, output_file_path, write=False)