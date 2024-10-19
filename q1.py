class InvalidGradeError(Exception):
    """Custom exception for invalid grade values."""
    pass

def read_file(filename):
    try:
        with open(f"{filename}.txt", mode='r') as f:
            contents = f.read().splitlines()  # Read the file line by line
            total_score = 0
            valid_scores_count = 0
            
            for line in contents:
                try:
                    name, grade = line.split(', ')
                    print(f"Student: {name}, Grade: {grade}")
                    # Try to convert the grade to an integer
                    score = int(grade)
                    if score < 0 or score > 100:
                        raise InvalidGradeError(f"{name} has an invalid grade: {grade}")
                    
                    # Add to the total score for calculating average
                    total_score += score
                    valid_scores_count += 1
                
                except ValueError:
                    # Handle cases where grade is not a number
                    raise InvalidGradeError(f"{name} has an invalid grade: {grade}")
            
            # Calculate and display the average if there are valid scores
            if valid_scores_count > 0:
                average = total_score / valid_scores_count
                print(f"\nThe average grade of the students is: {average:.2f}")
            else:
                print("\nNo valid grades found to calculate an average.")
    
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except InvalidGradeError as e:
        print(f"Error: {e}")

# Test the function
read_file("student_records")
