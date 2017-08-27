/* C-x86: Simple arithmetic using inline assembly */
#include <stdio.h>

main(){
	int arg1,arg2;
	int add,sub,mul,quo,rem ;
    printf("Enter Two Integers: ");
    scanf("%d%d",&arg1,&arg2);

    /* Addition */
    __asm__ ("addl %%ebx,%%eax;"
			:"=a"(add)
			:"a"(arg1),"b"(arg2)
			);
	/* Subtraction */
    __asm__ ("subl %%ebx,%%eax;"
			:"=a"(sub)
			:"a"(arg1),"b"(arg2)
			);
	/* Multiplication */
    __asm__ ("imull %%ebx,%%eax;"
			:"=a"(mul)
			:"a"(arg1),"b"(arg2)
			);
	/* Division */
	__asm__ ("movl $0,%%edx;"
             "movl %2,%%eax;"
             "movl %3,%%ebx;"
             "idivl %%ebx;"
			:"=&a"(quo),"=&d"(rem)
			:"g"(arg1),"g"(arg2)
			);
    printf("%d + %d = %d\n",arg1,arg2,add);
    printf("%d - %d = %d\n",arg1,arg2,sub);
    printf("%d * %d = %d\n",arg1,arg2,mul);
    printf("%d / %d = %d\n",arg1,arg2,quo);
    printf("%d %% %d = %d\n",arg1,arg2,rem);
}
