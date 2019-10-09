const fs = require("fs");

function run(taskDef) {
    // create and start the task
    const task = taskDef();

    let result = task.next();

    // start the process
    step();

    function step() {
        if (result.done) {
            return;
        }

        if (typeof result.value === "function") {
            // yield return a node callback async function
            result.value((err, data) => {
                if (err) {
                    result = task.throw(err);
                    return;
                }
                result = task.next(data);
                step()
            });
        } else {
            // ... processing data, then start next turn
            result = task.next(result.value);
            step();
        }

    }
}

function readFile(filename) {
    return callback => fs.readFile(filename, callback);
}

run(function* () {
    const content = yield readFile("jsconfig.json");
    console.log(content.toString("utf8"));
})