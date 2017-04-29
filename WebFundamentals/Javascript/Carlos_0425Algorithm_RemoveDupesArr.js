var arrHi = ["hello", "hello", "hello", "hi", "hi", 1, 1, 1, 1, 2, 2]

function removeDupe(arr){
  var obj = {}
  for(var i = 0; i<arr.length; i++){
    if(obj[arr[i]]){
      obj[arr[i]]++;
      for(var j = i; j < arr.length-1; j++){
        arr[j] = arr[j + 1]
      }
      arr.pop();
      i--
    }
    else{
      obj[arr[i]] = 1;
    }
  }
  console.log(arr)
  return arr
}
removeDupe(arrHi);
console.log(arrHi)