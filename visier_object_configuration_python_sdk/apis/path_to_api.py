import typing_extensions

from visier_object_configuration_python_sdk.paths import PathValues
from visier_object_configuration_python_sdk.apis.paths.v1_admin_calculation_concepts import V1AdminCalculationConcepts
from visier_object_configuration_python_sdk.apis.paths.v1_admin_calculation_concepts_concept_id import V1AdminCalculationConceptsConceptId
from visier_object_configuration_python_sdk.apis.paths.v1_admin_calculation_concepts_concept_id_configure import V1AdminCalculationConceptsConceptIdConfigure
from visier_object_configuration_python_sdk.apis.paths.v1_admin_selection_concepts import V1AdminSelectionConcepts
from visier_object_configuration_python_sdk.apis.paths.v1_admin_selection_concepts_concept_id import V1AdminSelectionConceptsConceptId
from visier_object_configuration_python_sdk.apis.paths.v1_admin_selection_concepts_concept_id_configure import V1AdminSelectionConceptsConceptIdConfigure

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_ADMIN_CALCULATIONCONCEPTS: V1AdminCalculationConcepts,
        PathValues.V1_ADMIN_CALCULATIONCONCEPTS_CONCEPT_ID: V1AdminCalculationConceptsConceptId,
        PathValues.V1_ADMIN_CALCULATIONCONCEPTS_CONCEPT_ID_CONFIGURE: V1AdminCalculationConceptsConceptIdConfigure,
        PathValues.V1_ADMIN_SELECTIONCONCEPTS: V1AdminSelectionConcepts,
        PathValues.V1_ADMIN_SELECTIONCONCEPTS_CONCEPT_ID: V1AdminSelectionConceptsConceptId,
        PathValues.V1_ADMIN_SELECTIONCONCEPTS_CONCEPT_ID_CONFIGURE: V1AdminSelectionConceptsConceptIdConfigure,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_ADMIN_CALCULATIONCONCEPTS: V1AdminCalculationConcepts,
        PathValues.V1_ADMIN_CALCULATIONCONCEPTS_CONCEPT_ID: V1AdminCalculationConceptsConceptId,
        PathValues.V1_ADMIN_CALCULATIONCONCEPTS_CONCEPT_ID_CONFIGURE: V1AdminCalculationConceptsConceptIdConfigure,
        PathValues.V1_ADMIN_SELECTIONCONCEPTS: V1AdminSelectionConcepts,
        PathValues.V1_ADMIN_SELECTIONCONCEPTS_CONCEPT_ID: V1AdminSelectionConceptsConceptId,
        PathValues.V1_ADMIN_SELECTIONCONCEPTS_CONCEPT_ID_CONFIGURE: V1AdminSelectionConceptsConceptIdConfigure,
    }
)
