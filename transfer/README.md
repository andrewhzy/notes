
1. go to master node, update the file: capacity-scheduler.xml.
   
3. update the file as the 2nd attached, and run below command: yarn rmadmin -refreshQueues
4. submit job to validate, there are a lot of pitfalls
  2. gcloud dataproc jobs submit will fail, it will use root as submit user, then it got error.(this I need to figure out why and how to overcome)
  3. ssh log into the master node, and submit spark job using spark’s raw command, it worked, see screenshots.
  4. if I sudo to be root and re submit job again(now submit user is root again), it will get error as by gcloud dataproc jobs submit.
  5. queue management can only through config file update and refresh (using yarn rmadmin -refreshQueues) or restart RM.
  6. with “using yarn rmadmin -refreshQueues“, change to existing queues will result in refresh failure. e.g. delete a queue, change a leaf queue to a parent queue. etc. such update can only done through restarting the resource manager daemon, an this will disrupt the service or even running jobs.
![image](https://github.com/user-attachments/assets/837a59eb-e45e-4b93-95a3-ea3c50b51016)
![image](https://github.com/user-attachments/assets/b882c7ef-e805-4c3b-84cf-f334342f82f5)
![image](https://github.com/user-attachments/assets/01966f74-9b45-4190-948a-51402c5a6354)
![image](https://github.com/user-attachments/assets/1725064a-492e-42be-ada0-9a3d308ac71d)

