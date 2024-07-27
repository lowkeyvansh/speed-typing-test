import time

def typing_test():
    # Text to be typed
    test_text = "The quick brown fox jumps over the lazy dog."
    
    print("Type the following text as quickly as you can:")
    print(f"\n{test_text}\n")
    
    # Prompt user to start typing
    input("Press Enter when you are ready to start...")
    
    # Record the start time
    start_time = time.time()
    
    # Get the user input
    user_input = input("\nStart typing: ")
    
    # Record the end time
    end_time = time.time()
    
    # Calculate the time taken
    time_taken = end_time - start_time
    
    # Check if the user's input matches the test text
    if user_input == test_text:
        print(f"\nCorrect! You typed the text in {time_taken:.2f} seconds.")
    else:
        print("\nText did not match. Please try again.")
        print(f"Time taken: {time_taken:.2f} seconds")

if __name__ == "__main__":
    typing_test()
