#include <stdio.h>

void print_array(int arr[], int size) {  // 增加 size 参数
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main(void) {
    int ss[] = {8, 5, 3, 1};
    int size = sizeof(ss) / sizeof(ss[0]);  // 在 main 里计算数组长度

    printf("Hello World\n");
    print_array(ss, size);  // 传递数组和长度

    return 0;
}