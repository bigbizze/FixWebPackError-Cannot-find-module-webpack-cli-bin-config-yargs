import os
webpack_dev_server_path = "node_modules/webpack-dev-server/bin/webpack-dev-server.js"
if os.path.exists(webpack_dev_server_path):
    with open(webpack_dev_server_path, "r") as fp:
        data = fp.read()

    data = data.replace("require('webpack-cli/bin/config-yargs')(yargs);", "require('webpack-cli/bin/config/config-yargs')(yargs);")
    data = data.replace("const config = require('webpack-cli/bin/convert-argv')(yargs, argv, {", "const config = require('webpack-cli/bin/utils/convert-argv')(yargs, argv, {")

    with open(webpack_dev_server_path, "w") as fp:
        fp.write(data)
