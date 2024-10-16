
module circuit4(input a,input b, input c, output f);
    assign f = ~(a | c) | (a |~b);
endmodule


