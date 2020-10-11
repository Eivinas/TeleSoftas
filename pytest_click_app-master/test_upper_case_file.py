# Tests script upper_case_file by comparing new compiled files with referenced files from data folder
# data folder files must have *input.txt/*output.txt in their name.
# To run: pytest 
import pytest
import upper_case_file 
import click
import os
import shutil
from os import listdir
from os.path import isfile, join
from upper_case_file import upper_case_file
from click.testing import CliRunner

class TestUperCaseClass():
    def setup_class(self):
        input_files_list = []
        output_files_list = []
        all_files_list = [f for f in listdir("data/") if isfile(join("data/", f))]
        i = 0     
                
        # Create temp dir in current path
        path = str(os.getcwd()) + "/temp"
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)
              
        # Fill input and output lists with text files from data folder
        for file in all_files_list:
            if "input" in file:
                input_files_list.append(file)
            else:
                output_files_list.append(file)

        # Run program for each input file in data folder and send output to temp folder
        for file in output_files_list:
            runner = CliRunner()
            result = runner.invoke(upper_case_file, [
                "--input-file", str("data/" + input_files_list[i]),
                "--output-file", str("temp/" + output_files_list[i])
            ])
            i = i + 1   
   
    # Removes temp dir with all files in it
    def teardown_class(self):
        path = str(os.getcwd()) + "/temp"
        try:
            shutil.rmtree(path)
        except OSError:
            print ("\n Deletion of the directory %s failed" % path)
        else:
            print ("\n Successfully deleted the directory %s" % path)


    # Checks if temp dir and data dir all output.txt files matches
    def test_upper_case_file(self):
        errors = []
        temp_output_files_list = [f for f in listdir("temp/") if isfile(join("temp/", f))]
        for file in temp_output_files_list:
            f_data = open("data/" + file, "r")
            f_temp = open("temp/" + file, "r")  
            data_orig =  f_data.read()
            data_temp =  f_temp.read()
            if data_orig != data_temp:
                errors.append(str(file) + " not matching ")
            f_data.close() 
            f_temp.close()   
        assert not errors, "errors occured:\n{}".format("\n".join(errors))
