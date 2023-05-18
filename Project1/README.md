
# Download
**Create a folder**
$ mkdir actions-runner && cd actions-runner

# Download the latest runner package
$ curl -o actions-runner-linux-x64-2.304.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.304.0/actions-runner-linux-x64-2.304.0.tar.gz

# Optional: Validate the hash
$ echo "292e8770bdeafca135c2c06cd5426f9dda49a775568f45fcc25cc2b576afc12f  actions-runner-linux-x64-2.304.0.tar.gz" | shasum -a 256 -c

# Extract the installer
$ tar xzf ./actions-runner-linux-x64-2.304.0.tar.gz

# Configure
**Create the runner and start the configuration experience**
$ ./config.sh --url https://github.com/youngmind01/Github-Actions --token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx# Last step, 

run it!
$ ./run.sh

# Use this YAML in your workflow file for each job
runs-on: self-hosted