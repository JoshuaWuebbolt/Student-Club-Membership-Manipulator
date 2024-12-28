import pandas as pd

from membershipList import MembershipList

dataframe = pd.read_excel('UTM Urbanism Club Membership Form (Responses).xlsx')

print("testing main.py")

membershipList = MembershipList(dataframe)
membershipList.initializeMembershipList()


quit = False

while not quit:
    print("1. Print all members\n"
          "2. Show duplicate members\n"
          "3. How many members\n"
          "4. Members with additional notes\n"
          
          "q. Quit\n")

    choice = input("Enter a number to choose: ")
    if choice == "1":
        print(membershipList)
    elif choice == "2":
        
        douplicateIndicies = membershipList.showDuplicateMembersByStudentNumber()

        print("There are " + str(len(douplicateIndicies)) + " douplicates at " + 
              str(douplicateIndicies) + 
              " Would you like to delete the duplicates? (y/n)")
        
        dele = input()

        if dele == "y" or dele == "Y":
            douplicateIndicies.sort(reverse=True)
            for i in range(len(douplicateIndicies)):
                if(douplicateIndicies[i] != douplicateIndicies[i-1]):
                    membershipList.membershipList.pop(douplicateIndicies[i])
        
    elif choice == "3":
        print("There are " + str(len(membershipList.membershipList)) + " members\n")

    elif choice == "4":
        additionalNotesIndicies = membershipList.additionalNotes()
        aditionalNotesPercentage = (len(additionalNotesIndicies)/len(membershipList.membershipList)*100)

        print("There are " + str(len(additionalNotesIndicies)) + 
              " members with additional notes. " +
              " That is " + '{:.2f}%'.format(aditionalNotesPercentage) + " of the members. " + 
              "Would you like to see the notes? (y/n)")

        if input() == "y":
            for i in additionalNotesIndicies:
                print(membershipList.membershipList[i].additional_note)





    elif choice == "q" or "Q" or "quit" or "Quit":
        quit = True









print("Exiting Program")