const fs = require("fs");

function run(taskDef) {
    // create and start task
    const task = taskDef();
    let result = task.next();

    step();

    function step() {
        if (result.done) {
            return;
        }

        const promise = Promise.resolve(result.value);
        promise.then(value => {
            result = task.next(value);
            step();
        }).catch(error => {
            result = task.throw(error);
            step();
        })
    }
}

function readFile(filename) {
    return new Promise((resolve, reject) => {
        fs.readFile(filename, (err, data) => {
            if (err) reject(err);
            else resolve(data);
        })
    })
}

run(function* () {
    const content = yield readFile("jsconfig.json");
    console.log(content.toString());
})