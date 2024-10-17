#include <iostream>
#include <bitset>
#include <string>
#include "q_engine.h"
#define N 500
using namespace std;
// TO DO 
// save the program in binary


void execute_first_engine(bitset<N*32>& program_memory, int intial_pc)
{
    engine<int64_t> e(0, 1);
    e.set_pc(intial_pc);
    e.execute(program_memory);
    cout << e.get_sub_computation_count() << " " << e.get_coefficient() << endl;
    return;
}

void execute_secodary_engine(bitset<N*32>& program_memory, int intial_sub_computation_count,
                             int computation_number)
{
    string state_file_path = "engine_state" + to_string(computation_number) + ".bin";
    engine<int64_t> e(computation_number, intial_sub_computation_count);
    e.execute(program_memory);
    cout << e.get_sub_computation_count() << " " << e.get_coefficient() << endl;
    return;
}

bitset<N*32> build_bitset(string& program)
{
    int p_len = program.size();
    if(p_len / 32 >= N){
        cerr << "program is too long: program is " << 
        p_len / 32 << " instructions long, the max allowed is " <<
        N-1 << endl;
        return 1;
    }
    string zeros(26, '0');
    program += "111111" + zeros;
    p_len += 32;
    bitset<N*32> program_memory(program);
    program_memory <<= N*32 - p_len;
    return program_memory;
}


int main(int argc, char* argv[])
{
    // argv[1] = intial pc / initial_sub_computation_count 
    // program memory file
    // computation number 
    int first_arg = atoi(argv[1]);
    string input_file = argv[2];
    int computation_number = atoi(argv[3]);

    freopen(input_file.c_str(), "r", stdin);
    string program; cin >> program;
    bitset<N*32> program_memory = build_bitset(program);
    
    if(computation_number == 0) execute_first_engine(program_memory, first_arg);
    else execute_secodary_engine(program_memory, first_arg, computation_number);
    return 0;
}