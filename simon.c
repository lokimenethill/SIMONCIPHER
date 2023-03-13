#include<stdio.h>
#define LCS _lrtotl //left circular shift
#define u64 unsigned long long
#define f(x) ((LCS(x,1) & LCS(x,8)) ^ LCS(x,2))
#define R2(x,y,k1,k2) (y^=f(x), y^=k1, x^=f(y), x^=k2)

void Simon(u64 pt[],u64 ct[], u64 k[]){
u64 i;

  ct[0]=pt[0];
  ct[1]=pt[1];
  for(i=0; i<68; i+=2){
    R2(ct[1],ct[0],k[i],k[i+1]);
  }
}

int main(){
  printf("hola mundo");
}
