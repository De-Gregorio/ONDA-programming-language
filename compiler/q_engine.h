#include <iostream>
#include <bitset>
#include <tuple>
#include <complex>
#include <fstream>
#include <cmath>
#define MAX_ITERATION 10000000
#define to_byte(x)  reinterpret_cast<char*>(x)
using namespace std;

// 6 5 5 8 8

template<typename T, size_t N>
class engine
{
private:
    static const int mem_size = 2097152;
    static const int reg_size = 32;
    static const int n_bit_opcode = 6;
    static const int word_size = 64;
    static const int $grp = 28;
    static const int $sp = 29;
    static const int $fp = 30;
    static const int garbage_size = 100000;
    static const bool print_all = false;
    const int computation_number;  
    int final_value;
    int sub_computation_count;
    bitset<n_bit_opcode> opcode;
    complex<double> coefficient; 
    T* memory = new T[mem_size];
    T* registers = new T[reg_size];
    T* garbage = new T[garbage_size];
    bool computation_completed = false;

    uint64_t pc = 0;    

    void reverseBitset(bitset<N>& bits)
    {
        int n = bits.size();
        for(int i = 0; i < n/2; i++){
            bool temp = bits[i];
            bits[i] = bits[n-i-1];
            bits[n-i-1] = temp;
        }
    }

    void sign_extend(T& num, int msf_bit)
    {
        // Calcola il bit di segno di num
        T sign_bit = 1 << (msf_bit - 1);
        
        // Se il bit di segno è impostato, estendi il segno
        if (num & sign_bit) 
            // Imposta tutti i bit superiori a n a 1
            num |= - (1 << msf_bit);
    }

    template<size_t n_bit_src1>
    T one_inp(bitset<N>& program_memory)
    {
        bitset<n_bit_src1> src1;
        int64_t offset = pc*32+n_bit_opcode;
        for(int i = 0; i < n_bit_src1; i++) 
            src1[i] = program_memory[(offset)+n_bit_src1-i-1];
        return src1.to_ullong();
    }
    
    template<size_t n_bit_src1, size_t n_bit_src2> 
    tuple<T, T> two_inp(bitset<N>& program_memory)
    {
        bitset<n_bit_src1> src1;
        bitset<n_bit_src2> src2;
        int64_t offset = pc*32+n_bit_opcode;
        for(int i = 0; i < n_bit_src1; i++)
            src1[i] = program_memory[(offset)+n_bit_src1-i-1];
        offset += n_bit_src1;
        for(int i = 0; i < n_bit_src2; i++)
            src2[i] = program_memory[(offset)+n_bit_src2-i-1];
        tuple<T, T> t = {src1.to_ullong(),
                         src2.to_ullong()}; 
        return t; 
    }

    template<size_t n_bit_src1, size_t n_bit_src2, size_t n_bit_src3> 
    tuple<T, T, T> three_inp(bitset<N>& program_memory)
    {
        bitset<n_bit_src1> src1;
        bitset<n_bit_src2> src2;
        bitset<n_bit_src3> src3;
        int64_t offset = pc*32+n_bit_opcode;
        for(int i = 0; i < n_bit_src1; i++)
            src1[i] = program_memory[(offset)+n_bit_src1-i-1];
        offset += n_bit_src1;
        for(int i = 0; i < n_bit_src2; i++)
            src2[i] = program_memory[(offset)+n_bit_src2-i-1];
        offset += n_bit_src2;
        for(int i = 0; i < n_bit_src3; i++)
            src3[i] = program_memory[(offset)+n_bit_src3-i-1];
        tuple<T, T, T> t = {src1.to_ullong(),
                            src2.to_ullong(),
                            src3.to_ullong()}; 
        return t;
    }

    template<size_t n_bit_src1, size_t n_bit_src2, size_t n_bit_src3, size_t n_bit_src4> 
    tuple<T, T, T, T> four_inp(bitset<N>& program_memory)
    {
        bitset<n_bit_src1> src1;
        bitset<n_bit_src2> src2;
        bitset<n_bit_src3> src3;
        bitset<n_bit_src4> src4;
        int64_t offset = pc*32+n_bit_opcode;
        for(int i = 0; i < n_bit_src1; i++)
            src1[i] = program_memory[(offset)+n_bit_src1-i-1];
        offset += n_bit_src1;
        for(int i = 0; i < n_bit_src2; i++)
            src2[i] = program_memory[(offset)+n_bit_src2-i-1];
        offset += n_bit_src2;
        for(int i = 0; i < n_bit_src3; i++)
            src3[i] = program_memory[(offset)+n_bit_src3-i-1];
        offset += n_bit_src3;
        for(int i = 0; i < n_bit_src3; i++)
            src4[i] = program_memory[(offset)+n_bit_src4-i-1];

        tuple<T, T, T, T> t = {src1.to_ullong(),
                               src2.to_ullong(),
                               src3.to_ullong(), 
                               src4.to_ullong()}; 
        return t;
    }

    void save_state(bool final_save = false)
    {
        ofstream outFile;
        if(final_save){
            outFile.open(".onda\\final_state" + to_string(computation_number) + ".bin", ios::binary);
            if(!outFile)
                cerr << "Failed to open file to save : " <<
                ".onda\\final_state" + to_string(computation_number) + ".bin" << endl;
        }else{
            outFile.open(".onda\\paused_state" + to_string(sub_computation_count) + ".bin", ios::binary);
            if (!outFile) {
                cerr << "Failed to open file to save: " <<
                ".onda\\paused_state" + to_string(sub_computation_count) + ".bin" <<
                ", final_save = " << final_save << endl;
                exit(EXIT_FAILURE);
            }
            sub_computation_count += 1;
        }


        float realPart = coefficient.real();
        float imagPart = coefficient.imag();

        outFile.write(to_byte(&realPart), sizeof(realPart));
        outFile.write(to_byte(&imagPart), sizeof(imagPart));
        outFile.write(to_byte(&pc), sizeof(pc));
        outFile.write(to_byte(registers), reg_size*sizeof(T));
        outFile.write(to_byte(memory+registers[$sp]+1), (mem_size - registers[$sp] + 2) * sizeof(T));
        outFile.write(to_byte(garbage), registers[$grp] * sizeof(T));
        outFile.close();    
        return;
    }

    void load_state(string path)
    {
        ifstream inFile(path, ios::binary);

        if (!inFile) {
            cerr << "Failed to open file for loading: " << path << endl;
            exit(EXIT_FAILURE);
            return;
        }

        float realPart, imagPart;        
        inFile.read(to_byte(&realPart), sizeof(realPart));
        inFile.read(to_byte(&imagPart), sizeof(imagPart));
        inFile.read(to_byte(&pc), sizeof(pc));
        inFile.read(to_byte(registers), reg_size*sizeof(T));
        inFile.read(to_byte(memory+registers[$sp]+1), (mem_size - registers[$sp] + 2) * sizeof(T));
        inFile.read(to_byte(garbage), registers[$grp] * sizeof(T));
        coefficient.real(realPart);
        coefficient.imag(imagPart);

        inFile.close();

        for(int i = 0; i < registers[$sp]+1; i++) memory[i] = 0;
        for(int i = registers[$grp]; i < garbage_size; i++) garbage[i] = 0;
        return;
    }

    int parity(T num, int n_bit_to_consider)
    {
        int count = 0;
        for(int i = 0; i < n_bit_to_consider; i++)
            if(num & (1 << i)) count++;
        return count % 2;
    }

    void check_errors(long long iteration)
    {
        if(pc+registers[1] < 0 || pc + registers[1] >= N / 32){
            cerr << "the program counter pc = " << pc+registers[1]+1 << 
            ", took either values over the size of the program(" << N/32 << 
            ") or is negative " << endl;
            print_state();
            exit(EXIT_FAILURE);
        }
        if(iteration > MAX_ITERATION){
            cerr << "compuation stopped because it passed the maximum_number " <<
            "of execuetable instructions: " << MAX_ITERATION << endl;
            cerr << "If this is not beacause of an infinte loop, raise the value of " << 
            "the MAX_ITERATION macro int the run_engine.cpp file and run the setup file" <<
            " to compile it again"  << endl; 
            exit(EXIT_FAILURE);
        }  
        int somma = 0;
        for(int i = 0; i < 32; i++)
            somma += registers[i] + memory[mem_size-1-i];
        if(somma != (mem_size*2-2) + registers[$grp]){
            cerr << "not all values of the memory are set to 0" << endl;
            print_state();
            exit(EXIT_FAILURE);
        }
        return;
    }

    void read_opcode(bitset<N>& program_memory)
    {
        for(int i = 0; i < n_bit_opcode; i ++) 
            opcode[i] = program_memory[(pc*32)+n_bit_opcode-i-1];
        return;
    }
    
    // 0
    void add(bitset<N>& program_memory)
    {
        // cerr<< "add" << endl;
        T dest, src;
        tie(dest, src) = two_inp<5, 5>(program_memory);
        registers[dest] += registers[src];
    }

    // 1
    void addi(bitset<N>& program_memory)
    {
        // cerr<< "addi"<< endl;
        T dest, imm;
        tie(dest, imm) = two_inp<5, 21>(program_memory);
        sign_extend(imm, 21);
        registers[dest] += imm;
    }

    // 2
    void cadd(bitset<N>& program_memory)
    {
        cerr<< "cadd" << endl;
        T cond, dest, src;
        tie(cond, dest, src) = three_inp<5, 5, 5>(program_memory);
        if(registers[cond] & 1) registers[dest] += registers[src];
    }

    // 3
    void caddi(bitset<N>& program_memory)
    {
        // cerr<< "caddi"<< endl;
        T cond, dest, imm;
        tie(cond, dest, imm) = three_inp<5, 5, 16>(program_memory);
        sign_extend(imm, 16);
        if(registers[cond] & 1) registers[dest] += imm;
    }

    // 4
    void sub(bitset<N>& program_memory)
    {
        T dest, src;
        tie(dest, src) = two_inp<5, 5>(program_memory);
        registers[dest] -= registers[src];
    }

    // 5
    void subi(bitset<N>& program_memory)
    {
        T dest, imm;
        tie(dest, imm) = two_inp<5, 21>(program_memory);
        sign_extend(imm, 21);
        registers[dest] -= imm;
    }

    // 6
    void csub(bitset<N>& program_memory)
    {
        T cond, dest, src;
        tie(cond, dest, src) = three_inp<5, 5, 5>(program_memory);
        if(registers[cond] & 1) registers[dest] -= registers[src];
    }

    // 7
    void csubi(bitset<N>& program_memory)
    {
        T cond, dest, imm;
        tie(cond, dest, imm) = three_inp<5, 5, 16>(program_memory);
        sign_extend(imm, 16);
        if(registers[cond] & 1) registers[dest] -= imm;
    }

    // 8 
    void div(bitset<N>& program_memory)
    {
        T dest, src1, src2;
        tie(dest, src1, src2) = three_inp<5, 5, 5>(program_memory);
        registers[dest] ^= registers[src1] / registers[src2];
    }

    // 9
    void divi(bitset<N>& program_memory)
    {
        T dest, src, imm;
        tie(dest, src, imm) = three_inp<5, 5, 16>(program_memory);
        sign_extend(imm, 16);
        registers[dest] ^= registers[src] / imm;
    }

    // 10
    void cdiv(bitset<N>& program_memory)
    {
        T cond, dest, src1, src2;
        tie(cond, dest, src1, src2) = four_inp<5, 5, 5, 5>(program_memory);
        if(registers[cond] & 1) registers[dest] ^= registers[src1] / registers[src2];
    }

    // 11
    void cdivi(bitset<N>& program_memory)
    {
        T cond, dest, src, imm;
        tie(cond, dest, src, imm) = four_inp<5, 5, 5, 11>(program_memory);
        sign_extend(imm, 11);
        if(registers[cond] & 1) registers[dest] ^= registers[src] / imm;
    }

    // 12
    void mul(bitset<N>& program_memory)
    {
        T dest, src1, src2;
        tie(dest, src1, src2) = three_inp<5, 5, 5>(program_memory);
        registers[dest] ^= registers[src1] * registers[src2];
    }

    // 13
    void muli(bitset<N>& program_memory)
    {
        // cerr<< "muli "<< endl;
        T dest, src1, imm;
        tie(dest, src1, imm) = three_inp<5, 5, 16>(program_memory);
        sign_extend(imm, 16);
        registers[dest] ^= registers[src1] * imm;
    }

    // 14
    void cmul(bitset<N>& program_memory)
    {
        T cond, dest, src1, src2;
        tie(cond, dest, src1, src2) = four_inp<5, 5, 5, 5>(program_memory);
        if(registers[cond] & 1) registers[dest] ^= registers[src1] * registers[src2];
    }

    // 15
    void cmuli(bitset<N>& program_memory)
    {
        T cond, dest, src, imm;
        tie(cond, dest, src, imm) = four_inp<5, 5, 5, 11>(program_memory);
        sign_extend(imm, 11);
        if(registers[cond] & 1) registers[dest] ^= registers[src] * imm;
    }

    // 16
    void swap_word_in_memory(bitset<N>& program_memory)
    {
        T src1, src2, offset;
        tie(src1, src2, offset) = three_inp<5, 5, 16>(program_memory);
        sign_extend(offset, 16);
        // cerr<< "offset = " << offset << endl;
        // cerr<< "sw R" << src1 << "  MEM " <<  registers[src2] + offset 
        // << "  (mem size = " << mem_size << ")" << endl; 
        T temp = registers[src1];
        registers[src1] = memory[registers[src2] + offset];      
        memory[registers[src2] + offset] = temp;
    }

    // 17
    void xor_sign_extended_immediate(bitset<N>& program_memory)
    {
        T src, imm;
        tie(src, imm) = two_inp<5, 21>(program_memory);
        sign_extend(imm, 21);
        registers[src] ^= imm;
    }

    // 18
    void load_upper(bitset<N>& program_memory)
    {
        // to implement
    }

    // 19
    void load_upperi(bitset<N>& program_memory)
    {
        // to implement
    }

    // 20
    void flip_on_equal(bitset<N>& program_memory)
    {
        // cerr<< "feq" << endl;
        T dest, src1, src2;
        tie(dest, src1, src2) = three_inp<5, 5, 5>(program_memory);
        if(registers[src1] == registers[src2]) registers[dest] ^= 1;
    }

    // 21
    void flip_on_equali(bitset<N>& program_memory)
    {
        cerr<< "feqi" << endl;
        T dest, src, imm;
        tie(dest, src, imm) = three_inp<5, 5, 16>(program_memory);
        sign_extend(imm, 16);
        if(registers[src] == imm) registers[dest] ^= 1; 
    }
    
    // 22
    void flip_on_not_equal(bitset<N>& program_memory)
    {
        T dest, src1, src2;
        tie(dest, src1, src2) = three_inp<5, 5, 5>(program_memory);
        if(registers[src1] != registers[src2]) registers[dest] ^= 1;
    }    

    // 23
    void flip_on_not_equali(bitset<N>& program_memory)
    {
        cerr<< "fnei: ";
        T dest, src, imm;
        tie(dest, src, imm) = three_inp<5, 5, 16>(program_memory);
        sign_extend(imm, 16);
        if(registers[src] != imm)registers[dest] ^= 1; 
    }  

    // 24
    void flip_on_less_than(bitset<N>& program_memory)
    {
        T dest, src1, src2;
        tie(dest, src1, src2) = three_inp<5, 5, 5>(program_memory);
        if(registers[src1] < registers[src2]) registers[dest] ^= 1;
    }

    // 25
    void flip_on_less_thani(bitset<N>& program_memory)
    {
        T dest, src1, imm;
        tie(dest, src1, imm) = three_inp<5, 5, 16>(program_memory);
        sign_extend(imm, 16);
        if(registers[src1] < imm) registers[dest] ^= 1;
    }

    // 26
    void no_op(bitset<N>& program_memory)
    {

    }

    // 27
    void neg(bitset<N>& program_memory)
    {
        T src;
        src = one_inp<5>(program_memory);
        registers[src] = -registers[src];
    }

    // 28
    void two_case_swap_ur(bitset<N>& program_memory)
    {
        // cerr<< "tcsu: ";
        // cerr<< registers[1]<< " " <<
        //         registers[nur1] << " " << registers[2] <<
        T nur1, nur2, activation, counter, nur;
        tie(nur1, nur2, activation, counter) = four_inp<5, 5, 5, 5>(program_memory);
        if((registers[counter] % 2) == registers[activation]){  
            nur = nur1;
        }else{
            nur = nur2;
        }
        T temp = registers[nur];
        registers[nur] = registers[1];
        registers[1] = temp;

        registers[activation] = !registers[activation];

        // cerr<< registers[1] << " " <<
        //         registers[nur1] << " " << registers[nur2] <<
        //         " " << registers[activation] << " " <<
        //         registers[counter] << endl;

    } 

    // 29
    void read_bit_at_index(bitset<N>& program_memory)
    {
        // cerr<< "rebi" << endl;
        T dest, src1, src2;
        tie(dest, src1, src2) = three_inp<5, 5, 5>(program_memory);
        registers[dest] ^= (registers[src1] >> registers[src2]) & 1;
    }

    // 30 
    void flip_first_bit(bitset<N>& program_memory)
    {
        // cerr<< "flip" << endl;
        T src;
        src = one_inp<5>(program_memory);
        registers[src] ^= 1;
        // registers[src] = registers[src] ^ (~0); flip all bits 
        // registers[src] = !registers[src]; non unitary
    }
    
    void print_state()
    {
        cerr << pc << endl;
        for(int i = 0; i < reg_size; i++)
            if(i == $sp || i == $fp){
                cerr<< "R[" << i << "] = " << registers[i] - mem_size << '\t' 
                << "MEM[" << -i-1 << "] = " << memory[mem_size-1-i] << '\t' 
                << "GAR[" << i << "] = " << garbage[i] << endl;
            }else{
                cerr<< "R[" << i << "] = " << registers[i] << '\t' 
                << "MEM[" << -i-1 << "] = " << memory[mem_size-1-i] << '\t' 
                << "GAR[" << i << "] = " << garbage[i] << endl;
            }
    }

    // 31
    void output_reg(bitset<N>& program_memory)  
    {
        T src;
        src = one_inp<5>(program_memory);
        if(src == 31){
            print_state();
        }else{
            cout << registers[src] << endl;
        }
    }

    // 32
    void swap_registers(bitset<N>& program_memory)
    {
        T src1, src2;
        tie(src1, src2) = two_inp<5, 5>(program_memory);
        // cerr<< "register[" << src1 << "] = " << registers[src1]
        // << "   resister[" << src2 << "] = " << registers[src2] << endl;   
        T t = registers[src2];
        registers[src2] = registers[src1];
        registers[src1] = t;
    }

    // 33
    void throw_away(bitset<N>& program_memory)
    {
        T src;
        src = one_inp<5>(program_memory);
        T t = garbage[registers[$grp]];
        garbage[registers[$grp]] = registers[src];
        registers[src] = t;
        registers[$grp] += 1;
        return;
    }

    // 34
    void exclusive_or(bitset<N>& program_memory)
    {
        T dest, src;
        tie(dest, src) = two_inp<5, 5>(program_memory);
        registers[dest] ^= registers[src];
        return;
    }

    // 35
    void negate(bitset<N>& program_memory)
    {
        T src;
        src = one_inp<5>(program_memory);
        registers[src] = -registers[src];
    }

    // 36
    void flip_all_bits(bitset<N>& program_memory)
    {
        T dest;
        dest = one_inp<5>(program_memory);
        registers[dest] = ~registers[dest];
    }

    // 37
    void z_gate(bitset<N>& program_memory)
    {
        T target, n_bits;
        tie(target, n_bits) = two_inp<5, 5>(program_memory);
        if(parity(registers[target], registers[n_bits]) == 1)
            coefficient *= -1;
        return;
    }

    void apply_hadamard(T r_idx, T bit_idx)
    {
        if(bit_idx < 0){
            if(registers[r_idx] == final_value) return;
            save_state();
            return;
        }
        coefficient *= (registers[r_idx] & (1 << bit_idx)) ? -1 / sqrt(2) : 1 / sqrt(2);
        complex<double> old_coeffiecient = coefficient;
        apply_hadamard(r_idx, bit_idx-1);
        coefficient = old_coeffiecient;

        coefficient *= (registers[r_idx] & (1 << bit_idx)) ? -1 : 1;

        registers[r_idx] ^= (1 << bit_idx);
        apply_hadamard(r_idx, bit_idx-1);
        registers[r_idx] ^= (1 << bit_idx);
        return;

    }

    // 38
    void hadamard_gate(bitset<N> program_memory)
    {
        T target, n_bits;
        tie(target, n_bits) = two_inp<5, 5>(program_memory);
        uint64_t mask = (1 << registers[n_bits]) - 1;
        final_value = registers[target] ^ mask; //  the last R[n_bits] bit are flipped 
        apply_hadamard(target, registers[n_bits] - 1);
        registers[target] = final_value;
        return;
    }

    // 63
    void end_program(bitset<N>& program_memory)
    {
        computation_completed = true;
    }

public:    
    engine(int init_computation_number = 0, int init_sub_computation_count = 1)
     :coefficient(1.0f, 0.0f), 
      sub_computation_count(init_sub_computation_count),
      computation_number(init_computation_number)
    {
        if(computation_number == 0){
            for(int i = 0; i < mem_size; i++) memory[i] = 0;
            for(int i = 0; i < reg_size; i++) registers[i] = 0;
            for(int i = 0; i < garbage_size; i++) garbage[i] = 0;
            registers[1] = 1;
            registers[$sp] = mem_size - 2; 
            registers[$fp] = mem_size - 1; 
        }else{
            string start_file_path = ".\\.onda\\paused_state" + to_string(computation_number) + ".bin";
            load_state(start_file_path);
        }
    }

    int get_sub_computation_count(){
        return sub_computation_count;
    }

    complex<double> get_coefficient(){
        return coefficient;
    }

    void set_pc(uint64_t new_pc){
        pc = new_pc-1;
    }


    void execute(bitset<N>& program_memory)
    {
        int iteration = 0;
        reverseBitset(program_memory);
        do
        {
            iteration++;
            pc += registers[1];
            read_opcode(program_memory);
            if(opcode == 0) {add(program_memory);   continue;}
            if(opcode == 1) {addi(program_memory);  continue;}
            if(opcode == 2) {cadd(program_memory);  continue;}
            if(opcode == 3) {caddi(program_memory); continue;}
            if(opcode == 4) {sub(program_memory);   continue;}
            if(opcode == 5) {subi(program_memory);  continue;}
            if(opcode == 6) {csub(program_memory);  continue;}
            if(opcode == 7) {csubi(program_memory); continue;}
            if(opcode == 8) {div(program_memory);   continue;}
            if(opcode == 9) {divi(program_memory);  continue;}
            if(opcode == 10) {cdiv(program_memory); continue;}
            if(opcode == 11) {cdivi(program_memory);continue;}
            if(opcode == 12) {mul(program_memory);  continue;}
            if(opcode == 13) {muli(program_memory); continue;}
            if(opcode == 14) {cmul(program_memory); continue;}
            if(opcode == 15) {cmuli(program_memory);        continue;}
            if(opcode == 16) {swap_word_in_memory(program_memory);      continue;}
            if(opcode == 17) {xor_sign_extended_immediate(program_memory);  continue;}
            if(opcode == 18) {load_upper(program_memory);   continue;}
            if(opcode == 19) {load_upperi(program_memory);  continue;}
            if(opcode == 20) {flip_on_equal(program_memory);    continue;}
            if(opcode == 21) {flip_on_equali(program_memory);   continue;}
            if(opcode == 22) {flip_on_not_equal(program_memory);    continue;}
            if(opcode == 23) {flip_on_not_equali(program_memory);   continue;}
            if(opcode == 24) {flip_on_less_than(program_memory);    continue;}
            if(opcode == 25) {flip_on_less_thani(program_memory);   continue;}
            if(opcode == 26) {no_op(program_memory);                continue;}
            if(opcode == 27) {neg(program_memory);  continue;}
            if(opcode == 28) {two_case_swap_ur(program_memory); continue;}
            if(opcode == 29) {read_bit_at_index(program_memory);    continue;}
            if(opcode == 30) {flip_first_bit(program_memory);   continue;}
            if(opcode == 31) {output_reg(program_memory);   continue;}
            if(opcode == 32) {swap_registers(program_memory);   continue;}
            if(opcode == 33) {throw_away(program_memory);   continue;}
            if(opcode == 34) {exclusive_or(program_memory); continue;}
            if(opcode == 35) {negate(program_memory);   continue;}
            if(opcode == 36) {flip_all_bits(program_memory);    continue;}
            if(opcode == 37) {z_gate(program_memory);   continue;}
            if(opcode == 38) {hadamard_gate(program_memory); continue;}
            if(opcode == 63) {end_program(program_memory);  break;}
            cerr<< "op code " << opcode << " non valido\n";
        }while(pc+registers[1] >= 0 && pc+registers[1] < N / 32 && iteration <= MAX_ITERATION);
        check_errors(iteration);
        save_state(true); // final_save = true
    }
};