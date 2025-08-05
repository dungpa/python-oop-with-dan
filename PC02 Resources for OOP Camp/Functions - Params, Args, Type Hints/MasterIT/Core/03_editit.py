# Edit this program by calling the 'output_fruit_message' function three times, using these arguments for each call
# - "apples"
# - "strawberries"
# - "bananas"
def output_fruit_message(fruit: str):
    if fruit == "apples":
        print("I do like apples")
    elif fruit == "bananas":
        print("Bananas go well with almost anything")
    elif fruit == "strawberries":
        print("Some strawberries and cream is a nice combination")
    else:
        print(f"I don't mind {fruit}")
