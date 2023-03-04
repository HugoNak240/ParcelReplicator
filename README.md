### File Manager Application: ParcelReplicator

## Description:

This application replicates a parcel of files to multiple subdirectories by using the python library tool, shutil. Initial intention is to automate a laboratory admin task, copy and paste quality control sample of the same type into multiple client workorder subdirectories. 

## How to use:

Clone repository and place files for replication into 'parcel' folder. Application is able to present list of files. 
Start application and enter the required inputs:
  1. Workorder number (string)
  2. Sample Type (string)
Select choice to input workorders and enter one at a time (loop until users enters string "yes"). Workorder numbers need to be typed in accurately (7 digit string) or application will crash. Then users must select from a set of
sample type or anlayte. Input matching number (single integer) to set analyte. These two inputs control where the files are 
copied. Users are also able to delete workorders from the list by selecting that option and again typing in the workorder number accurately (7 digit string). When ready, users select the 'execute' option and the app will prompt, enter 'EXE'.  
