import shutil
import os
from classes import Pathfinder

"""
assign contents of chosen folder as list of samples 
list of quality control samples to be copied/moved into workorder directories
create qcDest object, subdir_paths
"""

parcel = os.listdir(
    "/Users/hugonak/Desktop/ProgramPractice/githubrepo/COPY_MOVE_QC_gh/CopyMoveQC/CopyMove/SampleFolder")
parcel_list = " ".join(parcel)
subdir_paths = Pathfinder()


"""
menu for application
MUST HAVE
    5 avaiable options
        add, delete, change analyte, execute, quit
    show current list of quality control samples
"""


def menu():
    print("COPY_MOVE_QC")
    print("Place samples to copy and move into selected SampleFolder")
    print("Current list of samples :" + parcel_list)
    print("1. Choose Analyte")
    print("2. Enter Workorders")
    print("3. Delete Workorder")
    print("4. Show Workorder list")
    print("5. Execute CopyMove")
    print("6. Quit")
    userChoice = 0
    while userChoice == 0:
        userChoice = int(input("Select Action Number: "))
        if userChoice == 1:
            subdir_paths.change_AC()
            userChoice = 0
            menu()
        elif userChoice == 2:
            subdir_paths.add_workorder()
            userChoice = 0
            menu()
        elif userChoice == 3:
            subdir_paths.delete_workorder()
            menu()
            userChoice = 0
        elif userChoice == 4:
            subdir_paths.show_list()
            userChoice = 0
            menu()
        elif userChoice == 5:

            srcflder = "/Users/hugonak/Desktop/ProgramPractice/githubrepo/COPY_MOVE_QC_gh/CopyMoveQC/CopyMove/SampleFolder/"
            woDB = "/Users/hugonak/Desktop/ProgramPractice/githubrepo/COPY_MOVE_QC_gh/CopyMoveQC/CopyMove/WorkOrderDB"
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
