# Django-App

This application is built using Django and sqlite database , it allows the user to add polls , view the recently posted polls and view all polls inside the app .

## Set Up

I used docker in order to run the application , but you can use virtualenv to run it as well , but make sure that you install the packages inside the requirments.txt in order to run it , clone the repository using the following command:

git clone https://github.com/DaliaAsh/Django-App.git

You can use the docker-compose to run the app

docker-compose up

## Django-Poll App

After runing the server using the docker-compose command , You can navigate to localhost:8000 and you shall see the following page:
<img src = "https://user-images.githubusercontent.com/46220562/111909610-aa191580-8a66-11eb-8489-dd54f0678615.PNG">

After adding some polls:
<img src = "https://user-images.githubusercontent.com/46220562/111909622-b7ce9b00-8a66-11eb-9b47-b294bd792c21.PNG">

You can naviagte to the poll and vote to your answer:
<img src = "https://user-images.githubusercontent.com/46220562/111909631-c1f09980-8a66-11eb-95f3-b719a5d2134d.PNG">
