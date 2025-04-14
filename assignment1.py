def write_and_append_to_file(filename):
    # Step 1: Take user input and write to the file
    user_input = input("Enter some text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + '\n')

    # Step 2: Append additional data
    additional_input = input("Enter additional text to append: ")
    with open(filename, 'a') as file:
        file.write(additional_input + '\n')

    # Step 3: Read and display the final content of the file
    print("\nFinal content of the file:")
    with open(filename, 'r') as file:
        for line in file:
            print(line, end='')

# Run the function with 'output.txt'
write_and_append_to_file('output.txt')

