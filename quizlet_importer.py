def write_to_file(question, answer, file_path):
    with open(file_path, 'a') as file:
        # Strip whitespace from the beginning and end of question and answer
        question = question.strip()
        answer = answer.strip()
        file.write(f"{question}`{answer}``")

def main():
    file_path = './qa_data.txt'

    while True:
        # Get user input for question and answer
        question = input("Enter a question (or type 'exit' to quit): ")
        
        if question.lower() == 'exit':
            break

        answer = input("Enter the answer: ")

        # Write question and answer to the file
        write_to_file(question, answer, file_path)
        print("Question and answer set written to the file.")

if __name__ == "__main__":
    main()
