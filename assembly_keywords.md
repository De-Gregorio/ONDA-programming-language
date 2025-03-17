# Assembly Language Keywords

### Arithmetic and Logic Instructions
- `add` - Add two registers: `add $src1, $src2`,  
- `sub` - Subtract two registers: `sub $src1, $src2`
- `mul` - Multiply two registers: `mul $dest, $src1, $src2`
- `div` - Divide two registers: `div $dest, $src1, $src2`
- `xor` - Bitwise XOR: `xor $dest, $src1, $src2`
- `and` - Bitwise AND: `and $dest, $src1, $src2`
- `addi` - Add immediate value: `addi $src, immediate`
- `subi` - Subtract immediate value: `subi $src, immediate`
- `xorsi` - XOR with sign extended immediate value: `xorsi $dest, immediate`
- `flia` - Flip all qubits: `flia $dest` 
- `neg` - Negate register value: `neg $dest`
- `nop` - No operation: `nop`


### Control Flow Instructions
- `caddi` - Conditional add immediate: `caddi $cond, $src, immediate`
- `tcs` - Two case swap: `tcs $tur1, $tur2, $activation, $counter`
- `rebi` - Read qubit at index: `rebi $dest, $src1, $src2`
- `feq` - Flip on equal comparison: `feq $dest, $src1, $src2`
- `flt` - Flip on less than comparison: `flt $dest, $src1, $src2`
- `fne` - Flip on not equal comparison: `fne $dest, $src1, $src2`
- `flif` - Flip the first qubit: `flif $dest`

### Memory Instructions
- `sw` - Swap word to memory: `sw $src, offset($base)`
- `swre` - Swap registers: `swre $src1, $src2`
- `ta` - Throw away into garbage: `ta $dest`

### Quantum Instructions
- `z` - Z operation: `z $dest, $src`
- `had` - Hadamard operation: `had $dest, $src`

### Special Instructions 
- `eop` - End of program: `eop`
- `outr` - Output register value: `outr $src`
