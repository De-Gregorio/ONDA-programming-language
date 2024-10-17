import os
import subprocess
import shutil
import struct
import numpy as np 

class ParallelComputationsHandler():
    def __init__(self):
        self.results = {}

    def get_coeff(self, file_path): # DOESN'T WORK
        with open(file_path, "rb") as file: # rb meand read binary
            data = file.read(16)
            real, imag = struct.unpack('dd', data)  # 'ff' means two floats
            return real, imag
        
    def check_equal(self, comp1, comp2, folder_path = ".onda"):
        file1 = os.path.join(folder_path, "final_state" + str(comp1) + ".bin")
        file2 = os.path.join(folder_path, "final_state" + str(comp2) + ".bin")
        with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
            f1.seek(16)
            f2.seek(16)
            
            content1 = f1.read()
            content2 = f2.read()

            return content1 == content2
        
    def merge(self, comp1, comp2, folder_path = ".onda\\"):
        file1 = os.path.join(folder_path, "final_state" + str(comp1) + ".bin")
        file2 = os.path.join(folder_path, "final_state" + str(comp2) + ".bin")

        self.results[comp1][0] += self.results[comp2][0]
        del self.results[comp2]
        os.remove(file2)
        


    def merge_equal_states(self, compututation_count, folder_path = ".onda"):
        seen = []  # List to store seen files
        for comp in range(compututation_count):
            duplicate = False
            for seen_comp in seen:
                if self.check_equal(comp, seen_comp):  
                    self.merge(seen_comp, comp)
                    duplicate = True
                    break
            
            if not duplicate: seen.append(comp)



    def sort_queue(self):
        pass

    
    def build_folder(self, folder_path = ".onda"):
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)



    def run_parallel_computations(self, entry_point, exeFile, to_show_results = True):
        try:
            self.build_folder()
        except Exception as e:
            raise NameError(f"An error has occured: {e}")
        result = []
        sub_computation_count = int(entry_point) # only at the first computation
                                            # the argument reserved for sub_comp_count
                                            # indicates the inital pc value
        self.compuations_queued = [0] # list od IDs
        while len(self.compuations_queued) > 0:
            current_computation_id = self.compuations_queued[0]
            execution =  subprocess.run(["./compiler/run_engine.exe", 
                                         str(sub_computation_count), 
                                         exeFile, 
                                         str(current_computation_id)], 
                                         capture_output=True, text=True) 
            if execution.stderr  != "":
                raise NameError(f"in computation {current_computation_id}:\n{execution.stdout}\n{execution.stderr}") 

            intermediate_results = execution.stdout.split("\n")
            # the last 2 numbers of the stdout are 
            # the sub_computation_count and the
            # coefficient
            old_sub_computation_count = sub_computation_count
            sub_computation_count, coefficient = intermediate_results[-2].split()
            sub_computation_count = int(sub_computation_count)
            new_computations_queued = [i for i in range(old_sub_computation_count, sub_computation_count)]
            self.compuations_queued.extend(new_computations_queued)

            coefficient = complex(*eval(coefficient))

            result = [coefficient, [value for value in intermediate_results[:-2]]]

            self.sort_queue()
            
            self.results[current_computation_id] = result
            inital_file = os.path.join(".onda", 
                                       "paused_state" + str(self.compuations_queued[0]) + ".bin")
            if self.compuations_queued[0] != 0:
                os.remove(inital_file)
            self.compuations_queued.pop(0)

        self.merge_equal_states(sub_computation_count)
        if to_show_results: self.show_results()
        return self.results()
            

    def show_results(self):
        sorted_keys = sorted(self.results.keys(), key=lambda k: abs(self.results[k][0]))
        total = complex(0, 0)
        for key in reversed(sorted_keys):
            coeff = self.results[key][0]
            total += abs(coeff)**2
            print(f"comp n{key}:\t{coeff}\t", end="\t")
            if len(str(coeff)) < 8: print("\t", end="")
            for el in self.results[key][1]:
                print(el, end = "\t")
            print(f"{abs(coeff)**2:.5f}", end = "\t")
            print()
        

        