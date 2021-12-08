### Marius Filomeno Maurstad 2021 ###
#    HPC backup reminder program    #
#####################################

# Import the modules
import argparse
import datetime
import os

# Here is the program
parser = argparse.ArgumentParser()


# Add an argument
parser.add_argument('--name', help = "Name for backup object that needs to be updated in 20 days.")
parser.add_argument('--remove', help = "Remove backup object from list of objects to be backed up.")
parser.add_argument('--remind', action='store_true', help = "List of backup objects and their end date before backup")

# Parse the arguments
args = parser.parse_args()

# Get the path to the script folder
file_path = os.path.realpath(__file__)
path_to_write_file = file_path.replace("bkup.py","backup_objects.txt")


if args.name is not None:
    # Returns the current local date
    today = datetime.datetime.now()

    # Set a backup time of 20 days
    backup_before = today + datetime.timedelta(days=20)
    backup_before_formatted = args.name + "\t" +  backup_before.strftime("%d-%m-%Y %H:%M") + "\n"


    with open(path_to_write_file, "a") as f:
        f.write(backup_before_formatted)


if args.remove is not None:
    with open(path_to_write_file, "r") as f:
        lines = f.readlines()
    
    with open(path_to_write_file, "w") as f: 
        for line in lines:
            line_to_remove = line.split("\t")
            if line_to_remove[0].strip("\n") != args.remove:
                write_new_to_file = "\t".join(line_to_remove)
                f.write(write_new_to_file)

if args.remind is not None:
    with open(path_to_write_file, "r") as f:
        print(f.read())