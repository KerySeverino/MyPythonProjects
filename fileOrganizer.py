import os
import shutil

image_extension = (".jpg", ".jpeg", ".png", ".gif", ".webp")
video_extension = (".webm", ".mov", ".mp4", ".m4p", ".m4v")
document_extension = (".doc", ".docx", ".pdf", ".txt", ".key")
code_extension = (".py", ".java" ,".html", ".css", ".js", ".sql", ".cpp", ".c")

# For mac: right click and press (option) on your keyboard, this allows you to copy the path name.  
#Path name of where you want the files to go / direct directory.
ddir = "/Users/keryseverinodiaz/Downloads"

#Checks if the files (exists), if not it (creates) them.
# Create subdirectories if they don't exist
subdirectories = ["Images", "Videos", "Documents", "Code", "Other"]
for subdir in subdirectories:
    path = os.path.join(ddir, subdir)
    if not os.path.exists(path):
        os.makedirs(path)

#Gets the file extensions
def get_image(file):
    return os.path.splitext(file)[1] in image_extension

def get_video(file):
    return os.path.splitext(file)[1] in video_extension

def get_document(file):
    return os.path.splitext(file)[1] in document_extension

def get_code(file):
    return os.path.splitext(file)[1] in code_extension

for file in os.listdir(ddir):
    #Checks if the file is in the (directory)
    if os.path.isdir(ddir + "/" + file):
        continue

    if get_image(file):
        shutil.move(ddir + "/" + file, ddir + "/Images")
    elif get_video(file):
        shutil.move(ddir + "/" + file, ddir + "/Videos")
    elif get_document(file):
        shutil.move(ddir + "/" + file, ddir + "/Documents")
    elif get_code(file):
        shutil.move(ddir + "/" + file, ddir + "/Code")
