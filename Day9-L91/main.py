# Auction



studentScoresDict={
    "K.Weir":89,
    "C.Unt": 58,
    "B.Lowhard":77,
    "M.Ike-Hunt":82,
    "F.Udge-Pack":89
}


def classAverage(studentScores):

    classAvg=0

    #Get average
    gradesSum=0
    for element in studentScores:
        gradesSum +=studentScores[element]

    classAvg = gradesSum/len(studentScores)

    return classAvg


def printStudentScoreGrade(studentScores):

    for element in studentScores:
        gradeLabel=""
        print("Student: " + element)
        studentScore=studentScores[element]
        print("Score: " + str(studentScore))
        if studentScore > 80:
            gradeLabel="Your shits dopest"
            # elif
            #elif
            #else bla bla
        elif studentScore < 60:
            gradeLabel = "Not great at this"
        else:
            gradeLabel = "OK"

        print("Grade: " + gradeLabel)


print("Average: " + str(classAverage(studentScoresDict)))

print(printStudentScoreGrade(studentScoresDict))