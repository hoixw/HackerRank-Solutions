int* rotateLeft(int d, int arr_count, int* arr, int* result_count) {
    *result_count = arr_count;
    int *result = (int*)malloc(arr_count * sizeof(int));
    
    for (int i = 0; i < (arr_count - d); i++) {
        result[i] = arr[i+d];
    }
    
    for (int i = (arr_count - d); i < arr_count; i++) {
        result[i] = arr[i + d - arr_count];
    }
    
    return result;
}