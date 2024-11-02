# Defining a module named circuit_1 with inputs a, b, c, and output o
module circuit_1(a, b, c, o);
    input a;
    input b;
    input c;
        
    output o;

    # Internal wires to connect gates
    wire w; # Intermediate wire for NAND gate output
    wire y; # Intermediate wire for XOR gate output
    wire n; # Intermediate wire for AND gate output
    wire z; # Intermediate wire for NOR gate output

    # Instantiate gates with specific delays
    nand #(4) g0 (w, a, b); # NAND gate with delay of 4, output connected to w, inputs a and b
    xor  #(2) g1 (y, w, c); # XOR gate with delay of 2, output connected to y, inputs w and c
    and  #(7) g2 (n, a, y); # AND gate with delay of 7, output connected to n, inputs a and y
    nor  #(6) g3 (z, b, n); # NOR gate with delay of 6, output connected to z, inputs b and n
    or   #(3) g4 (o, z, c); # OR gate with delay of 3, output connected to o, inputs z and c

endmodule;
