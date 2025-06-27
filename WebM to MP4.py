from tqdm import tqdm
from ffmpeg_progress_yield import FfmpegProgress
from os import listdir, sep, remove
from os.path import isfile, expanduser
from tkinter import Tk, filedialog, Listbox, BooleanVar
from tkinter.ttk import Button, Label, Frame, Checkbutton
from sys import argv

# TODO: Add a part at the bottom where the progress is shown
#   - Label with "state=DISABLED" to make sure the user can't edit it
#   - Progress bar has been created, shows percentage instead of frames

# Enables debugging mode if the "-d" argument is passed via command line
debugging = False
if len(argv) > 2:
    for a in argv:
        if a.lower() == "-d":
            debugging = True

# DECLARE GLOBAL VARIABLES HERE
dir_files = []
conv_files = []
folder_path = False


def open_folder():
    """Opens a folder selection box and asks the user to select a folder
    """
    global dir_files
    global folder_path

    # Has the user select the folder
    folder_path = filedialog.askdirectory(initialdir=f"{expanduser('~')}{sep}Videos", mustexist=True, title="Select a folder")
    
    # If the user doesn't select a folder, default to their Videos folder (WINDOWS ONLY)
    if not folder_path:
        folder_path = f"{expanduser('~')}{sep}Videos"
    
    # Only gets files that have the ".webm" extension
    dir_files = [f for f in listdir(folder_path) if isfile(folder_path + sep + f)]

    # Adds the webm files to the listbox
    index = 1
    for file in dir_files:
        item_list.insert(index, file)
        index += 1
    
    root.update()

def convert_single(i_file):
    """Runs the conversion of webm to mp4 through FFMPEG

    Args:
        ifile (string): Path of the file to be converted
    """
    # Switches ".webm" with ".mp4" in the filename
    o_file = ''
    for part in i_file.split(".")[0:-1]:
        o_file = o_file + part + "."
    o_file = o_file + "mp4"
    
    if debugging:
        print(f"{i_file} --> {o_file}")

    # Gets full path to item to pass to ffmpeg
    old_name = folder_path + sep + i_file
    new_name = folder_path + sep + o_file

    # Sets up the command to convert the video
    ff = FfmpegProgress([
        "ffmpeg",
        "-i",
        old_name,
        "-c:v",
        "copy",
        "-crf",
        "22",
        new_name
    ])

    # Creates the progress bar and runs the conversion
    with tqdm(total=100, position=1, desc=f"Conversion of {i_file}") as pbar:
        for progress in ff.run_command_with_progress():
            pbar.update(progress - pbar.n)

    # Deletes the original file if the option is selected
    if delete_orig.get():
        if debugging:
            print(f"Deleting {old_name}")
        
        remove(old_name)

def convert_all():
    """Button function that runs the conversion code for all requested files
    """
    global conv_files

    conv_indices = item_list.curselection()
    for ind in conv_indices:
        conv_files.append(item_list.get(ind, ind)[0])
    if type(conv_files) == 'str':
        conv_files = [str(conv_files)]
    
    for to_convert in conv_files:
        convert_single(to_convert)
        # Add a bit here that checks if the original files should be deleted and deletes them if so

root = Tk()
root.title("WEBM to MP4")
# root.iconbitmap("[path/to/icon]")
mainframe = Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=('n', 'w', 'e', 's'))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Have to put have a window initialized before declaring this
delete_orig = BooleanVar()

# ADD WIDGETS HERE
window_title = Label(mainframe, text="WEBM to MP4 Converter", font=("Arial", 16, "bold"))
item_list = Listbox(mainframe, selectmode='multiple', width=60)
select_button = Button(mainframe, text="Open folder", command=open_folder)
del_button = Checkbutton(mainframe, text="Delete original?", variable=delete_orig)
run_button = Button(mainframe, text="Convert", command=convert_all)

# PLACE WIDGETS HERE
window_title.grid(row=0, column=1)
item_list.grid(row=1, column=0, columnspan=3)
select_button.grid(row=2, column=0)
del_button.grid(row=2, column=1)
run_button.grid(row=2, column=2)

root.mainloop()