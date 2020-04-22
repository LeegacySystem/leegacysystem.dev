import os
import shutil
import argparse


parser = argparse.ArgumentParser(description='Script to convert Jekyll posts to Hugo.')
parser.add_argument('-i', '--input', help='Folder containg jekyll formatted posts')
parser.add_argument('-o', '--output', help='destination folder for Hugo posts')
args = parser.parse_args()

jekyll = args.input
hugo = args.output


print(f'There are {len(os.listdir(jekyll))} items in the "{jekyll}" directory.')
response = input("Is this correct? (y/n):")

checkResonse = lambda x: None if x.lower().strip()[0] == "y" else exit(1)
checkResonse(response)

for file in os.listdir(jekyll):
#  print(f'''
#  Renaming      {file} 
#  To:           {file[11:]}
#  Moving to:    {hugo}/{file[11:]}
#  ''')

  shutil.copy(f'{jekyll}/{file}', f'{hugo}/{file[11:]}')
#  print(f'{jekyll}{file}', f'{hugo}{file[11:]}')