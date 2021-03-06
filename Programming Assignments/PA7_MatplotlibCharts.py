##*************************************************************************
##  Charts using matplotlib.
##  Programmer: Ariadna Ayala
##  Status: Completed 
##  The program displays three different charts: line chart, bar chart, and pie graph.
##  1) The Line Graph shows the Cost of 2 years of attendance (60 credit hours) of most
##     popular colleges in Central Texas. The data was taken from ACC web-site.
##  2) The Bar Chart shows displays average salary of software engineer depending on his/her
##     experience (Intern, Junior, Middle, and Senior).
##  3) The Pie chart only gives one chance to make a mistake in the format of the input. After 2nd mistake you will have
##     to start program over again.
##*************************************************************************


def main():                                                                 # Main function contains
    import matplotlib.pyplot as pie                                         # matplotlib import for
    import matplotlib.pyplot as plt                                         # each following function.
    import matplotlib.pyplot as bar

    def linegraph():                                                        # Plotting and Displaying the graph
        school = [0, 1, 2, 3, 4, 5]                                         # Each school and cost unit
        cost = [0, 0.51, 2.07, 2.08, 2.18, 6.09]                            # have a pre-assigned value.
        plt.plot(school, cost, marker='*')                                  # Plotting the graph.
        plt.title('Ariadna Ayala \n Tuition Cost per Semester')             # Assigning the Title.
        plt.xlabel('School')                                                # Assigning meaning to x-axis.
        plt.ylabel('Cost for 2 Years (60 Credit Hours)')                    # Assigning meaning to y-axis.
        plt.xticks([0,1,2,3,4,5],                                           # Assigning names to each value
                   ['0','ACC','Texas A&M','UT','Texas State',               # on x-axis.
                    'Avg.Private'])
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7],                                # Assigning names to each value
                   ['$0', '$10.0k', '$20.0k', '$30.0k', '$40.0k',           # on y-axis.
                    '$50.0k','$60.0k', '$70k'])
        plt.grid(True)                                                      # Adding grid.
        plt.show()                                                          # Displaying the graph.
    linegraph()

    show1 = input('Type "next" to display next graph: ')                    # When user is ready, type "next"
    show1 = show1.strip().lower()                                           # to display the next Graph.
    while show1 == 'next':                                                  # Won't work with numeric input and
                                                                            # input other than "next" in any form.
                                                                            # Using loop to show next graph.


        def bargraph():                                                     # Plotting and Displaying the graph,
            level = [0, 1, 2, 3, 4]                                         # this graph has similar structure to the
            salary = [0, 1, 2, 3, 4]                                        # Line graph above.
            b_width = 1
            bar.bar(level,salary,b_width, color=('m', 'y', 'm', 'y',        # Playing with color.
                                  'm', 'y'))
            bar.title('Ariadna Ayala \n Salary of a Software Engineer Depending on Experience ')
            bar.xlabel('Experience Level')
            bar.ylabel('Annual Salary in Thousands USD')
            plt.xticks([0, 1, 2, 3, 4],
                       ['0', 'Intern', 'Junior', 'Middle', 'Senior'])
            plt.yticks([0, 1, 2, 3, 4],
                       ['$0', '$62k', '$80k', '$102k', '$112'])
            bar.show()                                                      # Displaying the graph

        bargraph()
        break                                                               # Breaking the infinite loop,
                                                                            # otherwise graph will display non-stop


    show2 = input('Type "next" to display next graph: ')                    # When user is ready, type "next"
    show2 = show2.strip().lower()                                           # to display the next Graph.
                                                                            # Won't work with numeric input and
                                                                            # input other than "next" in any form.
    while show2 == 'next':                                                  # Using loop to show next graph.

        def piechart():
            try:                                                            # Collecting data from user & testing it
                val1 = float(input('Enter your 1st numeric value: '))
                val2 = float(input('Enter your 2nd numeric value: '))
                val3 = float(input('Enter your 3rd numeric value: '))
            except Exception as err:                                        # In case of error, will give another
                print('An error occured. Try again.',                       # chance to input numeric data.
                      ' Make sure the data is numeric')                     # If failed after 2nd try - restart program.
                val1 = float(input('Enter your 1st numeric value: '))
                val2 = float(input('Enter your 2nd numeric value: '))
                val3 = float(input('Enter your 3rd numeric value: '))

            finally:                                                        # Display the Pie chart using user's data.
                    pie.pie([val1, val2, val3],labels=['Value 1', 'Value 2', 'Value 3'])
                    pie.title('Ariadna Ayala \n A chart for your data:')
                    pie.show()

        piechart()
        break                                                               # Breaking the infinite loop.
    print('\n')
    print('This program is written by Ariadna Ayala')
main()
