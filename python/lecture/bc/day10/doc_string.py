def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name""" # doc_string
    if f_name == "" or l_name == "":
        print("You didn't provide valid inputs")
        return
    return f"Your name is {f_name.title()} {l_name.title()}"


formatted_name = format_name(
    input("What is your first name? "), input("What is your last name? ")
)
