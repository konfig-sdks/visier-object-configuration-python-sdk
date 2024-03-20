<div align="center">

[![Visit Visier](./header.png)](https://visier.com)

# Visier<a id="visier"></a>

Visier APIs for managing objects in studio experience


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`visierobjectconfiguration.object_configuration.get_calculation_concept`](#visierobjectconfigurationobject_configurationget_calculation_concept)
  * [`visierobjectconfiguration.object_configuration.get_calculation_concepts`](#visierobjectconfigurationobject_configurationget_calculation_concepts)
  * [`visierobjectconfiguration.object_configuration.get_selection_concept`](#visierobjectconfigurationobject_configurationget_selection_concept)
  * [`visierobjectconfiguration.object_configuration.get_selection_concepts`](#visierobjectconfigurationobject_configurationget_selection_concepts)
  * [`visierobjectconfiguration.object_configuration.map_calculation_concept`](#visierobjectconfigurationobject_configurationmap_calculation_concept)
  * [`visierobjectconfiguration.object_configuration.map_selection_concept`](#visierobjectconfigurationobject_configurationmap_selection_concept)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Visier&serviceName=ObjectConfiguration&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from visier_object_configuration_python_sdk import VisierObjectConfiguration, ApiException

visierobjectconfiguration = VisierObjectConfiguration(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Retrieve the configuration of a calculation concept
    get_calculation_concept_response = visierobjectconfiguration.object_configuration.get_calculation_concept(
        concept_id="conceptId_example",
    )
    print(get_calculation_concept_response)
except ApiException as e:
    print("Exception when calling ObjectConfigurationApi.get_calculation_concept: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from visier_object_configuration_python_sdk import VisierObjectConfiguration, ApiException

visierobjectconfiguration = VisierObjectConfiguration(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

async def main():
    try:
        # Retrieve the configuration of a calculation concept
        get_calculation_concept_response = await visierobjectconfiguration.object_configuration.aget_calculation_concept(
            concept_id="conceptId_example",
        )
        print(get_calculation_concept_response)
    except ApiException as e:
        print("Exception when calling ObjectConfigurationApi.get_calculation_concept: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from visier_object_configuration_python_sdk import VisierObjectConfiguration, ApiException

visierobjectconfiguration = VisierObjectConfiguration(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Retrieve the configuration of a calculation concept
    get_calculation_concept_response = visierobjectconfiguration.object_configuration.raw.get_calculation_concept(
        concept_id="conceptId_example",
    )
    pprint(get_calculation_concept_response.body)
    pprint(get_calculation_concept_response.body["uuid"])
    pprint(get_calculation_concept_response.body["name"])
    pprint(get_calculation_concept_response.body["configuration"])
    pprint(get_calculation_concept_response.headers)
    pprint(get_calculation_concept_response.status)
    pprint(get_calculation_concept_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ObjectConfigurationApi.get_calculation_concept: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `visierobjectconfiguration.object_configuration.get_calculation_concept`<a id="visierobjectconfigurationobject_configurationget_calculation_concept"></a>

This API allows you to retrieve the configuration details of a calculation concept in production.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_calculation_concept_response = visierobjectconfiguration.object_configuration.get_calculation_concept(
    concept_id="conceptId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### concept_id: `str`<a id="concept_id-str"></a>

The ID of the concept to retrieve the configuration for.

#### 🔄 Return<a id="🔄-return"></a>

[`CalculationConceptDTO`](./visier_object_configuration_python_sdk/pydantic/calculation_concept_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/calculation-concepts/{conceptId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierobjectconfiguration.object_configuration.get_calculation_concepts`<a id="visierobjectconfigurationobject_configurationget_calculation_concepts"></a>

This API allows you to retrieve the calculation concepts available in production.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_calculation_concepts_response = visierobjectconfiguration.object_configuration.get_calculation_concepts()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CalculationConceptListDTO`](./visier_object_configuration_python_sdk/pydantic/calculation_concept_list_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/calculation-concepts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierobjectconfiguration.object_configuration.get_selection_concept`<a id="visierobjectconfigurationobject_configurationget_selection_concept"></a>

This API allows you to retrieve the configuration details of a selection concept in production.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_selection_concept_response = visierobjectconfiguration.object_configuration.get_selection_concept(
    concept_id="conceptId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### concept_id: `str`<a id="concept_id-str"></a>

The ID of the concept to retrieve the configuration for.

#### 🔄 Return<a id="🔄-return"></a>

[`SelectionConceptDTO`](./visier_object_configuration_python_sdk/pydantic/selection_concept_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/selection-concepts/{conceptId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierobjectconfiguration.object_configuration.get_selection_concepts`<a id="visierobjectconfigurationobject_configurationget_selection_concepts"></a>

This API allows you to retrieve the selection concepts available in production.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_selection_concepts_response = visierobjectconfiguration.object_configuration.get_selection_concepts()
```

#### 🔄 Return<a id="🔄-return"></a>

[`SelectionConceptListDTO`](./visier_object_configuration_python_sdk/pydantic/selection_concept_list_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/selection-concepts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierobjectconfiguration.object_configuration.map_calculation_concept`<a id="visierobjectconfigurationobject_configurationmap_calculation_concept"></a>

This API allows you to map dimension members to nodes in a calculation concept.
 The changes are applied in a new project and published to production.

 The body of this API is the source of truth for dimension members mapped to the concept. For example, if a node in
 the body does not have any dimension members, all existing dimension members mapped to that node will be removed.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
map_calculation_concept_response = visierobjectconfiguration.object_configuration.map_calculation_concept(
    concept_id="conceptId_example",
    perspectives_to_map=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### concept_id: `str`<a id="concept_id-str"></a>

The UUID of the concept to configure.

##### perspectives_to_map: List[`PerspectiveConfigurationDTO`]<a id="perspectives_to_map-listperspectiveconfigurationdto"></a>

A list of objects representing the list of perspectives in the calculation concept.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CalculationConceptConfigurationMapDTO`](./visier_object_configuration_python_sdk/type/calculation_concept_configuration_map_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConceptConfigurationResultDTO`](./visier_object_configuration_python_sdk/pydantic/concept_configuration_result_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/calculation-concepts/{conceptId}/configure` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierobjectconfiguration.object_configuration.map_selection_concept`<a id="visierobjectconfigurationobject_configurationmap_selection_concept"></a>

This API allows you to map dimension members to a selection concept.
 The changes are applied to a new project and published to production.

 The body of this API is the source of truth for dimension members mapped to the concept. For example, if a node in
 the body does not have any dimension members, all existing dimension members mapped to that node will be removed.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
map_selection_concept_response = visierobjectconfiguration.object_configuration.map_selection_concept(
    concept_id="conceptId_example",
    analytic_object_filters_to_map=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### concept_id: `str`<a id="concept_id-str"></a>

The UUID of the concept to configure.

##### analytic_object_filters_to_map: List[`AnalyticObjectFilterDTO`]<a id="analytic_object_filters_to_map-listanalyticobjectfilterdto"></a>

A list of analytic object filters indicating the analytic object and dimension members used  for the selection concept.   Note: If this array is empty, all filters will be removed for the concept.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SelectionConceptConfigurationMapDTO`](./visier_object_configuration_python_sdk/type/selection_concept_configuration_map_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConceptConfigurationResultDTO`](./visier_object_configuration_python_sdk/pydantic/concept_configuration_result_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/admin/selection-concepts/{conceptId}/configure` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
