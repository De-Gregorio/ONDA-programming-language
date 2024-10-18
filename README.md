<h1>THE QUANTUM ONDA PROGRAMMING LANGUAGE</h1>
ONDA is a high-level programming language similar to C that can automatically manage garbage collection. This project implements an engine that simulates a potential quantum architecture along with its associated instruction set architecture (ISA). Each instruction used in the engine can be realized by a quantum circuit on a quantum computer.

<h1>INSTALLATION</h1>
Clone the repositary on your machine. Then some files must be compiled, to do so run the setup.py file the folder.

```
python setup.py
```
if every thing worked you should only get some warnings
```
during compilation of grammar:
warning(154): Gram.g4:13:0: rule functionImpl contains an optional block with at least one alternative that can match an empty string
warning(154): Gram.g4:13:0: rule functionImpl contains an optional block with at least one alternative that can match an empty string
```

<h2>Classical Features</h2>
ONDA supports all the common C operations, such as +, -, *, /, =, ~, and ^. Function calls and recursion function similarly. Currently, ONDA has only one data type: int. To declare an integer variable or array, you can use the same syntax as in C:

```C
int main()
{
    int a; // automatically initialized to 0
    int b = 52;
    int c[10]; // all 10 values are initialized to 0
    c[2] += b + a;
    return;
}
```
 
<h3>Conditianls and Loops</h3>
The if statement functions as usual, and the only available loop is the do-while loop.

```C
int a = 3;
if(a == 5){
    a -=2;
}else{
    a += 2;
}
int i;
do{
    a -= 1;
    i += 1;
}while(0 < a); // some operators, like >, are not available yet 
```

<h2>Quantum behaviors</h2>
Superposition is handled automatically, allowing the use of H gates, Z gates, and soon Y gates. When an operator that induces superposition is applied, the computation branches into two distinct paths, each potentially leading to different outcomes with its own complex coefficient. At the end of the computation, branches with identical states (i.e., all values are the same) are merged by summing their coefficients and eliminating duplicates. This process enables both constructive and destructive interference. 


<h3>Z gate</h3>
The Z gate, is applied by doing a # b. In this case a Z gate is applied to the first b qubits of the a value. The #= inplace operator is also supported.

```C
int a = 1;
a #= 1; //The coefficient of the computation has been multiplied by -1 because a Z gate has been applied to a qubit set to 1.
```

<h3>H gate</h3>
The H gate, is applied by doing a @ b. In this case a hadamard is applied to the first b qubits of the a value. The @= inplace operator is also supported. 

```C
int a = 0;
a @= 8; // a is now in a even superposition of the values from  0 to 255
```

<h1>USAGE</h1>
Write a file, possibly with .onda extension.

```C
int main()
{
    int a = 1;
    a @= 2;
    print a;
    return;
}
```

Then save it in the main folder and run: 

```
python main.py file.onda
```

You will gate as output the rankings of the most probable measure (the measure operation is implemented with "print a"):

```
comp n3:	(-0.5+0j)		3	0.25000	
comp n2:	(0.5+0j)		0	0.25000	
comp n1:	(-0.5+0j)		1	0.25000	
comp n0:	(0.5+0j)		2	0.25000	
```

<h1>COMMON BUGS</h1>
The project is still in a early stage and many features are not implemented yet. 
<h2>Blocks</h2>
Declaring a variable in a block, or more generally, expecting any C-like block behavior will result in an error.

```C
int a = 0;
if(a == 3){
    int b; // DO NOT DECLARE VARS IN BLOCKS
}
return;
```
This will lead to an error

<h2>Return</h2>
The insertion of the return is MANDATORY. 
The engine will not return if you do not tell him to do so. Omitting some trivial return may courrupt the computation.

```C
void f(a)
{
    print a + 2;
    // RETURN NOT SPECIFIED, A BUG WILL OCCUR
}

int main()
{
    int a = 8;
    f(a);
    // RETURN NOT SPECIFIED, A BUG WILL OCCUR
}
```
<h2>Infinite computations</h2>
The H gate is really powerful but it also have an exponantial overhead, so appling it multiple times might lead to an unfeasible number of "parallel" computations.
<h2>Edge cases</h2>
Any non-trivial edge case might lead to an error.
<h1>Code example</h1>
In this code example is shown how a grover search might be implemented. 

```C
int main()
{
    int arr_length = 4;
    int index = 0;
    int searched_number = 2;
    int iteration = 0;
    int one = 1;
    int arr[4];


    
    do{
        arr[iteration] = iteration*2;
        iteration += 1;
    }while(iteration < arr_length);


    iteration = 0;
    index @= 2;
    do{
        if(const arr[index] == searched_number){
            one #= 1;
        }


        index @= 2;
        if(const index == 0){
            one #= 1;
        }
        index @= 2;
        iteration += 1;
    }while(iteration < 1);

    print index;
    return;
}
```
The output of the execution is:

```
comp n2:	(-1+0j)		1	1.00000	
comp n3:	0j			2	0.00000	
comp n1:	0j			0	0.00000	
comp n0:	0j			3	0.00000	
```

<h1>Future Versions</h2>
<p>As afore mentioned, the Y gate will be implemented. Then an in-depth documentation of the language wil also be written.</p>

The ONDA programming language is intended as a prototype to demonstrate the tasks that quantum computers can handle and how poorly classical computers perform at these tasks. The compiler uses a stack machine model to translate the code into basic instructions. While this model is simple, it is slow and does not scale well. Although the code can be optimized in many ways, doing so is neither the best approach nor the main objective. In fact, the most effective optimization might be to start from scratch and explore other models for implementing such a programming language. This project does not aim to create the fastest quantum simulator. Instead, it seeks to inspire researchers to explore new models for quantum computation and showcase their potential. Despite the strict limitations of the field, it demonstrates that new abstractions are possible and crucial for achieving greater progress.