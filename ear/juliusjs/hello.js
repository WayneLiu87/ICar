// bootstrap JuliusJS
var julius = new Julius();

julius.onrecognition = function(sentence) {
    console.log(sentence);
};

// say "Hello, world!"
// console logs: `> HELLO WORLD`
