/*冒泡排序*/
function bubbleSort(arr, desc) {
    var i, len, j, temp;
    if (!arr || !arr.hasOwnProperty("length"))
        return;
    for (i = 0, len = arr.length; i < len; i++) {
        for (j = i + 1; j < len; j++) {
            if (desc ? arr[i] < arr[j] : arr[i] > arr[j]) {
                swap(arr, i, j);
            }
        }
    }
}

/*快速排序*/
function quickSort(arr, low, high, desc) {
    var index;
    if (!arr || !arr.hasOwnProperty("length") || low >= high)
        return;
    index = onceSort(arr, low, high, desc);
    quickSort(arr, low, index - 1, desc);
    quickSort(arr, index + 1, high, desc);
}

/*一次快排*/
function onceSort(arr, low, high, desc) {
    var key = arr[low];
    while (low < high) {
        while ((desc ? arr[high] <= key : arr[high] >= key) && high > low) {
            high--;
        }
        arr[low] = arr[high];
        while ((desc ? arr[low] >= key : arr[low] <= key) && high > low) {
            low++;
        }
        arr[high] = arr[low];
    }
    arr[low] = key;
    return low;
}

function swap(arr, i, j) {
    var temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}