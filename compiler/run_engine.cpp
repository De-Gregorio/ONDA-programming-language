#include <iostream>
#include <bitset>
#include <string>
#include "q_engine.h"
#define N 200
using namespace std;

int main(int argc, char* argv[])
{
    int entry_point = std::atoi(argv[1]);
    string input_file = argv[2];
    freopen(input_file.c_str(), "r", stdin);
    string program; cin >> program;
    int p_len = program.size();
    if(p_len / 32 >= N){
        cout << "program is too long: program is " << 
        p_len / 32 << " instructions long, the max allowed is " <<
        N-1;
        return 1;
    }
    string zeros(26, '0');
    program += "111111" + zeros;
    p_len += 32;
    bitset<N*32> program_memory(program);
    program_memory <<= N*32 - p_len;
    engine<int64_t> e;
    e.set_pc(entry_point);
    // cout << program_memory << endl;
    e.execute(program_memory);
    return 0;
}