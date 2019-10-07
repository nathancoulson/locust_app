# locust-app
Locust.io HTTP traffic generator for MSc Data Science project repo (microservice auto-scaling system)

# Description
Application summary as part of the test microservice based web application (seen in 2019 N C Coulson paper: "Adaptive microservice scaling for elastic web applications")

To simulate the HTTP request workload we will use Locust.io, which is a high performance configurable load testing tool written in Python.
The Locust.io tool allowed us to simulate HTTP traffic to the web application. We were able to specify the number of concurrent users and how often requests would be made. This was kept constant in order to focus on the question of which microservice was being stressed more by changing request mixes.
The Locust.io framework allowed us to easily create functions which randomly picked from our biased request subsets. By changing the ratio in which the Locust script picked which HTTP request to make we were able to ”bias” the traffic for a specific period toward one or more microservices. See a sample below and the full table in Appendix B.

# Deployment
The Locust.io app was containerised for easy deployment.
