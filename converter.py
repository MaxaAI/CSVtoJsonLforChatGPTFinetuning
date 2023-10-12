import csv
import json

def csv_to_gpt_format(input_filename, output_filename):
    # Open the output file for writing
    with open(output_filename, 'w', encoding='utf-8') as outfile:

        # Process the CSV and append messages to the base structure
        with open(input_filename, 'r', encoding='utf-8-sig') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                base = {
                    "messages": [
                        {
                            "role": "system",
                            "content": "Your finetuning message"
                        }
                    ]
                }

                user_content = row["User"]
                assistant_content = row["Assistant"]

                user_message = {
                    "role": "user",
                    "content": user_content
                }

                assistant_message = {
                    "role": "assistant",
                    "content": assistant_content
                }

                base["messages"].append(user_message)
                base["messages"].append(assistant_message)

                # Write the JSON format for each dialogue to the output file
                json_line = json.dumps(base) + "\n"  # add newline for each conversation
                outfile.write(json_line)

csv_to_gpt_format("testing.csv", "output.jsonl")