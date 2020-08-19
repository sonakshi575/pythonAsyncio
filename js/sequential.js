async function sleep(delay) {
  return new Promise(resolve => {
    setTimeout(() => resolve(), delay * 1000);
  });
}

async function delayedPrint(delay, text) {
  let i = 0;
  while (i < 5) {
    await sleep(delay);
    console.log(text);
    i++;
  }

  return Promise.resolve();
}

async function main() {
  await delayedPrint(2, "First");
  await delayedPrint(2, "Second");
}

main();
