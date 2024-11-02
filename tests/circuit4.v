//Defining a module named circuit_4 with inputs a, b, c, and output o
module circuit_4(a, b, c, o);
    input a;
    input b;
    input c;
        
    output o;

    //Internal wires to connect gates
    wire w; //Intermediate wire for AND gate output
    wire y; //Intermediate wire for OR gate output
    wire n; //Intermediate wire for NOR gate output
    wire z; //Intermediate wire for NAND gate output

    //Instantiate gates with specified delays
    and  #(4) g0 (w, a, b); //AND gate with delay of 4, output connected to w, inputs a and b
    or   #(6) g1 (y, w, c); //OR gate with delay of 6, output connected to y, inputs w and c
    nor  #(5) g2 (n, a, y); //NOR gate with delay of 5, output connected to n, inputs a and y
    nand #(3) g3 (z, b, n); //NAND gate with delay of 3, output connected to z, inputs b and n
    xor  #(7) g4 (o, z, c); //XOR gate with delay of 7, output connected to o, inputs z and c

endmodule;
