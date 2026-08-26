#list of dect key value  pair
questions = [
    {
        "question": "Who is known as the 'King in the North' at the beginning of the series?",
        "options": ["A) Jon Snow", "B) Robb Stark", "C) Ned Stark", "D) Balon Greyjoy"],
        "answer": "C"
    },
    {
        "question": "What is the official motto of House Stark?",
        "options": ["A) Fire and Blood", "B) Winter is Coming", "C) Hear Me Roar", "D) Growing Strong"],
        "answer": "B"
    },
    {
        "question": "Which creature is featured on the sigil of House Targaryen?",
        "options": ["A) Lion", "B) Direwolf", "C) Dragon", "D) Stag"],
        "answer": "C"
    },
    {
        "question": "What is the name of Arya Stark's sword?",
        "options": ["A) Needle", "B) Ice", "C) Longclaw", "D) Oathkeeper"],
        "answer": "A"
    },
    {
        "question": "Who is responsible for the creation of the Night King?",
        "options": ["A) The Lord of Light", "B) The First Men", "C) The Children of the Forest", "D) Valyrians"],
        "answer": "C"
    },
    {
        "question": "What is the capital city of the Seven Kingdoms where the Iron Throne sits?",
        "options": ["A) Winterfell", "B) King's Landing", "C) Dragonstone", "D) Braavos"],
        "answer": "B"
    },
    {
        "options": ["A) Joffrey Baratheon", "B) Viserys Targaryen", "C) Tywin Lannister", "D) Robb Stark"],
        "question": "Who orchestrates the infamous event known as the 'Red Wedding' along with Walder Frey?",
        "answer": "C"
    },
    {
        "question": "What is the name of the massive ice structure that guards the northern border of the Seven Kingdoms?",
        "options": ["A) The Shield", "B) The Wall", "C) The Frostfangs", "D) The Great Barrier"],
        "answer": "B"
    },
    {
        "question": "Which city is home to the Faceless Men and the House of Black and White?",
        "options": ["A) Pentos", "B) Meereen", "C) Volantis", "D) Braavos"],
        "answer": "D"
    },
    {
        "question": "What rare and powerful material is capable of killing White Walkers?",
        "options": ["A) Valyrian Steel", "B) Wildfire", "C) Ironwood", "D) Cast Iron"],
        "answer": "A"
    }
]
def quiz(question_list):
    point=0
    question_number=1
    print("------welcome to GAME OF THRONES quiz--------")
    for i in question_list:#[{},{},{}]- for first i ={}
        print("Question"+str(question_number)+":"+i["question"]) # should be string or else error will occur cuz you cant add string and integer
        for option in i["options"]:
            print(option)
        user_choice=input("enter your answer\n")
        if user_choice == "a": user_choice = "A"
        if user_choice == "b": user_choice = "B"
        if user_choice == "c": user_choice = "C"
        if user_choice == "d": user_choice = "D"
        if user_choice==i["answer"]:
            print("✅coolllll you did it.....correct answer")
            point=point+1
            print(f"you scored {point} points")
        else:
            print("❌ go watch game of thrones ")
        question_number+=1
    print("your quiz ended")
    print(f"your final score is {point}/{len(question_list)}")

quiz(questions)
        
