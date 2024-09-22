#include <iostream>
#include <bitset>
#include <tuple>
#define MAX_ITERATION 10000000
using namespace std;

// 6 5 5 8 8

template<typename T>
class engine
{
private:
    static const int mem_size = 2097152;
    static const int reg_size = 32;
    static const int garbage_size = 100000;
    static const int n_bit_opcode = 6;
    static const int word_size = 64;
    static const int $grp = 28;
    static const int $sp = 29;
    static const int $fp = 30;
    T* memory = new T[mem_size];
    T* registers = new T[reg_size];
    T* garbage = new T[garbage_size];
    bool computation_completed = false;

    uint64_t pc = 0;    

    template <size_t N>
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
        int32_t sign_bit = 1 << (msf_bit - 1);
        
        // Se il bit di segno è impostato, estendi il segno
        if (num & sign_bit) 
            // Imposta tutti i bit superiori a n a 1
            num |= - (1 << msf_bit);
    }

    template<size_t N, size_t n_bit_src1>
    T one_inp(bitset<N>& program_memory)
    {
        bitset<n_bit_src1> src1;
        int64_t offset = pc*32+n_bit_opcode;
        for(int i = 0; i < n_bit_src1; i++) 
            src1[i] = program_memory[(offset)+n_bit_src1-i-1];
        return src1.to_ullong();
    }
    
    template<size_t N, size_t n_bit_src1, size_t n_bit_src2> 
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

    template<size_t N, size_t n_bit_src1, size_t n_bit_src2, size_t n_bit_src3> 
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

    template<size_t N, size_t n_bit_src1, size_t n_bit_src2, size_t n_bit_src3,
    size_t n_bit_src4> 
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

    template <size_t N> // 0
    void add(bitset<N>& program_memory)
    {
        // cerr<< "add" << endl;
        T dest, src;
        tie(dest, src) = two_inp<N, 5, 5>(program_memory);
        registers[dest] += registers[src];
    }

    template <size_t N> // 1
    void addi(bitset<N>& program_memory)
    {
        // cerr<< "addi"<< endl;
        T dest, imm;
        tie(dest, imm) = two_inp<N, 5, 21>(program_memory);
        sign_extend(imm, 21);
        registers[dest] += imm;
    }

    template <size_t N> // 2
    void cadd(bitset<N>& program_memory)
    {
        cerr<< "cadd" << endl;
        T cond, dest, src;
        tie(cond, dest, src) = three_inp<N, 5, 5, 5>(program_memory);
        if(registers[cond] & 1) registers[dest] += registers[src];
    }

    template <size_t N> // 3
    void caddi(bitset<N>& program_memory)
    {
        // cerr<< "caddi"<< endl;
        T cond, dest, imm;
        tie(cond, dest, imm) = three_inp<N, 5, 5, 16>(program_memory);
        sign_extend(imm, 16);
        if(registers[cond] & 1) registers[dest] += imm;
    }

    template <size_t N> // 4
    void sub(bitset<N>& program_memory)
    {
        T dest, src;
        tie(dest, src) = two_inp<N, 5, 5>(program_memory);
        registers[dest] -= registers[src];
    }

    template <size_t N> // 5
    void subi(bitset<N>& program_memory)
    {
        T dest, imm;
        tie(dest, imm) = two_inp<N, 5, 21>(program_memory);
        sign_extend(imm, 21);
        registers[dest] -= imm;
    }

    template <size_t N> // 6
    void csub(bitset<N>& program_memory)
    {
        T cond, dest, src;
        tie(cond, dest, src) = three_inp<N, 5, 5, 5>(program_memory);
        if(registers[cond] & 1) registers[dest] -= registers[src];
    }

    template <size_t N> // 7
    void csubi(bitset<N>& program_memory)
    {
        T cond, dest, imm;
        tie(cond, dest, imm) = three_inp<N, 5, 5, 16>(program_memory);
        sign_extend(imm, 16);
        if(registers[cond] & 1) registers[dest] -= imm;
    }

    template <size_t N> // 8 
    void div(bitset<N>& program_memory)
    {
        T dest, src1, src2;
        tie(dest, src1, src2) = three_inp<N, 5, 5, 5>(program_memory);
        registers[dest] ^= registers[src1] / registers[src2];
    }

    template <size_t N> // 9
    void divi(bitset<N>& program_memory)
    {
        T dest, src, imm;
        tie(dest, src, imm) = three_inp<N, 5, 5, 16>(program_memory);
        sign_extend(imm, 16);
        registers[dest] ^= registers[src] / imm;
    }

    template <size_t N> // 10
    void cdiv(bitset<N>& program_memory)
    {
        T cond, dest, src1, src2;
        tie(cond, dest, src1, src2) = four_inp<N, 5, 5, 5, 5>(program_memory);
        if(registers[cond] & 1) registers[dest] ^= registers[src1] / registers[src2];
    }

    template <size_t N> // 11
    void cdivi(bitset<N>& program_memory)
    {
        T cond, dest, src, imm;
        tie(cond, dest, src, imm) = four_inp<N, 5, 5, 5, 11>(program_memory);
        sign_extend(imm, 11);
        if(registers[cond] & 1) registers[dest] ^= registers[src] / imm;
    }

    template <size_t N> // 12
    void mul(bitset<N>& program_memory)
    {
        T dest, src1, src2;
        tie(dest, src1, src2) = three_inp<N, 5, 5, 5>(program_memory);
        registers[dest] ^= registers[src1] * registers[src2];
    }

    template <size_t N> // 13
    void muli(bitset<N>& program_memory)
    {
        // cerr<< "muli "<< endl;
        T dest, src1, imm;
        tie(dest, src1, imm) = three_inp<N, 5, 5, 16>(program_memory);
        sign_extend(imm, 16);
        registers[dest] ^= registers[src1] * imm;
    }

    template <size_t N> // 14
    void cmul(bitset<N>& program_memory)
    {
        T cond, dest, src1, src2;
        tie(cond, dest, src1, src2) = four_inp<N, 5, 5, 5, 5>(program_memory);
        if(registers[cond] & 1) registers[dest] ^= registers[src1] * registers[src2];
    }

    template <size_t N> // 15
    void cmuli(bitset<N>& program_memory)
    {
        T cond, dest, src, imm;
        tie(cond, dest, src, imm) = four_inp<N, 5, 5, 5, 11>(program_memory);
        sign_extend(imm, 11);
        if(registers[cond] & 1) registers[dest] ^= registers[src] * imm;
    }

    template <size_t N>  // 16
    void swap_word_in_memory(bitset<N>& program_memory)
    {
        T src1, src2, offset;
        tie(src1, src2, offset) = three_inp<N, 5, 5, 16>(program_memory);
        sign_extend(offset, 16);
        // cerr<< "offset = " << offset << endl;
        // cerr<< "sw R" << src1 << "  MEM " <<  registers[src2] + offset 
        // << "  (mem size = " << mem_size << ")" << endl; 
        T temp = registers[src1];
        registers[src1] = memory[registers[src2] + offset];      
        memory[registers[src2] + offset] = temp;
    }

    template <size_t N> // 17
    void xor_sign_extended_immediate(bitset<N>& program_memory)
    {
        T src, imm;
        tie(src, imm) = two_inp<N, 5, 21>(program_memory);
        sign_extend(imm, 21);
        registers[src] ^= imm;
    }

    template <size_t N> // 18
    void load_upper(bitset<N>& program_memory)
    {
        // to implement
    }

    template <size_t N> // 19
    void load_upperi(bitset<N>& program_memory)
    {
        // to implement
    }

    template <size_t N> // 20
    void flip_on_equal(bitset<N>& program_memory)
    {
        // cerr<< "feq" << endl;
        T dest, src1, src2;
        tie(dest, src1, src2) = three_inp<N, 5, 5, 5>(program_memory);
        if(registers[src1] == registers[src2]) registers[dest] ^= 1;
    }

    template <size_t N> // 21
    void flip_on_equali(bitset<N>& program_memory)
    {
        cerr<< "feqi" << endl;
        T dest, src, imm;
        tie(dest, src, imm) = three_inp<N, 5, 5, 16>(program_memory);
        sign_extend(imm, 16);
        if(registers[src] == imm) registers[dest] ^= 1; 
    }
    
    template <size_t N> // 22
    void flip_on_not_equal(bitset<N>& program_memory)
    {
        T dest, src1, src2;
        tie(dest, src1, src2) = three_inp<N, 5, 5, 5>(program_memory);
        if(registers[src1] != registers[src2]) registers[dest] ^= 1;
    }    

    template <size_t N> // 23
    void flip_on_not_equali(bitset<N>& program_memory)
    {
        cerr<< "fnei: ";
        T dest, src, imm;
        tie(dest, src, imm) = three_inp<N, 5, 5, 16>(program_memory);
        sign_extend(imm, 16);
        if(registers[src] != imm)registers[dest] ^= 1; 
    }  

    template <size_t N> // 24
    void flip_on_less_than(bitset<N>& program_memory)
    {
        T dest, src1, src2;
        tie(dest, src1, src2) = three_inp<N, 5, 5, 5>(program_memory);
        if(registers[src1] < registers[src2]) registers[dest] ^= 1;
    }

    template <size_t N> // 25
    void flip_on_less_thani(bitset<N>& program_memory)
    {
        T dest, src1, imm;
        tie(dest, src1, imm) = three_inp<N, 5, 5, 16>(program_memory);
        sign_extend(imm, 16);
        if(registers[src1] < imm) registers[dest] ^= 1;
    }

    template <size_t N> // 26
    void no_op(bitset<N>& program_memory)
    {

    }

    template <size_t N> // 27
    void neg(bitset<N>& program_memory)
    {
        T src;
        src = one_inp<N, 5>(program_memory);
        registers[src] = -registers[src];
    }

    template <size_t N> // 28
    void two_case_swap_ur(bitset<N>& program_memory)
    {
        // cerr<< "tcsu: ";
        // cerr<< registers[1]<< " " <<
        //         registers[nur1] << " " << registers[2] <<
        T nur1, nur2, activation, counter, nur;
        tie(nur1, nur2, activation, counter) = four_inp<N, 5, 5, 5, 5>(program_memory);
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

    template <size_t N> // 29
    void read_bit_at_index(bitset<N>& program_memory)
    {
        // cerr<< "rebi" << endl;
        T dest, src1, src2;
        tie(dest, src1, src2) = three_inp<N, 5, 5, 5>(program_memory);
        registers[dest] ^= (registers[src1] >> registers[src2]) & 1;
    }

    template <size_t N> // 30 
    void flip(bitset<N>& program_memory)
    {
        // cerr<< "flip" << endl;
        T src;
        src = one_inp<N, 5>(program_memory);
        registers[src] ^= 1;
        // registers[src] = registers[src] ^ (~0); flip all bits 
        // registers[src] = !registers[src]; non unitary
    }
    
    template <size_t N> // 31
    void output_reg(bitset<N>& program_memory)  
    {
        T src;
        src = one_inp<N, 5>(program_memory);
        cerr << pc << endl;
        if(src == 31){
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
        }else{
            cout << "outr " << registers[src] << endl;
        }
    }

    template <size_t N> // 32
    void swap_registers(bitset<N>& program_memory)
    {
        T src1, src2;
        tie(src1, src2) = two_inp<N, 5, 5>(program_memory);
        // cerr<< "register[" << src1 << "] = " << registers[src1]
        // << "   resister[" << src2 << "] = " << registers[src2] << endl;   
        T t = registers[src2];
        registers[src2] = registers[src1];
        registers[src1] = t;
    }

    template <size_t N> // 33
    void throw_away(bitset<N>& program_memory)
    {
        T src;
        src = one_inp<N, 5>(program_memory);
        if(registers[$grp] % word_size != 0) {
            cerr<< "segmantation fault (i have no idea what it is)" << endl;
            exit(EXIT_FAILURE);
        }
        T t = garbage[registers[$grp] / word_size];
        garbage[registers[$grp] / word_size] = registers[src];
        registers[src] = t;
        registers[$grp] += word_size;
        return;
    }

    template <size_t N> // 34
    void load_from_garbage(bitset<N>& program_memory)
    {
        T src;
        src = one_inp<N, 5>(program_memory);    
        int64_t gp_value = registers[$grp];
        registers[src] ^= (garbage[gp_value/word_size] >> (gp_value%word_size)) & 1;
    }

    template <size_t N> // 35
    void negate(bitset<N>& program_memory)
    {
        T src;
        src = one_inp<N, 5>(program_memory);
        registers[src] = -registers[src];
    }

    template <size_t N> // 63
    void end_program(bitset<N>& program_memory)
    {
        computation_completed = true;
    }

public:    
    engine()
    {
        for(int i = 0; i < mem_size; i++) memory[i] = 0;
        for(int i = 0; i < reg_size; i++) registers[i] = 0;
        registers[1] = 1;
        registers[$sp] = mem_size - 2; // $sp
        registers[$fp] = mem_size - 1; // $fp
    }

    void set_pc(uint64_t new_pc)
    {
        pc = new_pc-1;
    }

    template <size_t N>
    void execute(bitset<N>& program_memory)
    {
        int iteration = 0;
        bitset<n_bit_opcode> opcode;
        reverseBitset(program_memory);
        do
        {
            iteration++;
            // if(registers[1] != 1){
            //     cerr << pc << " jump to " << pc + registers[1] << endl;
            // }
            pc += registers[1];
            for(int i = 0; i < n_bit_opcode; i ++) 
                opcode[i] = program_memory[(pc*32)+n_bit_opcode-i-1];
            // cerr<< " " << opcode << " " << endl;
            // transform this in a switch case
            if(opcode == 0) {add(program_memory);  continue;}
            if(opcode == 1) {addi(program_memory); continue;}
            if(opcode == 2) {cadd(program_memory);  continue;}
            if(opcode == 3) {caddi(program_memory); continue;}
            if(opcode == 4) {sub(program_memory);  continue;}
            if(opcode == 5) {subi(program_memory); continue;}
            if(opcode == 6) {csub(program_memory);  continue;}
            if(opcode == 7) {csubi(program_memory); continue;}
            if(opcode == 8) {div(program_memory);            continue;}
            if(opcode == 9) {divi(program_memory);          continue;}
            if(opcode == 10) {cdiv(program_memory);     continue;}
            if(opcode == 11) {cdivi(program_memory);      continue;}
            if(opcode == 12) {mul(program_memory); continue;}
            if(opcode == 13) {muli(program_memory); continue;}
            if(opcode == 14) {cmul(program_memory);  continue;}
            if(opcode == 15) {cmuli(program_memory);     continue;}
            if(opcode == 16) {swap_word_in_memory(program_memory);    continue;}
            if(opcode == 17) {xor_sign_extended_immediate(program_memory);               continue;}
            if(opcode == 18) {load_upper(program_memory);                 continue;}
            if(opcode == 19) {load_upperi(program_memory);          continue;}
            if(opcode == 20) {flip_on_equal(program_memory);   continue;}
            if(opcode == 21) {flip_on_equali(program_memory); continue;}
            if(opcode == 22) {flip_on_not_equal(program_memory);    continue;}
            if(opcode == 23) {flip_on_not_equali(program_memory);        continue;}
            if(opcode == 24) {flip_on_less_than(program_memory);       continue;}
            if(opcode == 25) {flip_on_less_thani(program_memory);  continue;}
            if(opcode == 26) {no_op(program_memory);                continue;}
            if(opcode == 27) {neg(program_memory);     continue;}
            if(opcode == 28) {two_case_swap_ur(program_memory);                continue;}
            if(opcode == 29) {read_bit_at_index(program_memory);            continue;}
            if(opcode == 30) {flip(program_memory);            continue;}
            if(opcode == 31) {output_reg(program_memory);            continue;}
            if(opcode == 32) {swap_registers(program_memory); continue;}
            if(opcode == 33) {throw_away(program_memory); continue;}
            if(opcode == 34) {load_from_garbage(program_memory); continue;}
            if(opcode == 35) {negate(program_memory); continue;}
            if(opcode == 63) {end_program(program_memory);         break;}
            cerr<< "op code " << opcode << " non valido\n";
        }while(pc+registers[1] >= 0 && pc+registers[1] < N / 32 && iteration <= MAX_ITERATION);
        if(pc+registers[1] < 0 || pc + registers[1] >= N / 32){
            cerr<< "messed up pc = " << pc+registers[1] << endl;
        }
        if(iteration <= MAX_ITERATION)
            cerr<< endl << "computazione completata" << endl;
        else    
            cerr<< "computazione interrotta perchè in loop infinito" << endl;

        int somma = 0;
        for(int i = 0; i < 32; i++){
            somma += registers[i] + memory[mem_size-1-i];
        }
        if(somma != (mem_size*2-2) + registers[$grp]){
            cerr << "forza napoli "<< (mem_size*2-2) + registers[$grp] << endl;
        }
        reverseBitset(program_memory);
    }
};

/*TO DO 
implement sign extension 
based on the fun bits at
the end of the instruction.
To do that a revision of the 
space given to the immediate
needs to be reivisited

TO IMPLEMENT
in the comparison only the LSB is
considered. The program

if(2) cerr<< "evaluated true";
else cerr<< "evaluated false";

will result in:
evaluated false
 */ 
