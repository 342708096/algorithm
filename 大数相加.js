function add(bigNumber1, bigNumber2) {
	bigNumber1 = Array.from(bigNumber1).reverse();
	bigNumber2 = Array.from(bigNumber2).reverse();
	const ret = []
	let t = 0;
	for (let i=0; i< Math.max(bigNumber1.length,bigNumber2.length);i++){
			let number1 = (bigNumber1[i] * 1) || 0
			let number2 = (bigNumber2[i] * 1) || 0
			ret.unshift((number1 + number2 + t) % 10)
			t = (number1 + number2 + t)/ 10 | 0
	}
	if (t) {
	  ret.unshift(t);
	}
	return ret.join('')
}

add('999999','88888') // 1088887