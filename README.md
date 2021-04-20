# Mastery Code Challenge

## Introduction

The Code Challenge was started on 04/15/2021 to create an LTL (less-than-load) system that has immutable Trucks and 
Shipments. The solution adheres to the requirements defined [here](./mastery_data_coding_challenge.md) including the 
bonus optimization requirement.

## LTL Truck/Shipment System

My solution contains the following technologies, languages, frameworks, and paradigms:

* Docker
* Python
* PostgreSQL
* Flask
* openrouteservice

I used **Docker** because it was required of me; although it is the industry standard approach for container deployment.
I developed my solution using **Python and PostgreSQL**, since the data platform team (as I was told) primarily 
developed with them. As a career developer, I know how difficult it can be if a team doesn't work with the
same tech stack, so I chose to use technologies that I as well as the team would be comfortable reviewing. I chose 
**Flask** to fulfill my need of a lightweight RESTful API. The **openrouteservice** is a set of crowd-sourced geolocation 
APIs that provide advanced capabilities for (in particular) route optimization and addresses the VRP, or vehicle 
routing problem.

I focused purely on the design, development, deployment, and documentation on the project. QA was ignored, since no
mention to unit tests were required.

I also broke my application down into single responsibilities. I try to adhere to standard practices when I can.

To reiterate, here were the original requirements:

### Requirements
* Must expose some kind of API (REST/GraphQL or other) to create trucks and shipments
  * Must be able to create trucks and shipments
  * Trucks and shipments are immutable, will not change once created
  * Trucks and shipments must be created even if a match is not currently available, only deny creation if validation fails
* Trucks must be loaded with shipments without exceeding capacity
* Shipments must fit on one truck, **cannot** be divided among multiple trucks
* Must include report endpoint for:
  * All successful matches
  * Trucks without shipments
  * Shipments without a truck
* **Bonus** Optimize LTL shipments based on location (i.e., minimize the distance between shipments for each truck)

### Instructions

To start the services, run the following from the root folder:

> docker-compose up -d

This will install all dependencies, setup the database, and establish two exposed ports: 5432 and 5000. 5432 is for PostgreSQL. 5000 is the location of the 
RESTful API that contains all the following routes:

```
Endpoint                      Methods  Rule
----------------------------  -------  --------------------------
create_shipment               POST     /shipment
create_truck                  POST     /truck
create_truck_shipment         PUT      /truck/shipment
get_shipments                 GET      /shipments
get_shipments_without_trucks  GET      /shipments/no_trucks
get_trucks                    GET      /trucks
get_trucks_without_shipments  GET      /trucks/no_shipments
optimize_truck_shipments      GET      /trucks/shipments/optimize
```

#### POST /shipment

Create a new, immutable shipment.

```json
{
	"weight": 8000.0,
	"origin_latitude": 47.2530556,
	"origin_longitude": -122.4430556,
	"destination_latitude": 45.505044,
	"destination_longitude": -122.674991
}
```

Returns the ID of the new shipment.

#### POST /truck

Create a new, immutable truck.

```json
{
	"capacity": 48000.0,
	"origin_latitude": 41.878113,
	"origin_longitude": -87.629799,
	"destination_latitude": 30.2669444,
	"destination_longitude": -97.7427778
}
```

Returns the ID of the new truck.

#### PUT /truck/shipment
Attempt a manual add of a shipment to a truck.

```json
{
	"truck_id": "a0t8878knnniaqk",
	"shipment_id": "a0t8878knnnil5u"
}
```

#### GET /shipments
Get all shipments.

#### GET /shipments/no_trucks
Get all shipments with no trucks.

#### GET /trucks
Get all trucks.

#### GET /trucks/no_shipments
Get all trucks with no shipments.

#### GET /trucks/shipments/optimize
Clear out all current truck/shipments, and attempt to optimize the routes. Still must work with valid locations for
all vehicles to work.

You can apply a custom maximum time window (in seconds) for the average truck by adding a query parameter:

>...?max_time_window=14400

This will set the time window for the average truck to 4 hours (60s * 60m * 4h = 14400s).