//Defining a module named circuit_5 with inputs a, b, c, and output o
module circuit_5(a, b, c, o);
    input a;
    input b;
    input c;
        
    output o;

    //Internal wires to connect gates
    wire w; //Intermediate wire for OR gate output
    wire y; //Intermediate wire for NAND gate output
    wire n; //Intermediate wire for XOR gate output
    wire z; //Intermediate wire for AND gate output

    //Instantiate gates with specific delays
    or   #(6) g0 (w, a, b); //OR gate with delay of 6, output connected to w, inputs a and b
    nand #(3) g1 (y, w, c); //NAND gate with delay of 3, output connected to y, inputs w and c
    xor  #(5) g2 (n, a, y); //XOR gate with delay of 5, output connected to n, inputs a and y
    and  #(4) g3 (z, b, n); //AND gate with delay of 4, output connected to z, inputs b and n
    nor  #(7) g4 (o, z, c); //NOR gate with delay of 7, output connected to o, inputs z and c

endmodule;
