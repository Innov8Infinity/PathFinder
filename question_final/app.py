from flask import Flask, request, render_template, redirect, url_for
import csv
import os
import pandas as pd
from ollama import generate
from threading import Thread

app = Flask(__name__)

data_dir = os.path.join(app.root_path, 'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

csv_file_path = os.path.join(data_dir, 'submissions.csv')

def read_file(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file type. Please provide a CSV or Excel file.")

def format_data(row):
    prompt = (
        f"I am a student with an education level of {row['Education_Level']}. "
        f"My current branch is {row['Branch']} and my preferred branch is {row['Preferred_Branch']}. "
        f"My preferred subjects are {row['Preferred_Subjects']} and my least preferred subjects are {row['Least_Preferred_Subjects']}. "
        f"My learning style is {row['Learning_Style']}. My career goals include {row['Career_Goals']}. "
        f"I am interested in fields such as {row['Fields_of_Interest']}. My preferred job roles are {row['Preferred_Job_Roles']}. "
        f"I possess technical skills in {row['Technical_Skills']} and have obtained certifications in {row['Certifications']}. "
        f"I have work experience in {row['Work_Experience']}. I prefer learning through platforms like {row['Learning_Platforms']} "
        f"and plan to pursue courses or certifications such as {row['Courses_Certifications']}. "
        f"I am passionate about skills like {row['Passionate_Skills']}. "
        f"Can you suggest some relevant courses along with LINKS on platforms like Coursera, Udemy, that align with my goals and interests, "
        f"along with this can you provide insights on what career goals and study plan for me based on the above data? "
        f"Please give the output in normal text like don't use bold, italic extra lines, give the links next to the course without parenthesis and make it perfect."
    )
    return prompt

def get_llm_response(prompt):
    full_response = ''
    for response in generate(model='llama3', prompt=prompt, stream=True):
        print(response['response'], end='', flush=True)
        full_response += response['response']
    return full_response

def append_youtube_links(response, field_of_interest):
    youtube_links = {
        'machine learning': [
            'https://www.youtube.com/watch?v=Gv9_4yMHFhI',
            'https://www.youtube.com/watch?v=7eh4d6sabA0',
            'https://www.youtube.com/watch?v=IpGxLWOIZy4',
            'https://www.youtube.com/watch?v=HcqpanDadyQ',
            'https://www.youtube.com/watch?v=0qtRNg6X8bM'
        ],
        'blockchain': [
            'https://www.youtube.com/watch?v=SSo_EIwHSd4',
            'https://www.youtube.com/watch?v=3xGLc-zz9cA',
            'https://www.youtube.com/watch?v=bBC-nXj3Ng4',
            'https://www.youtube.com/watch?v=2pTzTZUn6hI',
            'https://www.youtube.com/watch?v=TDGq4aeevgY'
        ],
        'data structures and algorithms': [
            'https://www.youtube.com/watch?v=8hly31xKli0',
            'https://www.youtube.com/watch?v=bum_19loj9A',
            'https://www.youtube.com/watch?v=RBSGKlAvoiM',
            'https://www.youtube.com/watch?v=PkZNo7MFNFg',
            'https://www.youtube.com/watch?v=ShEez0JkOFw'
        ],
        'cyber security': [
            'https://www.youtube.com/watch?v=7m-cmNdiFuU',
            'https://www.youtube.com/watch?v=1gO2U1aOq4A',
            'https://www.youtube.com/watch?v=fWzEzFLa2rY',
            'https://www.youtube.com/watch?v=lI4c0zCz-XQ',
            'https://www.youtube.com/watch?v=2Hb9I-d6PHc'
        ],
        'java': [
            'https://www.youtube.com/watch?v=grEKMHGYyns',
            'https://www.youtube.com/watch?v=eIrMbAQSU34',
            'https://www.youtube.com/watch?v=3u1fu6f8Hto',
            'https://www.youtube.com/watch?v=WPvGqX-TXP0',
            'https://www.youtube.com/watch?v=og1e2t7iWFs'
        ],
        # Add more categories and links as needed
    }

    field_of_interest_lower = field_of_interest.lower()
    for category, links in youtube_links.items():
        if category in field_of_interest_lower:
            response += "\n\nYouTube Links:\n" + "\n".join(links)
            break
    return response

def process_llm_responses(csv_data):
    responses = []
    for _, row in csv_data.iterrows():
        prompt = format_data(row)
        response = get_llm_response(prompt)
        response_with_links = append_youtube_links(response, row['Fields_of_Interest'])
        responses.append(response_with_links)

    # Save the responses to a file
    responses_file_path = os.path.join(data_dir, 'llm_responses.txt')
    with open(responses_file_path, 'w') as f:
        for response in responses:
            f.write(response + '\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'Education_Level': request.form.get('Education_Level'),
        'Branch': request.form.get('Branch'),
        'Preferred_Branch': request.form.get('Preferred_Branch'),
        'Preferred_Subjects': request.form.get('Preferred_Subjects'),
        'Least_Preferred_Subjects': request.form.get('Least_Preferred_Subjects'),
        'Learning_Style': request.form.get('Learning_Style'),
        'Career_Goals': request.form.get('Career_Goals'),
        'Fields_of_Interest': request.form.get('Fields_of_Interest'),
        'Preferred_Job_Roles': request.form.get('Preferred_Job_Roles'),
        'Technical_Skills': request.form.get('Technical_Skills'),
        'Certifications': request.form.get('Certifications'),
        'Work_Experience': request.form.get('Work_Experience'),
        'Learning_Platforms': request.form.get('Learning_Platforms'),
        'Courses_Certifications': request.form.get('Courses_Certifications'),
        'Passionate_Skills': request.form.getlist('Passionate_Skills'),
    }
    try:
        os.remove(csv_file_path)
    except FileNotFoundError:
        pass
    fieldnames = list(data.keys())
    try:
        # Write data to CSV file
        with open(csv_file_path, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(data)
    except Exception as e:
        print(f"Error writing to CSV file: {e}")
        return redirect('/')

    # Start a new thread to process LLM responses
    csv_data = read_file(csv_file_path)
    thread = Thread(target=process_llm_responses, args=(csv_data,))
    thread.start()

    # Redirect to the dashboard page
    return redirect('http://127.0.0.1:5501/dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)