# import pandas lib as pd
import pandas as pd

from member import Member


# read by default 1st sheet of an excel file
#dataframe = pd.read_excel('UTM Urbanism Club Membership Form (Responses).xlsx')

#print(dataframe)

class MembershipList:
    """Holds a list of members of the club
    """




    def __init__(self, dataframe) -> None:
        self.dataframe = dataframe
        self.membershipList = []



    def createMember(self, line) -> Member:
        """Creates a Member object from the data on the first line in the excel file
        """

        return Member(line[1], line[2], line[3], line[4], line[5], line[6])


    def initializeMembershipList(self) -> None:
        """Initializes the membership list with the data from the excel file
        """
        for row in self.dataframe.itertuples():
            #membershipList.append(createMember(row))
            self.membershipList.append(self.createMember(row))
            # print("R")
            # print(row)

    

    def __str__(self) -> str:

        for member in self.membershipList:
            print(member) 

        return ""
    
    def showDuplicateMembersByStudentNumber(self) -> list[int]:
        """Shows duplicate members in the membership list
        """
        douplicateNumber = 0
        douplicateIndices = []

        for i in range(len(self.membershipList)):
            if(self.membershipList[i].student_number == "-" or self.membershipList[i].student_number == " "):
                continue
            match = False
            for j in range(i+1, len(self.membershipList)):
                if self.membershipList[i].student_number == self.membershipList[j].student_number:
                    if not match:
                        print(self.membershipList[i])
                        match = True
                    print(self.membershipList[j])
                    douplicateNumber += 1
                    douplicateIndices.append(j)
            if match:
                print("\n")

        #print("Total number of duplicate members: " + str(douplicateNumber) + "\n")
        #print(douplicateIndices)
        return douplicateIndices       

    def additionalNotes(self) -> list[int]:
        """Shows members with additional notes
        """
        notes = []

        for i in range(len(self.membershipList)):
            if(self.membershipList[i].additional_note != None):
                notes.append(i)
        return notes




