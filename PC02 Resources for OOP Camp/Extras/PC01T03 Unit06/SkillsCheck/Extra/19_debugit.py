# Fix the errors in this program
def validate_subject() -> str:
    while True:
        subject = input("Enter your favourite subject: ")
        if subject in ["maths", "science", "english", "computing", "art", "french", "german", "p.e", "r.e",
                       "p.s.e", "history", "geography"]:
            return subject


your_subject = validate[]
print(f"I like {your_subject} too!")
