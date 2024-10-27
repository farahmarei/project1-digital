module circuit_4(a, b, c, o);
    input a;
    input b;
    input c;
        
    output o;
        
    wire w;
    wire y;
    wire n;
    wire z;
        
    and  #(4) g0 (w, a, b);
    or   #(6) g1 (y, w, c);
    nor  #(5) g2 (n, a, y);
    nand #(3) g3 (z, b, n);
    xor  #(7) g4 (o, z, c);

endmodule;
