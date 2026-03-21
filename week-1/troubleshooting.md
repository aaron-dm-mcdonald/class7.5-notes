# VM Troubleshooting


```bash
# this metadata key is helpful! 
gcloud compute instances create <VM NAME> \
  --tags=http-server \
  --metadata=startup-script-url=<RAW LINK>
  ```

## Examine VM 

### CLI

  ```bash
  gcloud compute instances list

  gcloud compute instances describe <VM NAME> \
  --zone=<ZONE USED> \
  --format="yaml(name,status,zone,tags,metadata,networkInterfaces)"
  ```

### Console

- Check VM lifecycle state
    - is it running? staging? 
    - how long has it been initalized? 
    - can it be bootstraping still? 
    - wait a few minutes 

- Verify network tag (http-server)
- Go to VM details and verify startup script under metadata keys
- If you see web server default index.html page then wait a minute

## Where is the failure point

```bash
ping <EXTERNAL_IP> # verify network connectivity 
curl -v http://<EXTERNAL_IP> # verify its not your web browser and get verbose error
```

- time out (28): connection never gets to VM: fw issue
- failed to connect/connection refused (7): port 80 is reachable but nothing is listening on it (nginx didnt start or startup script failed)
- empty reply: server is running but webpage didnt get created or possible still bootstrapping. try again after one minute. 

## SSH troubleshooting
```bash
# Did the startup script run and did it error?
sudo journalctl -u google-startup-scripts

# Is nginx running?
sudo systemctl status nginx

# Did the html file get created?
cat /var/www/html/index.html
```