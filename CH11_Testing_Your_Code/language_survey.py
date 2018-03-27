from survey import AnonymousSurvey

# Define a questio, and make a survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store response to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_responses(response)

#Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()