## Report of Monaco 2018 Racing
#### What is it?

A package that reads data from 3 files start.log, end.log and abbreviation that contain start and end data of the best
lap for each racer of Formula 1 - Monaco 2018 Racing and abbreviation explanations, orders racers by time and print
report that shows the top 15 racers and the rest after underline.
____
#### How to use an application via the command line?

The application has a few parameters:
- files - the name of the folder that contains start, end and abbreviation files 
- asc / desc - optional order (default order is asc)
- driver - shows statistic about driver

###### Examples:
- python command_line.py --files <folder_path> [--asc | --desc]
- python command_line.py --files <folder_path> --driver “Sebastian Vettel”

