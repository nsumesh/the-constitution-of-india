import os

# List of note files to combine
note_files = [
    'Preamble.txt','PART01.txt', 'PART02.txt', 'PART03.txt', 'PART04.txt', 'PART04A.txt', 
    'PART05.txt', 'PART06.txt', 'PART07.txt', 'PART08.txt', 'PART09.txt', 
    'PART09A.txt', 'PART09B.txt', 'PART10.txt', 'PART11.txt', 'PART12.txt', 
    'PART13.txt', 'PART14.txt', 'PART14A.txt', 'PART15.txt', 'PART16.txt', 
    'PART17.txt', 'PART18.txt', 'PART19.txt', 'PART20.txt', 'PART21.txt', 
    'PART22.txt', 'SCHEDULE01.txt', 'SCHEDULE02.txt', 'SCHEDULE03.txt', 'SCHEDULE04.txt', 
    'SCHEDULE05.txt', 'SCHEDULE06.txt', 'SCHEDULE07.txt', 'SCHEDULE08.txt', 
    'SCHEDULE09.txt', 'SCHEDULE10.txt', 'SCHEDULE11.txt', 'SCHEDULE12.txt'
]

# List of schedule files to combine


# Name of the combined file
combined_file = 'Constitution.txt'

with open(combined_file, 'w', encoding='utf-8') as outfile:
    for file_name in note_files:
        try:
            with open(file_name, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read() + "\n")
        except UnicodeDecodeError as e:
            print(f"Error reading {file_name}: {e}")
            continue

print(f"Combined notes and schedules saved to {combined_file}")
