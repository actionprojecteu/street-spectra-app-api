# API description for StreetSpectra project

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
user_data = swagger_client.UserData() # UserData |  (optional)

try:
    # Create user data
    api_instance.add_new_user(user_data=user_data)
except ApiException as e:
    print("Exception when calling DefaultApi->add_new_user: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://virtserver.swaggerhub.com/jgcasta/StreetSpectra/1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**add_new_user**](docs/DefaultApi.md#add_new_user) | **POST** /addNewUserData | Create user data
*DefaultApi* | [**edit_user_data**](docs/DefaultApi.md#edit_user_data) | **POST** /editUserData | Edit user data
*DefaultApi* | [**get_history_data_post**](docs/DefaultApi.md#get_history_data_post) | **POST** /getHistoryData | Retrieve history data for a user
*DefaultApi* | [**get_map_distribution_post**](docs/DefaultApi.md#get_map_distribution_post) | **POST** /getMapDistribution | Retrieve map data distribution
*DefaultApi* | [**get_spectrum_data_post**](docs/DefaultApi.md#get_spectrum_data_post) | **POST** /getSpectrumData | Retrieve data from a single spectrum
*DefaultApi* | [**get_user_data**](docs/DefaultApi.md#get_user_data) | **POST** /getUserData | Retrieve user data
*DefaultApi* | [**get_users_ranking_post**](docs/DefaultApi.md#get_users_ranking_post) | **POST** /getUsersRanking | Retrieve ranking of users
*DefaultApi* | [**login**](docs/DefaultApi.md#login) | **POST** /login | User login
*DefaultApi* | [**send_spectrum_data_post**](docs/DefaultApi.md#send_spectrum_data_post) | **POST** /sendSpectrumData | Send spectrum metadata
*DefaultApi* | [**send_spectrum_img_post**](docs/DefaultApi.md#send_spectrum_img_post) | **POST** /sendSpectrumImg | Send spectrum image file


## Documentation For Models

 - [GetSpectrumData](docs/GetSpectrumData.md)
 - [Login](docs/Login.md)
 - [RequestMapDistribution](docs/RequestMapDistribution.md)
 - [Response](docs/Response.md)
 - [ResponseListSpectra](docs/ResponseListSpectra.md)
 - [SpectrumData](docs/SpectrumData.md)
 - [UserData](docs/UserData.md)
 - [UserRanking](docs/UserRanking.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

jgcasta@gmail.com

