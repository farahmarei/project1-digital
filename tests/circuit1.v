
module circuit1(input a,input b, input c, output f);
    assign f = (~a&c) & (b | a);
endmodule


