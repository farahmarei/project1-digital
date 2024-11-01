module circuit_1(a, b, o);
    input a;
    input b; 
    output o;
    wire x;
    wire no;
        
    and #(4) g0 (x, a, b);
    not #(4) g1 (no,b);
    or #(4) g2 (o,x,no);

