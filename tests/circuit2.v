module circuit2(input a,input b, input c, output f);
    assign f = ~(a&b) ^ ((b&c) | a);
endmodule

