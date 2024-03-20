import typing_extensions

from visier_object_configuration_python_sdk.apis.tags import TagValues
from visier_object_configuration_python_sdk.apis.tags.object_configuration_api import ObjectConfigurationApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.OBJECT_CONFIGURATION: ObjectConfigurationApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.OBJECT_CONFIGURATION: ObjectConfigurationApi,
    }
)
