import os

ANALYTE_CHOICES = {1: 'PFAS', 2: 'DIOXIN', 3: 'PCB', 4: 'PEST'}

"""
for qcDest
all we need is a list of of workorders and analysis to build file path
only cycle through list of workorders 
"""


class Pathfinder():
    def __init__(self):
        self.workorders = []

    # def __repr__(self):
    #     os.path("/Users/hugonak/Desktop/ProgramPractice/COPY_MOVE_QC/CopyMove/SampleFolder/"+self.workorders+"/"+self.sampletype)
    #     return print(self.workorders)

    def change_AC(self):
        self.sampletype = ANALYTE_CHOICES[int(
            input("1:PFAS, 2:DIOXIN, 3:PCB, 4:PEST "))]
        return print("Sampletype set to - "+self.sampletype)

    def add_workorder(self):
        status = False
        ready = ""
        while status is False:
            workorder = str(input("Enter Workorder Number to Add: "))
            self.workorders.append(workorder)
            print(workorder + " was added to WO list")
            # print("bug bug bug")
            ready = str(input("Have all workorders been added?"))
            ready = ready.upper()
            if ready == "YES":

                status = True

    def delete_workorder(self):
        status = False
        ready = ""
        while status is False:
            workorder = str(input("Enter Workorder Number to Delete: "))
            self.workorders.remove(workorder)
            print(workorder + " was deleted to WO list")
            ready = str(input("Would you like to remove more?"))
            ready = ready.upper()
            if ready == "NO":
                status = True

    def show_list(self):
        woList = " ".join(self.workorders)
        print("Current list of workorders : " + woList)
