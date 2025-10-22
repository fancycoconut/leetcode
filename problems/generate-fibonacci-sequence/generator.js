/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let output = [];

    if (output.length === 0) {
        output.push(0);
        yield output[output.length - 1];
    }
    if (output.length === 1) {
        output.push(1);
        yield output[output.length - 1];
    }

    while (true) {
        var next = output[output.length - 2] + output[output.length - 1];
        output.push(next);
        yield next;
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */