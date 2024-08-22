
# CVsum Project

This project is a web application designed to summarize key points from a CV in PDF format using the OpenAI API and present the results in an Excel file.

## Project Structure

The project is organized as follows:

- **app/**
  - **routes.py**: Contains the main routes and logic for processing PDF files, interacting with the OpenAI API, and generating the Excel file.
- **static/**
  - **index.html**: HTML file providing a simple interface for uploading PDF files and obtaining generated summaries.
- **main.py**: The main file that configures and runs the FastAPI application.
- **requirements.txt**: File containing the dependencies required to run the project.
- **.env**: Optional file for securely storing the OpenAI API key (this file should be excluded from version control).

## Requirements

Before you begin, ensure you have the following prerequisites installed:

- Python 3.7 or higher
- pip (Python package installer)
- Git

## Installation

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/portfoliojuanberrios/CVsum.git
cd CVsum
```

### 2. Create and Activate a Virtual Environment

It is recommended to use a virtual environment to manage the project dependencies.

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### On Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

With the virtual environment activated, install the project dependencies using pip:

```bash
pip install -r requirements.txt
```

### 4. Configure the OpenAI API Key

The project requires an OpenAI API key to function. You need to configure this key securely within the source code.

#### Edit `routes.py`:

1. Open the `app/routes.py` file.
2. Locate the line where the OpenAI client is initialized:

    ```python
    client = openai.Client(api_key='put open api key')
    ```

3. Replace `'put open api key'` with your actual API key. **Be sure to keep this key secure and do not share it publicly.**

#### Secure Alternative: Using Environment Variables

It is recommended not to store the API key directly in the code. You can use a `.env` file or configure the key as an environment variable:

1. **.env File:** Create a `.env` file in the root of the project with the following content:

    ```plaintext
    OPENAI_API_KEY=your_api_key_here
    ```

2. Modify `routes.py` to read the key from the environment variable:

    ```python
    import os
    client = openai.Client(api_key=os.getenv('OPENAI_API_KEY'))
    ```

3. **System Environment Variables:**
   - On **Windows**: 
     1. Open Control Panel -> System and Security -> System.
     2. Click on "Advanced system settings" and then "Environment Variables."
     3. Create a new environment variable named `OPENAI_API_KEY` with your API key as the value.
   - On **Linux**:
     ```bash
     export OPENAI_API_KEY=your_api_key_here
     ```

### 5. Run the Project

With everything configured, you can run the project using:

```bash
uvicorn main:app --reload
```

This command will start the FastAPI application, and it will be served at `http://127.0.0.1:8000`.

### 6. Web Interface

To access the web interface:

1. Open a web browser and go to `http://127.0.0.1:8000/static/index.html`.
2. Upload a PDF file and click "Summarize CV" to generate a summary.
3. Once the summary is generated, you can download an Excel file with the results.

## Notes

- **Security:** Ensure that your API key is not exposed in the public repository. Use a `.gitignore` file to exclude the `.env` file if you choose this option.
- **Compatibility:** The project has been tested on Windows 10 and Ubuntu 20.04. Ensure that your environment meets the minimum requirements.

## Contributions

If you wish to contribute to the project, please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

**Juan A. Berrios Moya**  
AI & Software Engineer and Researcher  
[LinkedIn](https://www.linkedin.com/in/juan-berrios-moya/)
