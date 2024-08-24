# PathFinder

PathFinder is an AI-driven platform designed to provide personalized career guidance to students in educational institutions. Leveraging machine learning algorithms,PathFinder analyzes a wide range of student data to offer tailored recommendations for courses, topics, and career fields based on individual preferences, academic performance, and ongoing trends.

## Key Features

- **Data Collection:** Gathers comprehensive student data including academic records, preferences, interests, goals, and feedback.
- **Machine Learning Models:** Employs algorithms to analyze data and uncover patterns for academic and career insights.
- **Personalized Recommendations:** Provides tailored guidance on courses, topics of focus, and potential career fields.
- **Interactive Interface:** Offers a user-friendly interface for seamless interaction.
- **Continuous Improvement:** Incorporates feedback to enhance recommendation accuracy over time.

## Tech Stack

- **Backend:** Flask, Python , Streamlit, FastAPI,etc
- **Machine Learning Library:**  Pytorch..
- **LLM's:**  llama3(8b),llava
- **Web Framework:** Flask , HTML5, CSS3, JS, Bootstrap
- **Database Management System:** MySQL (not implemented yet)

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.11.x
- pip (Python package installer)
- MySQL (optional)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/HackStyx/PathFinder.git
    cd PathFinder
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up the LLM locally:
    - Install the ollama locally with all the required applications.
    - Start the ollama with 'llama3' profile.([tutorial)](https://docs.privategpt.dev/installation/getting-started/installation)

4. Run the application:
    ```sh
    python app.py (for connecting the auth page to form)
    python LLM_Main.py (for connecting the Local LLM to Program via API)
    index.html
    ```

### Usage

- Access the platform at `http://localhost:5000`.
- Sign up and provide your academic and personal information.
- Get personalized course and career recommendations.

## Folder Structure

```plaintext
PathFinder/
├── README.md
├── LLM_Main.md
├── requirements.txt
├── index.html
├── dashboard.html
├── results.html
├── dashb.html
├── assets/..
├──Login/
│   ├── index.html
│   ├── signup.html
│   ├── others/..
└── question_final/
    └── data/submissions.csv
	└── app.py
	└──format_data.py
	└── llm_responses.txt

```
## Note

->If something is not working or getting connection error try changing the host address and relative path of the resources.

->If you are getting slow output that's totally hardware dependent. (you can use cuda cores for better performance)

## Screenshots
![Screenshot 2024-08-24 113322](https://github.com/user-attachments/assets/6e1217d8-7c84-4e7d-8902-be178e6cab9d)
![Screenshot 2024-08-24 113437](https://github.com/user-attachments/assets/8931da3a-4e77-400f-b0d1-bcffe270526f)
![Screenshot 2024-08-24 113600](https://github.com/user-attachments/assets/832267a3-c288-4d5d-be71-e2cd09553bf1)
![Screenshot 2024-08-24 113641](https://github.com/user-attachments/assets/d7abe30c-0fbb-4333-86e6-054f29ab88fd)
![Screenshot 2024-08-24 113819](https://github.com/user-attachments/assets/2f6672ad-46aa-4dcd-bbfd-6450a51327e3)



## Contributing
We welcome contributions from the our community! If you'd like to contribute to the project, please follow our [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, suggestions, or want to contribute to this project, please feel free to reach :
- [Prince](https://github.com/hackstyx)
