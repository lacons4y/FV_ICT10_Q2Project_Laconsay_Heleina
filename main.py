from pyscript import document, display

def general_weighted_average(e):
    # Gets the student's first and last name from the input fields
    firstname = document.getElementById("first_name").value
    lastname = document.getElementById("last_name").value

    # Gets the student's grades from the input fields
    # float() converts the input (text) into a number we can calculate with
    science = float(document.getElementById("science").value)
    english = float(document.getElementById("english").value)
    math = float(document.getElementById("math").value)
    socialstudies = float(document.getElementById("socialstudies").value)
    filipino = float(document.getElementById("filipino").value)
    ict = float(document.getElementById("ict").value)

    # Subjects list now matches input order and summary display
    subjects = ['Science', 'English', 'Math', 'Social Studies', 'Filipino', 'ICT']

    # Calculates the weighted sum of all grades
    # Each subject is multiplied by its corresponding number of units
    weighted_sum = (
        science * 5 +
        english * 5 +
        math * 5 +
        socialstudies * 4 +
        filipino * 3 +
        ict * 2
    )

    # Total number of units for all subjects combined
    total_units = (5 * 3) + 4 + 3 + 2

    # Computes the General Weighted Average (GWA)
    gwa = weighted_sum / total_units

    # Create a formatted summary showing each subject and its grade
    # ".0f" removes decimal places when displaying grades
    summary = f"""\
{subjects[0]}: {science:.0f}
{subjects[1]}: {english:.0f}
{subjects[2]}: {math:.0f}
{subjects[3]}: {socialstudies:.0f}
{subjects[4]}: {filipino:.0f}
{subjects[5]}: {ict:.0f}
"""

    # Displays the student's name, grade summary, and GWA on the webpage
    display(f"Name: {firstname} {lastname}", target="student_info")
    display(summary, target="summary")
    display(f"Your general weighted average is {gwa:.2f}", target="output")


# This dictionary stores information about each school club
# The club name is the key, and the value is another dictionary with details
club_info = {
    "Communication Arts Club": {
        "Name": "Communication Arts Club",
        "Description": "A club for people who like to make different forms of art.",
        "Meeting time": "Wednesday & Friday 03:00 - 04:00 PM",
        "Location": "Room 406",
        "Club Moderator": "Ms. Yannis Fernandez",
        "Number of members": "15",
        "Category": "Non-Academic"
    },
    "Dance Club": {
        "Name": "Dance Club",
        "Description": "A club for people who love dancing.",
        "Meeting time": "Tuesday 03:00 - 05:00 PM",
        "Location": "Teatro Preciosa",
        "Club Moderator": "Mr. Alfred Cases",
        "Number of members": "25",
        "Category": "Non-Academic"
    },
    "Band Club": {
        "Name": "Band Club",
        "Description": "A club for those interested in playing musical instruments.",
        "Meeting time": "Tuesday & Wednesday",
        "Location": "Band Room",
        "Club Moderator": "Mr. Emilio Alumno",
        "Number of members": "25",
        "Category": "Non-Academic"
    },
    "Glee Club": {
        "Name": "Glee Club",
        "Description": "A club for those who love to sing.",
        "Meeting time": "Monday 03:00 - 05:00 PM",
        "Location": "High School Music Room",
        "Club Moderator": "Mr. Denver Martin",
        "Number of members": "15",
        "Category": "Non-Academic"
    },
    "Math Club": {
        "Name": "Math Club",
        "Description": "A club for people who enjoy solving mathematical problems.",
        "Meeting time": "Monday 02:30 - 03:00 PM",
        "Location": "Room 404",
        "Club Moderator": "Mr. Gabriel Gabuya",
        "Number of members": "10",
        "Category": "Academic"
    },
    "Science Club": {
        "Name": "Science Club",
        "Description": "A club for those who enjoy science.",
        "Meeting time": "Tuesday 03:00 - 04:00 PM",
        "Location": "Room 404",
        "Club Moderator": "Ms. Jameelyn Maramag",
        "Number of members": "10",
        "Category": "Academic"
    }
}


def clubinfo(e):
    # Gets the selected club name from the dropdown menu
    selected = document.getElementById("club-select").value
    info = club_info.get(selected)  # Retrieves the corresponding club data

    # Formats the club information clearly and consistently
    if info:
        output = (
            f"Club Name: {info['Name']}\n"
            f"Description: {info['Description']}\n"
            f"Meeting Time: {info['Meeting time']}\n"
            f"Location: {info['Location']}\n"
            f"Club Moderator: {info['Club Moderator']}\n"
            f"Number of Members: {info['Number of members']}\n"
            f"Category: {info['Category']}"
        )
    else:  # If no club is found, show a fallback message
        output = "No information available."

    # Display the club information in the designated HTML element
    document.getElementById("club_info").innerText = output

