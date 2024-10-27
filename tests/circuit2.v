module circuit_2(a, b, c, o);
    input a;
    input b;
    input c;
        
    output o;
        
    wire w;
    wire y;
    wire n;
    wire z;
        
    nor #(3) g0 (w, a, b);
    and #(6) g1 (y, w, z);
    xor #(4) g2 (n, a, y);
    or  #(8) g3 (z, b, c);
    and #(2) g4 (o, n, z);

endmodule;
