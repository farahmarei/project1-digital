module circuit_1(a, b, c, o);
    input a;
    input b;
    input c;
        
    output o;
        
    wire w;
    wire y;
    wire n;
    wire z;
        
    nand #(4) g0 (w, a, b);
    xor  #(2) g1 (y, w, c);
    and  #(7) g2 (n, a, y);
    nor  #(6) g3 (z, b, n);
    or   #(3) g4 (o, z, c);

endmodule;
