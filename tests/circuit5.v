module circuit5(input a,input b, input c, output f);
    assign f = (~(a&b)|c) | ((b&~c) | a);
endmodule
