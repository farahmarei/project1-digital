module circuit_3(a, b, c, o);
    input a;
    input b;
    input c;
        
    output o;
        
    wire w;
    wire y;
    wire n;
    wire z;
        
    nand #(5) g0 (w, a, b);
    xor  #(3) g1 (y, w, c);
    not  #(2) g2 (n, a);
    or   #(7) g3 (z, n, y);
    nor  #(4) g4 (o, z, c);

endmodule;
