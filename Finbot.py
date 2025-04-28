# Define function for the Chatbot logic predefined questions and responses
def simple_chatbot(user_query):
    if user_query == "What was Tesla's total revenue in 2024?":
        return "Tesla's total revenue in 2024 was 391 billion dollars."
    elif user_query == "What was Apple's net income in 2022?":
        return "Apples' net income in 2022 was 99 billion dollars."
    elif user_query == "Which company had the highest profit margin in the last financial year?":
        return "The company that had the highest profit margin in the last yera, 2024, was Microsoft."    
    elif user_query == "Which company had the highest net income growth in 2024?":
        return "The company with the highest net income growth in 2024 was Microsoft."
    elif user_query == "In which year did the 3 companies have an increase in revenue growth?":
        return "All 3 companies had an increase in revenue growth in 2024."
    else:
        return "Sorry, I can only provide information on predefined queries."

# Define function to make chatbot function interactive
while True:
    user_query = input("Ask me a financial question (or type 'exit' to quit): ")
    if user_query.lower() == "exit":
        print("Goodbye!")
        break
    response = simple_chatbot(user_query)
    print(response)
