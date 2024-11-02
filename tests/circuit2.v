//Defining a module named circuit_2 with inputs a, b, c, and output o
module circuit_2(a, b, c, o);
    input a;
    input b;
    input c;
        
    output o;

    //Internal wires to connect gates
    wire w; //Intermediate wire for NOR gate output
    wire y; //Intermediate wire for AND gate output
    wire n; //Intermediate wire for XOR gate output
    wire z; //Intermediate wire for OR gate output

    //Instantiate gates with specific delays 
    nor #(3) g0 (w, a, b); //NOR gate with delay of 3, output connected to w, inputs a and b
    and #(6) g1 (y, w, z); //AND gate with delay of 6, output connected to y, inputs w and z
    xor #(4) g2 (n, a, y); //XOR gate with delay of 4, output connected to n, inputs a and y
    or  #(8) g3 (z, b, c); //OR gate with delay of 8, output connected to z, inputs b and c
    and #(2) g4 (o, n, z); //AND gate with delay of 2, output connected to o, inputs n and z

endmodule;
