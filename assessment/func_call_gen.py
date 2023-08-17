import ast


def generate_function_call(user_code, testcases_input):
    """
    Generate a function caller code based on user code and test case input.

    Args:
    ----
        user_code (bytes): Byte representation of the user's function code.
        testcases_input (str): Comma-separated string of test case arguments.

    Returns:
    -------
        bytes: Byte representation of the function caller code.
    """
    try:
        parsed_code = ast.parse(user_code)
    except SyntaxError:
        return False
    function_name = parsed_code.body[0].name
    user_args = parsed_code.body[0].args.args
    testcases_args = [arg.strip() for arg in testcases_input.split(",")]

    if len(user_args) != len(testcases_args):
        return False

    args_str = ""
    for i, arg in enumerate(testcases_args):
        if arg != "True" and arg != "False" and not arg.isnumeric():
            args_str += f"'{arg}'"
        else:
            args_str += arg

        if i != len(testcases_args) - 1:
            args_str += ", "

    return bytes(f"\r\nprint({function_name}({args_str}))", "utf-8")
