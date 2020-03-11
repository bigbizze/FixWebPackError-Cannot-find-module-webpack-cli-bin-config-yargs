# FixWebPackError-Cannot-find-module-webpack-cli-bin-config-yargs
python script to fix: ```Error: Cannot find module 'webpack-cli/bin/config-yargs' when using webpack-dev-server &amp; webpack```

If you have the following error when using webpack-dev-server:
```
internal/modules/cjs/loader.js:638
    throw err;

Error: Cannot find module 'webpack-cli/bin/config-yargs'
    at Function.Module._resolveFilename (internal/modules/cjs/loader.js:636:15)
    at Function.Module._load (internal/modules/cjs/loader.js:562:25)
    at Module.require (internal/modules/cjs/loader.js:692:17)
    at require (internal/modules/cjs/helpers.js:25:18)
    at Object.<anonymous> (node_modules\webpack-dev-server\bin\webpack-dev-server.js:77:1)
    at Module._compile (internal/modules/cjs/loader.js:778:30)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:789:10)
    at Module.load (internal/modules/cjs/loader.js:653:32)
    at tryModuleLoad (internal/modules/cjs/loader.js:593:12)
    at Function.Module._load (internal/modules/cjs/loader.js:585:3)
error Command failed with exit code 1.
info Visit https://yarnpkg.com/en/docs/cli/run for documentation about this command.
```

And have python installed, you can prepend a call to this script to your package.json webpack-dev-server command like this:

```
 "scripts": {
    "start": "python utils_scripts/FixWebpackServerError.py && webpack-dev-server",
    ...
  }
```

& it will fix the issue for you.

NOTE: if you do not have python installed globally, change the word python above to the .exe of (shouldn't really matter which version) of a python3 interpreter.

I have the file inside a folder in the root of the project directory called 'utils_scripts'.
