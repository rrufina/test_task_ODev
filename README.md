# Test Task
## API endpoints:
1. ```GET: metrics/start_at=2020-01-01&end_at=2020-01-09``` - returns standart deviation and average value the exchange rate of all currencies for the specified time period
![GET Request](https://i.imgur.com/5R3KnbZ.png)  


2. ```GET: metrics/correlation/start_at=2020-03-23&end_at=2020-03-25&symbols=ILS,JPY``` - returns correlation between two currency pairs (CUR1-EUR, CUR2-EUR) for the specified time period
![GET Request](https://i.imgur.com/QuVd8xM.png)  

For ease of entering data: you can go to ```http://localhost:8000/metrics/```

## Get the source code
Go to the directory you want to see this project in. Now you can get all the source code of this project using git clone command.
```
> git clone https://github.com/rrufina/test_task_ODev
```

## Deployment using Docker
### Change environmental variables
Now you can see example.env with such content inside it:
```
SECRET_KEY=your_django_secret_key_here
```
Put your django secret key here. If you don't have one, you can get it [here](https://djecrety.ir).
### Copy to .env
Now you need to copy the content of example.env to .env file. Use this:
```
> cp example.env .env
```
### Compose up
Now you need build our application, to do this use the following command:
```
> docker-compose up --build -d
```

## Documentation
To view the documentation you need to run the appplication and go [here](http://localhost:8000/redoc/).