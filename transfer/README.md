
1. gcloud dataproc jobs submit will fail, it will use root as submit user, then it got error.(this I need to figure out why and how to overcome)
2. ssh log into the master node, and submit spark job using spark’s raw command, it worked, see screenshots.
3. if I sudo to be root and re submit job again(now submit user is root again), it will get error as by gcloud dataproc jobs submit.
4. queue management can only through config file update and refresh (using yarn rmadmin -refreshQueues) or restart RM.
5. with “using yarn rmadmin -refreshQueues“, change to existing queues will result in refresh failure. e.g. delete a queue, change a leaf queue to a parent queue. etc. such update can only done through restarting the resource manager daemon, an this will disrupt the service or even running jobs.


![image](https://github.com/user-attachments/assets/4f06e2e3-b556-4213-8c1b-e665b6843c54)
![image](https://github.com/user-attachments/assets/b882c7ef-e805-4c3b-84cf-f334342f82f5)
![image](https://github.com/user-attachments/assets/01966f74-9b45-4190-948a-51402c5a6354)
![image](https://github.com/user-attachments/assets/1725064a-492e-42be-ada0-9a3d308ac71d)

