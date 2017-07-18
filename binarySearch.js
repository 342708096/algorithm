function binarySearch(arr, search, low, high ) {
	low = low || 0;
	high = high || arr.length - 1
	const mid = (low + high) >>> 1
	if (arr[mid] === search) {
		return mid;
	}
	if (mid < high && search > arr[mid]) {
		return binarySearch(arr,search, mid + 1, high);
	}
	if (low < mid && search < arr[mid]) {
		return binarySearch(arr, search, low, mid - 1, );
	}
	return null
}