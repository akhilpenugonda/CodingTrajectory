
// JavaScript program to count all duplicates
// from string using maps
function printDups(str)
{
	let count = new Map();
	for (let i = 0; i < str.length; i++) {
		if(count.has(str[i])){
			count.set(str[i],count.get(str[i])+1);
		}
		else{
			count.set(str[i],1);
		}
		//increase the count of characters by 1 
	}

	for (let [it,it2] of count) { //iterating through the unordered map 
		if (it2 > 1) //if the count of characters is greater than 1 then duplicate found
			document.write(it,", count = ",it2,"</br>");
	}
}
/* Driver code*/

let str = "test string";
printDups(str);

