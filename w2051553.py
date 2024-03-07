# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20230071
# Date: 3/12/2023
from graphics import *

# initiate variables to count different progression outcomes
progress = 0
exclude = 0
trailer = 0
retriever = 0

# Store progression data for later display
progression_data = []

# Define possible credit values
credit_values = {0, 20, 40, 60, 80, 100, 120}

# Calculate the total number of students with different progression outcomes
total_prog = progress + exclude + trailer + retriever

# Function to determine progression outcome based on pass and fail credits
def progress_outcome(pass_credit, fail_credit):
    credit_volume = 120
    global progress, exclude, trailer, retriever, total_prog
    
    if pass_credit == credit_volume:
        result = 'Progress'
        progress += 1
    elif fail_credit >= 80:
        result = 'Exclude'
        exclude += 1
    elif pass_credit == 100:
        result = 'Progress(Module trailer)'
        trailer += 1
    else:
        result = 'Module retriever'
        retriever += 1
    total_prog = progress + exclude + trailer + retriever
    return result

# Function to take user input, calculate progression outcome, and display a graphical representation
def main():
    while True:
        try:
            pass_credit = int(input('\nEnter pass credit: '))
            defer_credit = int(input('Enter defer credit: '))
            fail_credit = int(input('Enter fail credit: '))
            # Store the entered data for later display
            progression_data.append([pass_credit, defer_credit, fail_credit])

            # Check if credits are within valid ranges and add up to the total credit volume
            if pass_credit in credit_values and defer_credit in credit_values and fail_credit in credit_values:
                if pass_credit+defer_credit+fail_credit == 120:
                    print(progress_outcome(pass_credit, fail_credit))
                else:
                    print('Total incorrect')
            else:
                print('Out of range')
        except ValueError:
            print('Integer required')

        # Ask the user if they want to enter another set of data or quit
        key_letter = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
        if key_letter.lower() == 'q':
            
            # Graph representing progression outcomes              
            win = GraphWin("Progression Outcome", 600, 500)
            win.setBackground("White")

            my_heading = Text(Point(100, 50), 'Progression Outcome')
            my_heading.draw(win)

            bar_1 = Rectangle(Point(40, win.getHeight()-20), Point(40+50, win.getHeight()-20-progress*10))
            bar_1.setFill('blue')
            bar_1.draw(win)
            text_1 = Text(Point(40+25, win.getHeight()-28-progress*10), progress)
            text_11 = Text(Point(40+25, win.getHeight()-10), 'Progress')
            text_1.draw(win)
            text_11.draw(win)

            bar_2 = Rectangle(Point(120, win.getHeight()-20), Point(120+50, win.getHeight()-20-trailer*10))
            bar_2.setFill('blue')
            bar_2.draw(win)
            text_2 = Text(Point(120+25, win.getHeight()-28-trailer*10), trailer)
            text_22 = Text(Point(120+25, win.getHeight()-10), 'Trailer')
            text_2.draw(win)
            text_22.draw(win)

            bar_3 = Rectangle(Point(210, win.getHeight()-20), Point(210+50, win.getHeight()-20-retriever*10))
            bar_3.setFill('blue')
            bar_3.draw(win)
            text_3 = Text(Point(210+25, win.getHeight()-28-retriever*10), retriever)
            text_33 = Text(Point(210+25, win.getHeight()-10), 'Retriever')
            text_3.draw(win)
            text_33.draw(win)

            bar_4 = Rectangle(Point(290, win.getHeight()-20), Point(290+50, win.getHeight()-20-exclude*10))
            bar_4.setFill('blue')
            bar_4.draw(win)
            text_4 = Text(Point(290+25, win.getHeight()-28-exclude*10), exclude)
            text_44 = Text(Point(290+25, win.getHeight()-10), 'Excluded')
            text_4.draw(win)
            text_44.draw(win)

            line_1 = Line(Point(20, win.getHeight()-19), Point(win.getWidth()-20, win.getHeight()-19))
            line_1.draw(win)

            text_tot = Text(Point(470, 200), str(int(total_prog)) + " outcomes in total")
            text_tot.draw(win)

            win.getMouse()
            win.close()

            break

# Execute the main function if this script is run           
if __name__ == "__main__":
    main()

# Function to display progression data from list
def display_progression_data():
    for data in progression_data:                     
        result = progress_outcome(data[0], data[2])       
        print(result, f"- {data[0]}, {data[1]}, {data[2]}")            
print('\nPart. 2')
display_progression_data()

# Function to display progression data from text file             
def display_progression_text():
    for data in progression_data:
        f = open('cwt.txt', 'w')
        result = progress_outcome(data[0], data[2])
        f_result = "{}, {}, {}".format(data[0], data[1], data[2])
        f.write(str(result))
        f.write(' - ')
        f.write(str(f_result))             
        f.close()  
        f = open('cwt.txt', 'r')
        data_text = f.read()
        print(data_text)
print('\nPart. 3')
display_progression_text()



             
                 
                 
        


             
          


    










 


  
