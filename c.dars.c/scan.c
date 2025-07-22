#include <stdio.h>
int main() {

 int b;
 char a[50];
 printf("salom ismingizni kiriting!!!\n");
 scanf("%s",a);
 printf("davom etish -- 1\n tugatish -- 0\n");
 scanf("%d",&b);
do {
 switch (b) {
case 1:
 printf("Assalomu Alaykum STIVERNA 😊");
 break;
}
 }
while (b != 0);
return 0;
}
