async function delayedPrint(delay, text){
  return new Promise(resolve=>{
      setTimeout(()=>{
        console.log(text);
        resolve();
      }, delay*1000);
  })
  
}

async function main(){
  await delayedPrint(2,"First");
  await delayedPrint(2, "Second");
}

main();