const fs = require("fs");

function run(taskDef) {
    // create and start task
    const task = taskDef();
    return Promise.resolve(task);
}

async function readFile(filename) {
    return new Promise((resolve, reject) => {
        fs.readFile(filename, (err, data) => {
            if (err) reject(err);
            else resolve(data);
        })
    })
}

run(async () => {
    const content = await readFile("jsconfig.json");
    console.log(content.toString());
})