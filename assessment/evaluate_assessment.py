from question.models import Question
from .code_executor import execute_testcases


def evaluate_mcq(answer_data, question):
    selected_choice_id = answer_data["selected_choice_id"]
    selected_choice = question.choices.get(id=selected_choice_id)
    correct_choice = question.choices.get(is_correct=True)

    score = 1 if selected_choice.id == correct_choice.id else 0

    return {
        "selected_choice": selected_choice.text,
        "correct_choice": correct_choice.text,
        "score": score,
    }


def evaluate_cod(answer_data, question):
    code = answer_data["code"]
    testcases = question.testcases.all()
    all_testcases_passed = True
    testcase_results = []
    for testcase in testcases:
        testcase_input = testcase.input_data
        testcase_output = testcase.expected_output
        result = execute_testcases(
            bytes(code, "utf-8"), testcase_input, testcase_output
        )
        testcase_results.append(result)

        if result.get("status") == "Fail":
            all_testcases_passed = False

    score = 1 if all_testcases_passed else 0
    return {
        "score": score,
        "testcase_results": testcase_results,
    }


def evaluate_assessment(assessment, answers):
    total_score = 0
    assessment_results = []

    for answer_data in answers:
        question_id = answer_data["question_id"]
        question_type = answer_data["question_type"]

        question = Question.objects.get(pk=question_id)
        question_result = {"question": question.text, "type": question_type}

        if question_type == "MCQ":
            mcq_result = evaluate_mcq(answer_data, question)
            question_result.update(mcq_result)
            total_score += mcq_result["score"]

        elif question_type == "COD":
            cod_result = evaluate_cod(answer_data, question)
            question_result.update(cod_result)
            total_score += cod_result["score"]

        assessment_results.append(question_result)

    total_questions = assessment.questions.count()
    percentage_score = float(f"{(total_score / total_questions) * 100:.2f}")

    return percentage_score, assessment_results


def assessment_response(percentage_score, assessment, assessment_results):
    return {
        "message": "Assessment submitted successfully.",
        "percentage_score": percentage_score,
        "assessment": assessment.title,
        "assessment_results": assessment_results,
    }
