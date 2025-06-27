import random, sys, getopt, time
from tqdm import tqdm

# Takes command-line arguments to help streamline the process
opts, args = getopt.getopt(sys.argv[1:], "hn:l:u:o:")

for opt, arg in opts:
    # Shows a help message if needed
    if opt == '-h':
        print("""This script generates text files containing random numbers, with one number per line
              
              Usage: number_generator.py [args]
              -h: Show this message
              -n* (int): The number of random numbers needed
              -l* (int): The lower bound of generation (inclusive)
              -u* (int): The upper bound of generation (inclusive)
              -o* (str): The output filename (without extension!)
              -f (str): The output file type (if not specified, will be .txt)
              
              * = required (any arguments not specified will be asked by the program)
              
              Any arguments not explicitly defined here are ignored
              """)
        sys.exit()
    # The rest of these set the variables as explained above
    elif opt == '-n':
        num_of_nums = int(arg)
    elif opt == '-l':
        lower_bound = int(arg)
    elif opt == '-u':
        upper_bound = int(arg)
    elif opt == '-o':
        output_filename = arg
    elif opt == '-f':
        file_extension = arg
    else:
        pass    # This makes sure that any other args don't break the program (hopefully)

# Gets the necessary info from the user if it isn't given as an argument
if 'num_of_nums' not in globals():
    num_of_nums = int(input('Number of random numbers: '))
if 'lower_bound' not in globals():
    lower_bound = int(input('Lower bound of generation: '))
if 'upper_bound' not in globals():
    upper_bound = int(input('Upper bound of generation: '))
if 'output_filename' not in globals():
    output_filename = input('Output filename: ')
if 'file_extension' not in globals():
    file_extension = 'txt'
    
# Changes the time between generations based on how many numbers are needed
sleep_time = 0
if num_of_nums > 200:
    sleep_time = 0.005
elif 200 > num_of_nums >= 100:
    sleep_time = 0.01
elif 100 > num_of_nums >= 50:
    sleep_time = 0.125
elif 50 > num_of_nums >= 25:
    sleep_time = 0.25
elif 25 > num_of_nums:
    sleep_time = 0.5

# Generates the numbers into a list for exporting to a file
nums = []

for i in tqdm(range(num_of_nums)):
    nums.append(f'{random.randint(lower_bound, upper_bound)}\n')
    time.sleep(sleep_time)

# Outputs the numbers to a file
with open(f'{output_filename}.{file_extension}', 'a') as o_file:
    o_file.writelines(nums)

# Let the user know that the file was created
print(f'{output_filename} created!')
time.sleep(5)