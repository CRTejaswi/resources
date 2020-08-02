/* C-x86: Multiplication by 5 */
/* Uses GAS instead of Intel x86 syntax */
#include <stdio.h>
/* Input-Output Registers are different, but unknown*/
void f1(int x){
    int y=0;
     asm ("leal(%1,%1,4),%0"
         :"=r"(y)           // Output
         :"r"(x)            // Input
         );
}
/* Input-Output Registers are same, but unknown */
void f2(int x){
    int y=0;
     asm ("leal(%0,%0,4),%0"
         :"=r"(y)           // Output
         :"0"(x)            // Input
         );
}
/* Input-Output Registers are same, and known */
void f3(int x){
     asm ("leal(%%ecx,%%ecx,4),%%ecx"
         :"=c"(x)           // Output
         :"c"(x)            // Input
         );
}
main(){
    int x;
    scanf("%d",&x);
    f1(x);
    f2(x);
    f3(x);
}
