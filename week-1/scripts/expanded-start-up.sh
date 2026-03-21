#!/bin/bash

# install the webserver, it will start automatically 
apt install -y nginx

# Grab the Metadata for the webpage 
VM_NAME=$(curl -s -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/name)
INTERNAL_IP=$(curl -s -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/0/ip)
PROJECT_ID=$(curl -s -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/project/project-id)


# make the webpage and put it where nginx looks for html files
cat <<EOF > /var/www/html/index.html
<html>
<body>
  <h1>VM Metadata:</h1>
  <p><b>Project</b>: $PROJECT_ID</p>
  <p><b>VM Name</b>: $VM_NAME</p>
  <p><b>Internal IP</b>: $INTERNAL_IP</p>
</body>
</html>
EOF