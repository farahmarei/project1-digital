module circuit_5(a, b, c, o);
    input a;
    input b;
    input c;
        
    output o;
        
    wire w;
    wire y;
    wire n;
    wire z;
        
    or   #(6) g0 (w, a, b);
    nand #(3) g1 (y, w, c);
    xor  #(5) g2 (n, a, y);
    and  #(4) g3 (z, b, n);
    nor  #(7) g4 (o, z, c);

endmodule;
