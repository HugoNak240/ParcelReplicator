import shutil
import os
from classes.Pathfinder import Pathfinder

"""
assign contents of chosen folder as list of samples 
list of quality control samples to be copied/moved into workorder directories
create qcDest object, subdir_paths
"""

parcel = os.listdir(
    "/Users/hugonak/Desktop/ProgramPractice/githubrepo/ParcelReplicator_local/ParcelReplicator/parcel")
parcel_list = " ".join(parcel)
subdir_paths = Pathfinder()


"""
Format for menu text
    print('{:s}'.format('\u0332').join(''))

menu for application
MUST HAVE
    5 avaiable options
        add, delete, change analyte, execute, quit
    show current list of quality control samples
"""


def menu():
    print('{:s}'.format('\u0332').join('ParcelReplicator'))
    print('{:s}'.format('\u0332').join('Place samples into "parcel" folder'))
    print('{:s}'.format('\u0332').join(
        'Current list of samples :') + parcel_list)
    print("1. Choose Analyte")
    print("2. Enter Workorders")
    print("3. Delete Workorder")
    print("4. Show Workorder list")
    print("5. Execute")
    print("6. Quit")
    userChoice = 0
    while userChoice == 0:
        userChoice = int(input("Select Action Number: "))
        if userChoice == 1:
            os.system('clear')
            subdir_paths.change_AC()
            userChoice = 0
            menu()
        elif userChoice == 2:
            os.system('clear')
            subdir_paths.add_workorder()
            userChoice = 0
            menu()
        elif userChoice == 3:
            os.system('clear')
            subdir_paths.delete_workorder()
            menu()
            userChoice = 0
        elif userChoice == 4:
            os.system('clear')
            subdir_paths.show_list()
            userChoice = 0
            menu()
        elif userChoice == 5:
            os.system('clear')
            srcflder = "/Users/hugonak/Desktop/ProgramPractice/githubrepo/ParcelReplicator_local/ParcelReplicator/parcel"
            woDB = "/Users/hugonak/Desktop/ProgramPractice/githubrepo/ParcelReplicator_local/ParcelReplicator/ExampleDB"
            execute = ""
            execute = input("Enter EXE to initiate application: ")

            # Creates duplicates in target subdirectory
            # nested for loop
            # OUTER: iterates through workorders <- subdir's
            #     INNER: iterates and copy each parcel item from list to each subdir <- p
            if execute == "EXE":
                for wo in subdir_paths.workorders:
                    for samp in parcel:
                        sample = os.path.join(srcflder, samp)
                        half_path = os.path.join(woDB, wo)
                        full_path = os.path.join(
                            half_path, subdir_paths.sampletype)
                        shutil.copy2(sample, full_path)
                userChoice = 0
                menu()
            else:
                userChoice = 0
                menu()
        elif userChoice == 6:
            exit()


menu()
