//寻找字符串里面出现的最长回文

//思路一: 暴力求解 时间复杂度为O(N^3)
function findLongestPalindrome1(str){
    const length = str.length;
    let maxLength = 0, start = 0;
    for (let i=0;i<length;i++){
        for (let j = i+1; j<length; j++){
            for (let ii = i, jj = j; ii <= jj; ii ++ , jj --){
                if (str.charAt(ii) !== str.charAt(jj)){
                    break;
                }
                if (jj - ii <= 1  && j - i + 1 > maxLength){
                    maxLength = j - i +1;
                    start = i;
                }
            }
        }
    }
    if (maxLength > 0){
        return str.substr(start, maxLength);
    }
    return null;
}

console.log(findLongestPalindrome1('1233211'));

//思路二: 中心扩展 时间复杂度为O(N^2)
function findLongestPalindrome2(str){
    const length = str.length;
    if (length === 1) return str;
    if (length === 0) return null;
    let maxLength = 0, start;
    for (let i = 0; i < length; i++){//长度为奇数
        let j = i - 1, k = i + 1;
        while(j >= 0 && k < length && str.charAt(j) === str.charAt(k)){
            if ( k - j +1 > maxLength){
                start = j;
                maxLength=k-j+1;
            }
            j -- ;
            k ++ ;
        }
    }

    for (let i=0; i<length; i++){//长度为偶数
        let j = i, k = i +1 ;
        while(j >= 0 && k < length && str.charAt(j) === str.charAt(k)){
            if ( k - j +1 > maxLength){
                start = j;
                maxLength=k-j+1;
            }
            j -- ;
            k ++ ;
        }
    }

    if (maxLength > 0){
        return str.substr(start, maxLength);
    }
    return null;
}

console.log(findLongestPalindrome2('12333211'));