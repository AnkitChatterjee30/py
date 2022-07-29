class Question:
    def __init__(self,prompt,answer):
        self.prompt=prompt
        self.answer=answer
question_prompts=[
    "What is the colour of apple ? \n(a)Red/Green \n(b)Black \n(c)Blue \n",
    "What is the capital of India ? \n(a)Kolkata \n(b)New Delhi  \n(c)Mumbai \n",
    "When did India become independent ? \n(a)15th August, 1896 \n(b) 17th July 1878 \n(c)15th August, 1947 \n",
    "How many times have Australian Cricket team won the world cup till 2020 ? \n(a)6 times \n(b)5 times \n(c)7 times \n",
    "Who had hit 6 sixes in an over in 2007 T20 world cup ? \n(a)Sachin Tendulkar \n(b)Yuvraj Singh \n(c)MS Dhoni \n"

]
questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"b"), 
    Question(question_prompts[2],"c"),
    Question(question_prompts[3],"b"),
    Question(question_prompts[4],"b"),
]
def run_test(questions):
    score=0
    print("Welcome to the Quiz ")
    name=input("Enter your name :")
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print(f"{name},you scored",str(score) ,"/" ,str(len(questions)) ,"Correct")

run_test(questions)
