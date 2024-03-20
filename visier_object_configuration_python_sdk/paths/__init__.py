# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from visier_object_configuration_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_ADMIN_CALCULATIONCONCEPTS = "/v1/admin/calculation-concepts"
    V1_ADMIN_CALCULATIONCONCEPTS_CONCEPT_ID = "/v1/admin/calculation-concepts/{conceptId}"
    V1_ADMIN_CALCULATIONCONCEPTS_CONCEPT_ID_CONFIGURE = "/v1/admin/calculation-concepts/{conceptId}/configure"
    V1_ADMIN_SELECTIONCONCEPTS = "/v1/admin/selection-concepts"
    V1_ADMIN_SELECTIONCONCEPTS_CONCEPT_ID = "/v1/admin/selection-concepts/{conceptId}"
    V1_ADMIN_SELECTIONCONCEPTS_CONCEPT_ID_CONFIGURE = "/v1/admin/selection-concepts/{conceptId}/configure"
