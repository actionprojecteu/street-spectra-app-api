# swagger_client.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/jgcasta/StreetSpectra/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_new_user**](DefaultApi.md#add_new_user) | **POST** /addNewUserData | Create user data
[**edit_user_data**](DefaultApi.md#edit_user_data) | **POST** /editUserData | Edit user data
[**get_history_data_post**](DefaultApi.md#get_history_data_post) | **POST** /getHistoryData | Retrieve history data for a user
[**get_map_distribution_post**](DefaultApi.md#get_map_distribution_post) | **POST** /getMapDistribution | Retrieve map data distribution
[**get_spectrum_data_post**](DefaultApi.md#get_spectrum_data_post) | **POST** /getSpectrumData | Retrieve data from a single spectrum
[**get_user_data**](DefaultApi.md#get_user_data) | **POST** /getUserData | Retrieve user data
[**get_users_ranking_post**](DefaultApi.md#get_users_ranking_post) | **POST** /getUsersRanking | Retrieve ranking of users
[**login**](DefaultApi.md#login) | **POST** /login | User login
[**send_spectrum_data_post**](DefaultApi.md#send_spectrum_data_post) | **POST** /sendSpectrumData | Send spectrum metadata
[**send_spectrum_img_post**](DefaultApi.md#send_spectrum_img_post) | **POST** /sendSpectrumImg | Send spectrum image file


# **add_new_user**
> add_new_user(user_data=user_data)

Create user data

Send user data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
user_data = swagger_client.UserData() # UserData |  (optional)

try:
    # Create user data
    api_instance.add_new_user(user_data=user_data)
except ApiException as e:
    print("Exception when calling DefaultApi->add_new_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_data** | [**UserData**](UserData.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_user_data**
> edit_user_data(user_data=user_data)

Edit user data

Edit user data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
user_data = swagger_client.UserData() # UserData |  (optional)

try:
    # Edit user data
    api_instance.edit_user_data(user_data=user_data)
except ApiException as e:
    print("Exception when calling DefaultApi->edit_user_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_data** | [**UserData**](UserData.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_history_data_post**
> get_history_data_post(login=login)

Retrieve history data for a user

Retrieve history data for a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
login = swagger_client.Login() # Login |  (optional)

try:
    # Retrieve history data for a user
    api_instance.get_history_data_post(login=login)
except ApiException as e:
    print("Exception when calling DefaultApi->get_history_data_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | [**Login**](Login.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_map_distribution_post**
> ResponseListSpectra get_map_distribution_post(get_map_distribution=get_map_distribution)

Retrieve map data distribution

Retrieve map data distribution

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
get_map_distribution = swagger_client.RequestMapDistribution() # RequestMapDistribution |  (optional)

try:
    # Retrieve map data distribution
    api_response = api_instance.get_map_distribution_post(get_map_distribution=get_map_distribution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_map_distribution_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_map_distribution** | [**RequestMapDistribution**](RequestMapDistribution.md)|  | [optional] 

### Return type

[**ResponseListSpectra**](ResponseListSpectra.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spectrum_data_post**
> SpectrumData get_spectrum_data_post(get_spectrum_data=get_spectrum_data)

Retrieve data from a single spectrum

Retrieve data from a single spectrum. Image stored as username + ts_gps UNIX time in seconds **jgcasta1579627948.jpg**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
get_spectrum_data = swagger_client.GetSpectrumData() # GetSpectrumData |  (optional)

try:
    # Retrieve data from a single spectrum
    api_response = api_instance.get_spectrum_data_post(get_spectrum_data=get_spectrum_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_spectrum_data_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_spectrum_data** | [**GetSpectrumData**](GetSpectrumData.md)|  | [optional] 

### Return type

[**SpectrumData**](SpectrumData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_data**
> get_user_data(user_data=user_data)

Retrieve user data

Retrieve user data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
user_data = swagger_client.UserData() # UserData |  (optional)

try:
    # Retrieve user data
    api_instance.get_user_data(user_data=user_data)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_data** | [**UserData**](UserData.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_ranking_post**
> get_users_ranking_post(login=login)

Retrieve ranking of users

Retrieve ranking of users

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
login = swagger_client.UserData() # UserData |  (optional)

try:
    # Retrieve ranking of users
    api_instance.get_users_ranking_post(login=login)
except ApiException as e:
    print("Exception when calling DefaultApi->get_users_ranking_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | [**UserData**](UserData.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> UserData login(login=login)

User login

User login

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
login = swagger_client.Login() # Login |  (optional)

try:
    # User login
    api_response = api_instance.login(login=login)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | [**Login**](Login.md)|  | [optional] 

### Return type

[**UserData**](UserData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_spectrum_data_post**
> send_spectrum_data_post(spectrum_data=spectrum_data)

Send spectrum metadata

Send spectrum metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
spectrum_data = swagger_client.SpectrumData() # SpectrumData |  (optional)

try:
    # Send spectrum metadata
    api_instance.send_spectrum_data_post(spectrum_data=spectrum_data)
except ApiException as e:
    print("Exception when calling DefaultApi->send_spectrum_data_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spectrum_data** | [**SpectrumData**](SpectrumData.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_spectrum_img_post**
> send_spectrum_img_post(spectrum_image=spectrum_image)

Send spectrum image file

Send spectrum image file

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
spectrum_image = '/path/to/file.txt' # file |  (optional)

try:
    # Send spectrum image file
    api_instance.send_spectrum_img_post(spectrum_image=spectrum_image)
except ApiException as e:
    print("Exception when calling DefaultApi->send_spectrum_img_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spectrum_image** | **file**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

