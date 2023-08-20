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
- Login
- Candidate
- Questions
- Assessment
- Add Assessment Question
- Remove Assessment Question
- Save Answer
- Submit Assessment
- Assessments Result

### Login

Authenticate a user by providing their email and password. This endpoint generates JWT tokens for authentication.

- **URL:** `http://127.0.0.1:8000/api/login/`
- **Method:** POST

#### Request
  - **Body:**
    ```json
    {
        "email": "abc@gmail.com",
        "password": "123"
    }
    ```
#### Response
  - **Status Code: 200 OK**
  - **Description: Returns JWT tokens for access and refresh**
  - **data:**
  ```json
  {
    "refresh": "eyJhbGciOiJIUzIkjfnwkjdnkwqjdoqjpwdpjoqCJqdGkiOiIzMzIzYjlmNjNhODg0ODY5YWExYmYyY2MwZjYzNzFhMiIsInVzZXJfaWQiOjE0fQ.VkAC-kDZjwkYf6p8V7C_TwruGxKgQkNx1uM2kNaWoZk",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkyMjk1MzQ5LCJpYXQiOkjwhdkbqkjdnoiWIaSI6IjkzYjQzYzFiMWEwZTQ3MjU5YTc0ZWIwNGEwOTRlYTUwIiwidXNlcl9pZCI6MTR9.4k58jbEcP-4ovZb_l1Ck7BNnCtEs7mSBf83i_mEcCCY"
  }
  ```

### Candidate

The Candidate section provides endpoints related to candidate management.

#### List Candidates:

- **Get a list of all candidates** 

  - URL: `http://127.0.0.1:8000/api/candidate/candidates`
  - Method: GET

#### Retrieve Candidate:

- **Get details of a candidate by ID**

  - URL: `http://127.0.0.1:8000/api/candidate/candidates/{id}`
  - Method: GET

#### Create Candidate:

- **Register a new candidate**

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

#### Update Candidate:

- **Update candidate data by providing ID**

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

#### Partial Update Candidate:

- **Update some parts of candidate data by providing ID**

  - URL: `http://127.0.0.1:8000/api/candidate/candidates/{id}`
  - Method: PATCH
  - Request Body (partial update):
    ```json
    {
        "is_staff": true,
        "email": "abc23@yahoo.com"
    }
    ```

#### Delete Candidate:

- **Delete a candidate by providing ID**

  - URL: `http://127.0.0.1:8000/api/candidate/candidates/{id}`
  - Method: DELETE

#### Permissions

- **List Candidates:** Only staff users are allowed.
- **Create Candidate:** Any user can create.
- **Retrieve Candidate:** Only the owner of the candidate can retrieve.
- **Update Candidate:** Owners and staff members can update.
- **Partial Update Candidate:** Owners and staff members can update partially.
- **Delete Candidate:** Only staff users are allowed.

### Questions

#### List Questions:

- **Get a list of all questions**

  - URL: `http://127.0.0.1:8000/api/question/questions`
  - Method: GET

#### Retrieve Question:

- **Get details of a question by ID**

  - URL: `http://127.0.0.1:8000/api/question/questions/{id}`
  - Method: GET

#### Create Question:

- **Create a new question**

  - URL: `http://127.0.0.1:8000/api/question/questions`
  - Method: POST
  - Request Body:
    ```json
    {
        "text": "Write the function to add two numbers",
        "question_type": "COD",
        "code_template": "def add(num1, num2):\r\n    pass",
        "choices": [],
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

#### Update Question:

- **Update question data by providing ID**

  - URL: `http://127.0.0.1:8000/api/question/questions/{id}`
  - Method: PUT
  - Request Body:
    ```json
    {
        "text": "What is MCQs?",
        "question_type": "MCQ",
        "code_template": null,
        "choices": [
            {
                "text": "Option A",
                "is_correct": true
            },
            {
                "text": "Option B",
                "is_correct": false
            }
       ]
        "testcases": []
    }
    ```

#### Partial Update Question:

- **Update some parts of question data by providing ID**

  - URL: `http://127.0.0.1:8000/api/question/questions/{id}`
  - Method: PATCH
  - Request Body:
    ```json
    {
        "text": "what is data type"
    }
    ```

#### Delete Question:

- **Delete a question by providing ID**

  - URL: `http://127.0.0.1:8000/api/question/questions/{id}`
  - Method: DELETE

#### Permissions

- **List Questions:** Authenticated user can access.
- **Retrieve Question:** Authenticated user can access.
- **Create Question:** Staff users are allowed.
- **Update Question:** Staff users are allowed.
- **Partial Update Question:** Staff users are allowed.
- **Delete Question:** Staff users are allowed.

### Assessment

#### List Assessments:

- **Get a list of all assessments**

  - URL: `http://127.0.0.1:8000/api/assessment/assessments`
  - Method: GET

#### Retrieve Assessment:

- **Get details of an assessment by ID**

  - URL: `http://127.0.0.1:8000/api/assessment/assessments/{id}`
  - Method: GET
  - Response Body:
  ```
    {
      "id": 10,
      "title": "Test Assessment",
      "description": "This is test assessment",
      "date_created": "2023-08-20",
      "date_updated": "2023-08-20",
      "questions": [
          {
              "id": 13,
              "text": "Write the function for sum of two no.?",
              "question_type": "COD",
              "code_template": "def sum(no1, no2):\r\n    # write your code here",
              "choices": [],
              "testcases": [
                  {
                      "id": 8,
                      "input_data": "1, 2",
                      "expected_output": "3",
                      "is_public": true
                  },
                  (testcases...)
              ]
          },
          {
              "id": 29,
              "text": "Its an mcq test1",
              "question_type": "MCQ",
              "code_template": "",
              "choices": [
                  {
                      "id": 41,
                      "text": "Option A",
                      "is_correct": true
                  },
                  (choices...)
              ],
              "testcases": []
          }
      ]
  }
  ```

#### Create Assessment:

- **Create a new assessment**

  - URL: `http://127.0.0.1:8000/api/assessment/assessments`
  - Method: POST
  - Request Body:
    ```json
    {
        "title": "Math Assignment",
        "description": "A math assignment for KG"
    }
    ```

#### Update Assessment:

- **Update assessment data by providing ID**

  - URL: `http://127.0.0.1:8000/api/assessment/assessments/{id}`
  - Method: PUT
  - Request Body:
    ```json
    {
        "title": "Math Assignment",
        "description": "Updated description",
    }
    ```

#### Partial Update Assessment:

- **Update some parts of assessment data by providing ID**

  - URL: `http://127.0.0.1:8000/api/assessment/assessments/{id}`
  - Method: PATCH
  - Request Body:
    ```json
    {
        "description": "Updated description"
    }
    ```

#### Delete Assessment:

- **Delete an assessment by providing ID**

  - URL: `http://127.0.0.1:8000/api/assessment/assessments/{id}`
  - Method: DELETE

#### Permissions

- **List Assessments:** Authenticated user can access.
- **Retrieve Assessment:** Authenticated user can access.
- **Create Assessment:** Staff users are allowed.
- **Update Assessment:** Staff users are allowed.
- **Partial Update Assessment:** Staff users are allowed.
- **Delete Assessment:** Staff users are allowed.

### Add Assessment Question

- **Add question to an assessment by id**
  - **URL:** `http://127.0.0.1:8000/api/assessment/update-question/add/`
  - **Method:** POST
  - Request Body:
  ```json
  {
    "assessment_id": 9,
    "question_id":13
  }
  ```

### Remove Assessment Question

- **Remove question to an assessment by id**
  - **URL:** `http://127.0.0.1:8000/api/assessment/update-question/remove/`
  - **Method:** POST
  - Request Body:
  ```json
  {
    "assessment_id": 9,
    "question_id":13
  }
  ```

### Save Answer

The Save Answer section provides endpoints related to answer management.

#### List Answers:

- **Get a list of all answer** 

  - URL: `http://127.0.0.1:8000/api/assessment/save-answer/`
  - Method: GET
  - Request Body:
    ```json
    [
        {
            "id": 4,
            "candidate_id": 16,
            "assessment_id": 10,
            "question_id": 29,
            "question_type": "MCQ",
            "selected_choice_id": 41,
            "code": null,
            "timestamp": "2023-08-20T15:47:34.687596Z"
        },
        {
            "id": 1,
            "candidate_id": 16,
            "assessment_id": 10,
            "question_id": 13,
            "question_type": "COD",
            "selected_choice_id": null,
            "code": "def sum(no1, no2):\r\n    return no1+no2",
            "timestamp": "2023-08-20T14:42:43.191561Z"
        }
    ]
    
    ```

#### Retrieve Answer:

- **Get details of a answer by ID**

  - URL: `http://127.0.0.1:8000/api/assessment/save-answer/{id}/`
  - Method: GET
  - Response Body:
  ```
  [
      {
          "id": 4,
          "candidate_id": 16,
          "assessment_id": 10,
          "question_id": 29,
          "question_type": "MCQ",
          "selected_choice_id": 41,
          "code": null,
          "timestamp": "2023-08-20T15:47:34.687596Z"
      },
      {
          "id": 1,
          "candidate_id": 16,
          "assessment_id": 10,
          "question_id": 13,
          "question_type": "COD",
          "selected_choice_id": null,
          "code": "def sum(no1, no2):\r\n    return no1+no2",
          "timestamp": "2023-08-20T14:42:43.191561Z"
      }
  ]
  ```

#### Save Answer:

- **Save a new Answer**

  - URL: `http://127.0.0.1:8000/api/assessment/save-answer/`
  - Method: POST
  - Request Body:
    ```json
    {
        "assessment_id":"10",
        "question_id":"13",
        "question_type": "COD",
        "code":"def sum(no1, no2):\r\n    return no1+no2"
    }
    ```

#### Update Answer:

- **Update answer data by providing ID**

  - URL: `http://127.0.0.1:8000/api/assessment/save-answer/{id}/`
  - Method: PUT
  - Request Body (full update):
    ```json
    {
        "assessment_id":"10",
        "question_id":"13",
        "question_type": "COD",
        "code":"def sum(no1, no2):\r\n    return no1+no2"
    }
    ```

#### Partial Update Answer:

- **Update some parts of answer data by providing ID**

  - URL: `http://127.0.0.1:8000/api/assessment/save-answer/{id}/`
  - Method: PATCH
  - Request Body (partial update):
    ```json
    {
        "code":"def sum(no1, no2):\r\n    return no1+no2"
    }
    ```
#### Delete Answer:

- **Delete a candidate by providing ID**

  - URL: `http://127.0.0.1:8000/api/candidate/candidates/{id}`
  - Method: DELETE

#### Permissions

- **List Answer:** Only staff users are allowed.
- **Create Answer:** Authenticated user can create.
- **Retrieve Answer:** Only the owner of the candidate can retrieve.
- **Update Answer:** Owners
- **Partial Update Answer:** Owners
- **Destroy Answer:** Only staff users are allowed

- **Remove question to an assessment by id**
  - **URL:** `http://127.0.0.1:8000/api/assessment/update-question/remove/`
  - **Method:** POST
  - Request Body:
  ```json
  {
    "assessment_id": 9,
    "question_id":13
  }
  ```

### Submit Assessment

- **Authenticated candidates can submit thier assessments with their answers**
  - **URL:** `http://127.0.0.1:8000/api/assessment/submit-assessment/`
  - **Method:** POST

  #### Request
    - **Body:**
      ```json
      {
      "assessment_id": 1,
      "answers": [
      // Answers will be automatically added through answer model
      // for particular assessment of candidate
          {
              "question_id": 1,
              "question_type": "MCQ",
              "selected_choice_id": 2
          },
          {
              "question_id": 2,
              "question_type": "COD",
              "code": "print('Hello, world!')"
          },
      ]
      }
      ```
  #### Response
    - **Status Code: 201 Created**
    - **Description: Returns Result of Assessment**
    - **data:**
    ```json
    {
      "message": "Assessment submitted successfully.",
      "percentage_score": 33.33,
      "assessment": "Demo Assignment",
      "assessment_results": [
          {
              "question": "Demo Question 2",
              "type": "MCQ",
              "selected_choice": "true",
              "correct_choice": "true",
              "score": 1
          }
      ]
    }
    ```


### Assessments Result

#### List Assessment Results:

- **Get a list of all assessment results**

  - URL: `http://127.0.0.1:8000/api/assessment/assessments-result`
  - Method: GET
  - Response Body:
  ```
    [
        {
            "id": 70,
            "score": 100.0,
            "submission_date": "2023-08-20",
            "assessment_id": 10,
            "assessment_title": "Test Assessment",
            "candidate_id": 16,
            "candidate_email": "abc12323@gmail.com",
            "result": [
                {
                    "type": "MCQ",
                    "score": 1,
                    "question": "Its an mcq test1",
                    "correct_choice": "Option A",
                    "selected_choice": "Option A"
                },
                {
                    "type": "COD",
                    "score": 1,
                    "question": "Write the function for sum of two no.?",
                    "testcase_results": [
                        {
                            "input": "1, 2",
                            "status": "Pass",
                            "duration": 0.093719,
                            "actual_output": "3",
                            "expected_output": "3"
                        },
                        {
                            "input": "15, 100",
                            "status": "Pass",
                            "duration": 0.036583,
                            "actual_output": "115",
                            "expected_output": "115"
                        }
                    ]
                }
            ]
        }
    ]
  ```

#### Retrieve Assessment Result:

- **Get details of an assessment-result by ID**

  - URL: `http://127.0.0.1:8000/api/assessment/assessments-result/{id}`
  - Method: GET

#### Permissions

- **List Assessments Result:** Staff users are allowed.
- **Retrieve Assessment Result:** Staff and Owner are allowed

## Contribution

Contributions, bug reports, and feature requests are welcome.
