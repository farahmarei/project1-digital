
module circuit3(input a,input b, input c, output f);
    assign f = (a&~b) ^ (~c | a);
endmodule

