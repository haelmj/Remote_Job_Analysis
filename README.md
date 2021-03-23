# Remote_Job_Analysis

Analysis to map-out the quantity of available remote jobs per category

View Trello Board [here](https://trello.com/b/2eVWEyPj/remote-job-analysis)

## Requirements

This project requires preferably version 89.0.4389.90 of Chrome browser as well as Python 3 installed on the host system.

**Python Dependencies**

- [Selenium](https://pypi.org/project/selenium/)

**WebDriver**

- [Chrome WebDriver](https://chromedriver.chromium.org/)  
*Note:* A chrome webdriver for version 89 can be found in the assets folder of this project. If you have a different version of Chrome, download the chrome webdriver for that version and replace it with the one in the assets folder.

### Setup

1. Clone this project to your local system:
`git clone https://github.com/haelmj/Remote_Job_Analysis.git`

2. Setup Chrome Driver:

    - Include the ChromeDriver location in your PATH environment variable
    - Create an environment variable with key: `CHROME_DRIVER` and value: the full path to the chromedriver executable.

3. Setup a virtual environment:

```

python -m venv venv

```

4. Activate the virtual environment:
For Windows Command Line Users:

```
venv\Scripts\activate.bat
```

For bash users:

```bash
source /venv/Scripts/activate
```

5. Install module dependencies:
`pip install -r requirements.txt`

### Stage 1

*Estimated Scrape time: 4mins*

Run app:

```
cd Stage1-DataGathering/
python get_job_listings.py
```

## Development Status

- **In progress**
