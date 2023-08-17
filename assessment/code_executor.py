import epicbox
from .func_call_gen import generate_function_call

epicbox.configure(
    profiles=[
        epicbox.Profile('python', 'python:3.11-alpine')
    ]
)

def execute_testcases(code, testcases_input, testcase_output):
    """
    Execute a series of test cases using a dynamically generated function call.

    Args:
    ----
        code (str): The user-provided function code.
        testcases_input (str): Comma-separated string of test case arguments.
        testcase_output (str): Expected output for given testcase input.

    Returns:
    -------
        dict: A dictionary containing the execution result.
    """
    generated_call = generate_function_call(code, testcases_input)

    if generated_call:
        combined_code = code + generated_call
        files = [{'name': 'main.py', 'content': combined_code}]
        resource_limits = {'cputime': 1, 'memory': 128}
        result = epicbox.run('python', 'python3 main.py', stdin=testcases_input, files=files, limits=resource_limits)
        output = result['stdout'].decode('utf-8').strip()
        duration = result['duration']
        is_passed = output == testcase_output
        testcase_result = {
                "input": testcases_input,
                "expected_output": testcase_output,
                "actual_output": output,
                "status": "Pass" if is_passed else "Fail",
                "duration": duration
            }
        print(testcase_result)
        return testcase_result
    else:
        return {"error": "Mismatch in argument counts between user code and test case input."}

