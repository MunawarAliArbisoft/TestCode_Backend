# TestCode Backend

The TestCode is an online assessment Center backend project aims to create a robust backend system for managing an online assessment center. Admins can effortlessly create assessments, candidates can register and attempt assessments, and automated code evaluation provides immediate feedback.

## Key Features

- Admins create and manage assessments with titles, descriptions, and question types.
- Candidates register, attempt assessments, and receive automated feedback.
- Various question types including MCQs and coding questions are supported.
- Automated code evaluation ensures consistent and accurate results.
- Admins oversee assessments, view reports, and manage users.
- Secure authentication and API endpoints ensure data integrity.

## Getting Started

1. Clone the repository.
2. Set up a virtual environment.
3. Install dependencies from `requirements.txt`.
4. Run migrations and start the development server.

## Documentation

The detailed information on API endpoints are given below:
- [Candidate](#candidate)
- [Questions](#questions)
- [Assessment](#assessment)
- [Assessments Result](#assessments-result)
- [Login](#login)

## Candidate

- **List Candidates:** Get a list of all candidates.

  - URL: `http://127.0.0.1:8000/api/candidate/candidates`
  - Method: GET

- **Retrieve Candidate:** Get details of a candidate by ID.

  - URL: `http://127.0.0.1:8000/api/candidate/candidates/{id}`
  - Method: GET

- **Create Candidate:** Register a new candidate.

  - URL: `http://127.0.0.1:8000/api/candidate/candidates`
  - Method: POST
  - Request Body:
    ```json
    {
        "first_name": "XYZ",
        "last_name": "EFG",
        "is_staff": false,
        "email": "abc23@gmail.com",
        "password": "1234"
    }
    ```

- **Update Candidate:** Update candidate data by providing ID.

  - URL: `http://127.0.0.1:8000/api/candidate/candidates/{id}`
  - Method: PUT
  - Request Body (full update):
    ```json
    {
        "first_name": "XYZ",
        "last_name": "EFG",
        "is_staff": false,
        "email": "abc23@gmail.com",
        "password": "1234"
    }
    ```

- **Partial Update Candidate:** Update some parts of candidate data by providing ID.

  - URL: `http://127.0.0.1:8000/api/candidate/candidates/{id}`
  - Method: PATCH
  - Request Body (partial update):
    ```json
    {
        "is_staff": true,
        "email": "abc23@yahoo.com"
    }
    ```

- **Delete Candidate:** Delete a candidate by providing ID.

  - URL: `http://127.0.0.1:8000/api/candidate/candidates/{id}`
  - Method: DELETE

### Permissions

- **List Candidates:** Only staff users are allowed.
- **Create Candidate:** Any user can create.
- **Retrieve Candidate:** Only the owner of the candidate can retrieve.
- **Update Candidate:** Owners and staff members can update.
- **Partial Update Candidate:** Owners and staff members can update partially.
- **Delete Candidate:** Only staff users are allowed.

## Questions

- **List Questions:** Get a list of all questions.

  - URL: `http://127.0.0.1:8000/api/question/questions`
  - Method: GET

- **Retrieve Question:** Get details of a question by ID.

  - URL: `http://127.0.0.1:8000/api/question/questions/{id}`
  - Method: GET

- **Create Question:** Create a new question.

  - URL: `http://127.0.0.1:8000/api/question/questions`
  - Method: POST
  - Request Body:
    ```json
    {
        "assessment": 4,
        "text": "Write the function to add two numbers",
        "question_type": "COD",
        "code_template": "def add(num1, num2):\r\n    pass",
        "choices": [
            {
                "id": 5,
                "text": "1"
            }
        ],
        "testcases": [
            {
                "id": 1,
                "input_data": "1,2",
                "expected_output": "3",
                "is_public": true
            }
        ]
    }
    ```

- **Update Question:** Update question data by providing ID.

  - URL: `http://127.0.0.1:8000/api/question/questions/{id}`
  - Method: PUT
  - Request Body:
    ```json
    {
        "assessment": 4,
        "text": "Write the function to add two numbers",
        "question_type": "COD",
        "code_template": "def add(num1, num2):\r\n    pass",
        "choices": [
            {
                "id": 5,
                "text": "1"
            }
        ],
        "testcases": [
            {
                "id": 1,
                "input_data": "1,2",
                "expected_output": "3",
                "is_public": true
            }
        ]
    }
    ```

- **Partial Update Question:** Update some parts of question data by providing ID.

  - URL: `http://127.0.0.1:8000/api/question/questions/{id}`
  - Method: PATCH
  - Request Body:
    ```json
    {
        "question_type": "MCQ"
    }
    ```

- **Delete Question:** Delete a question by providing ID.

  - URL: `http://127.0.0.1:8000/api/question/questions/{id}`
  - Method: DELETE

### Permissions

- **List Questions:** Authenticated user can access.
- **Retrieve Question:** Authenticated user can access.
- **Create Question:** Staff users are allowed.
- **Update Question:** Staff users are allowed.
- **Partial Update Question:** Staff users are allowed.
- **Delete Question:** Staff users are allowed.

## Assessment

- **List Assessments:** Get a list of all assessments.

  - URL: `http://127.0.0.1:8000/api/assessment/assessments`
  - Method: GET

- **Retrieve Assessment:** Get details of an assessment by ID.

  - URL: `http://127.0.0.1:8000/api/assessment/assessments/{id}`
  - Method: GET

- **Create Assessment:** Create a new assessment.

  - URL: `http://127.0.0.1:8000/api/assessment/assessments`
  - Method: POST
  - Request Body:
    ```json
    {
        "title": "Math Assignment",
        "description": "A math assignment for KG",
        "date_created": "2023-08-04",
        "date_updated": "2023-08-04",
        "questions": [
            {
                "id": 1,
                "assessment": 1,
                "text": "What is 2+2?",
                ... (other question fields)
            },
            ... (other questions)
        ]
    }
    ```

- **Update Assessment:** Update assessment data by providing ID.

  - URL: `http://127.0.0.1:8000/api/assessment/assessments/{id}`
  - Method: PUT
  - Request Body:
    ```json
    {
        "title": "Math Assignment",
        "description": "Updated description",
        "date_created": "2023-08-04",
        "date_updated": "2023-08-10",
        "questions": [
            {
                "id": 1,
                "assessment": 1,
                "text": "What is 2+2?",
                ... (other question fields)
            },
            ... (other questions)
        ]
    }
    ```

- **Partial Update Assessment:** Update some parts of assessment data by providing ID.

  - URL: `http://127.0.0.1:8000/api/assessment/assessments/{id}`
  - Method: PATCH
  - Request Body:
    ```json
    {
        "description": "Updated description"
    }
    ```

- **Delete Assessment:** Delete an assessment by providing ID.

  - URL: `http://127.0.0.1:8000/api/assessment/assessments/{id}`
  - Method: DELETE

### Permissions

- **List Assessments:** Authenticated user can access.
- **Retrieve Assessment:** Authenticated user can access.
- **Create Assessment:** Staff users are allowed.
- **Update Assessment:** Staff users are allowed.
- **Partial Update Assessment:** Staff users are allowed.
- **Delete Assessment:** Staff users are allowed.

## Assessments Result

- **List Assessment Results:** Get a list of all assessment results.

  - URL: `http://127.0.0.1:8000/api/assessment/assessments-result`
  - Method: GET

- **Retrieve Assessment Result:** Get details of an assessment-result by ID.

  - URL: `http://127.0.0.1:8000/api/assessment/assessments-result/{id}`
  - Method: GET

- **Create Assessment Result:** Create a new assessment result.

  - URL: `http://127.0.0.1:8000/api/assessment/assessments-result`
  - Method: POST
  - Request Body:
    ```json
    {
    "score": 87.0,
    "assessment": {
        "id": 4
    },
    "candidate": {
        "email": "abdullah@gmail.com"
    },
    "result": [
            {
                "type": "MCQ",
                "score": 1,
                "question": "What is the datatype of 92.3?",
                "correct_choice": "float",
                "selected_choice": "float"
            },
            {
                "type": "COD",
                "score": 1,
                "question": "Write the function to greet with name?",
                "testcase_results": [
                    {
                        "input": "Munawar",
                        "status": "Pass",
                        "duration": 0.063543,
                        "actual_output": "Hello Munawar",
                        "expected_output": "Hello Munawar"
                    }
                ]
            },
            {
                "type": "COD",
                "score": 0,
                "question": "Write the function to sum 2 numbers?",
                "testcase_results": [
                    {
                        "error": "Mismatch Arguments or invalid syntax",
                        "status": "Fail"
                    },
                    {
                        "error": "Mismatch Arguments or invalid syntax",
                        "status": "Fail"
                    }
                ]
            }
        ]
    }
    ```

- **Update Assessments Result:** Update assessment data by providing ID.

  - URL: `http://127.0.0.1:8000/api/assessment/assessments-result/{id}`
  - Method: PUT
  - Request Body:
    ```json
    {
    "score": 87.0,
    "assessment": {
        "id": 4
    },
    "candidate": {
        "email": "abdullah@gmail.com"
    },
    "result": [
            {
                "type": "MCQ",
                "score": 1,
                "question": "What is the datatype of 92.3?",
                "correct_choice": "float",
                "selected_choice": "float"
            },
            {
                "type": "COD",
                "score": 1,
                "question": "Write the function to greet with name?",
                "testcase_results": [
                    {
                        "input": "Munawar",
                        "status": "Pass",
                        "duration": 0.063543,
                        "actual_output": "Hello Munawar",
                        "expected_output": "Hello Munawar"
                    }
                ]
            },
        ]
    }
    ```

- **Partial Update Assessment Result:** Update some parts of assessment data by providing ID.

  - URL: `http://127.0.0.1:8000/api/assessment/assessments-result/{id}`
  - Method: PATCH
  - Request Body:
    ```json
    {
        "score": 90.0
    }
    ```

- **Delete Assessment Result:** Delete an assessment by providing ID.

  - URL: `http://127.0.0.1:8000/api/assessment/assessments-result/{id}`
  - Method: DELETE

### Permissions

- **List Assessments Result:** Staff users are allowed.
- **Retrieve Assessment Result:** Staff and Owner are allowed
- **Create Assessment Result:** Staff users are allowed.
- **Update Assessment Result:** Staff users are allowed.
- **Partial Update Assessment Result:** Staff users are allowed.
- **Delete Assessment Result:** Staff users are allowed.

## Login

Authenticate a user by providing their email and password. This endpoint generates JWT tokens for authentication.

- **URL:** `http://127.0.0.1:8000/api/login/`
- **Method:** POST

- Request
  - **Body:**
    ```json
    {
        "email": "abc@gmail.com",
        "password": "123"
    }
    ```
- Response
  - Status Code: 200 OK
  - Description: Returns JWT tokens for access and refresh.
  - data:
  ```json
  {
    "refresh": "eyJhbGciOiJIUzIkjfnwkjdnkwqjdoqjpwdpjoqCJqdGkiOiIzMzIzYjlmNjNhODg0ODY5YWExYmYyY2MwZjYzNzFhMiIsInVzZXJfaWQiOjE0fQ.VkAC-kDZjwkYf6p8V7C_TwruGxKgQkNx1uM2kNaWoZk",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkyMjk1MzQ5LCJpYXQiOkjwhdkbqkjdnoiWIaSI6IjkzYjQzYzFiMWEwZTQ3MjU5YTc0ZWIwNGEwOTRlYTUwIiwidXNlcl9pZCI6MTR9.4k58jbEcP-4ovZb_l1Ck7BNnCtEs7mSBf83i_mEcCCY"
  }
  ```
## Contribution

Contributions, bug reports, and feature requests are welcome. Please follow the contribution guidelines.
