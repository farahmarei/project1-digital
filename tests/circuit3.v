//Defining a module named circuit_3 with inputs a, b, c, and output o
module circuit_3(a, b, c, o);
    input a;
    input b;
    input c;
        
    output o;

    //Internal wires to connect gates
    wire w; //Intermediate wire for NAND gate output 
    wire y; //Intermediate wire for XOR gate output 
    wire n; //Intermediate wire for NOT gate output 
    wire z; //Intermediate wire for OR gate output 

    //Instantiate gates with specified delays
    nand #(5) g0 (w, a, b); //NAND gate with delay of 5, output connected to w, inputs a and b
    xor  #(3) g1 (y, w, c); //XOR gate with delay of 3, output connected to y, inputs w and c
    not  #(2) g2 (n, a); //NOT gate with delay of 2, output connected to n, input a
    or   #(7) g3 (z, n, y); //OR gate with delay of 7, output connected to z, inputs n and y
    nor  #(4) g4 (o, z, c); //NOR gate with delay of 4, output connected to o, inputs z and c

endmodule;
