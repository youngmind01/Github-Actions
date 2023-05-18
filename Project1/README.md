
# A step by step guiude on how to install and configure Self Hosted Runner

 Firewall setup // make sure you have port 80,443 open for inbound, and same thing for outbound on your runner before proceeding with the below.

 - From your Main repo, navigate to settings
 - Click on Actions tab from the left side menu
 - Select runner
 - Choose the OS and architecture you will be using as runner // e.g Linux, 64bit arc.

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

$ ./config.sh --url https://github.com/youngmind01/Github-Actions --token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
// make sure nobdoy else sees your token.

# Last step

run it!
$ ./run.sh

# Use this YAML in your workflow file for each job
runs-on: self-hosted

![Screenshot from 2023-05-18 01-19-51](https://github.com/youngmind01/Github-Actions/assets/54754559/a41c677c-3415-48f6-97f7-26fb540c8ceb)




