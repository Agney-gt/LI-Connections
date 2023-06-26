# LI-Connections
Automate Linkedin Cnnections

Flask API Endpoint that reads data from google sheets, logs into linkedin and sends personalized connection requests and updates the connection status on the sheet.

Create a new github project and follow the below steps to set up the virtual machine.

Cloud Virtual Machine Set Up - https://github.com/garywu/google-compute-engine-selenium
a) Set up GCP/AWS Machine

b) Go to the above github and follow the instructions there.

c) Run the shell script to set up the required infrastructure.

d) Note the chromedriver version. This is discussed in detail in the video.


https://github.com/Agney-gt/LI-Connections/assets/84612798/2e5071c7-ed6c-4386-93ad-324cb23fc098


Google Sheets Set Up - https://www.youtube.com/watch?v=TiOCo43rJHM&t=1s
Follow the steps in the above video and copy paste the excel containing sales navigator search into a google sheet.

Share the sheet with your service account as mentioned in Video 1

Add the service accounts secret-key.json into the folder in which the script is present on the VM

Linkedin Automation Set Up - Please have a look at the video to understand how the Selenium script uses the google sheets to login, send requests and update the sheet.
Ensure the cookies are named correctly and present folder in which the script is present on the VM









https://github.com/Agney-gt/LI-Connections/assets/84612798/f4136c6e-df2c-48b4-8975-d69a2c4fb3b1



https://github.com/Agney-gt/LI-Connections/assets/84612798/8d699e5f-46e6-45bc-977f-62da1e2e6fc1



https://github.com/Agney-gt/LI-Connections/assets/84612798/e1383a79-73d2-47f8-a1ce-bd6402303962


