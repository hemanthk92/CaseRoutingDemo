"""Generated client library for datapol version v1alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.datapol.v1alpha1 import datapol_v1alpha1_messages as messages


class DatapolV1alpha1(base_api.BaseApiClient):
  """Generated client library for service datapol version v1alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://datapol.googleapis.com/'

  _PACKAGE = u'datapol'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/xapi.zoo']
  _VERSION = u'v1alpha1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'DatapolV1alpha1'
  _URL_VERSION = u'v1alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new datapol handle."""
    url = url or self.BASE_URL
    super(DatapolV1alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.data_taxonomyStores_annotationTags = self.DataTaxonomyStoresAnnotationTagsService(self)
    self.data_taxonomyStores_dataTaxonomies = self.DataTaxonomyStoresDataTaxonomiesService(self)
    self.data_taxonomyStores = self.DataTaxonomyStoresService(self)
    self.data = self.DataService(self)
    self.dataAssets = self.DataAssetsService(self)
    self.operations = self.OperationsService(self)
    self.taxonomyStores_dataTaxonomies_annotations = self.TaxonomyStoresDataTaxonomiesAnnotationsService(self)
    self.taxonomyStores_dataTaxonomies = self.TaxonomyStoresDataTaxonomiesService(self)
    self.taxonomyStores_taxonomyReports = self.TaxonomyStoresTaxonomyReportsService(self)
    self.taxonomyStores = self.TaxonomyStoresService(self)

  class DataTaxonomyStoresAnnotationTagsService(base_api.BaseApiService):
    """Service class for the data_taxonomyStores_annotationTags resource."""

    _NAME = u'data_taxonomyStores_annotationTags'

    def __init__(self, client):
      super(DatapolV1alpha1.DataTaxonomyStoresAnnotationTagsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      """Lists all visible annotation tags from a taxonomy store that are applied on.
a cloud data set.

      Args:
        request: (DatapolDataTaxonomyStoresAnnotationTagsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListAnnotationTagsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/data/{dataId}/taxonomyStores/{taxonomyStoresId}/annotationTags',
        http_method=u'GET',
        method_id=u'datapol.data.taxonomyStores.annotationTags.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'dataSubsetName', u'pageSize', u'pageToken'],
        relative_path=u'v1alpha1/{+parent}/annotationTags',
        request_field='',
        request_type_name=u'DatapolDataTaxonomyStoresAnnotationTagsListRequest',
        response_type_name=u'ListAnnotationTagsResponse',
        supports_download=False,
    )

  class DataTaxonomyStoresDataTaxonomiesService(base_api.BaseApiService):
    """Service class for the data_taxonomyStores_dataTaxonomies resource."""

    _NAME = u'data_taxonomyStores_dataTaxonomies'

    def __init__(self, client):
      super(DatapolV1alpha1.DataTaxonomyStoresDataTaxonomiesService, self).__init__(client)
      self._upload_configs = {
          }

    def ApplyAnnotationTag(self, request, global_params=None):
      """Applies an annotation tag on a cloud data set.

      Args:
        request: (DatapolDataTaxonomyStoresDataTaxonomiesApplyAnnotationTagRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AnnotationTag) The response message.
      """
      config = self.GetMethodConfig('ApplyAnnotationTag')
      return self._RunMethod(
          config, request, global_params=global_params)

    ApplyAnnotationTag.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/data/{dataId}/taxonomyStores/{taxonomyStoresId}/dataTaxonomies/{dataTaxonomiesId}:applyAnnotationTag',
        http_method=u'POST',
        method_id=u'datapol.data.taxonomyStores.dataTaxonomies.applyAnnotationTag',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}:applyAnnotationTag',
        request_field=u'applyAnnotationTagRequest',
        request_type_name=u'DatapolDataTaxonomyStoresDataTaxonomiesApplyAnnotationTagRequest',
        response_type_name=u'AnnotationTag',
        supports_download=False,
    )

    def DeleteAnnotationTag(self, request, global_params=None):
      """Deletes an annotation tag from a cloud data set.

      Args:
        request: (DatapolDataTaxonomyStoresDataTaxonomiesDeleteAnnotationTagRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('DeleteAnnotationTag')
      return self._RunMethod(
          config, request, global_params=global_params)

    DeleteAnnotationTag.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/data/{dataId}/taxonomyStores/{taxonomyStoresId}/dataTaxonomies/{dataTaxonomiesId}/annotationTag',
        http_method=u'DELETE',
        method_id=u'datapol.data.taxonomyStores.dataTaxonomies.deleteAnnotationTag',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'dataSubsetName'],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'DatapolDataTaxonomyStoresDataTaxonomiesDeleteAnnotationTagRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

  class DataTaxonomyStoresService(base_api.BaseApiService):
    """Service class for the data_taxonomyStores resource."""

    _NAME = u'data_taxonomyStores'

    def __init__(self, client):
      super(DatapolV1alpha1.DataTaxonomyStoresService, self).__init__(client)
      self._upload_configs = {
          }

  class DataService(base_api.BaseApiService):
    """Service class for the data resource."""

    _NAME = u'data'

    def __init__(self, client):
      super(DatapolV1alpha1.DataService, self).__init__(client)
      self._upload_configs = {
          }

  class DataAssetsService(base_api.BaseApiService):
    """Service class for the dataAssets resource."""

    _NAME = u'dataAssets'

    def __init__(self, client):
      super(DatapolV1alpha1.DataAssetsService, self).__init__(client)
      self._upload_configs = {
          }

    def ListResourceNames(self, request, global_params=None):
      """Lists all cloud data assets with given predicates.

      Args:
        request: (DatapolDataAssetsListResourceNamesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListAssetsResponse) The response message.
      """
      config = self.GetMethodConfig('ListResourceNames')
      return self._RunMethod(
          config, request, global_params=global_params)

    ListResourceNames.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'datapol.dataAssets.listResourceNames',
        ordered_params=[],
        path_params=[],
        query_params=[u'annotatableOnly', u'annotations', u'filter', u'includeAnnotatedByGroup', u'pageSize', u'pageToken'],
        relative_path=u'v1alpha1/dataAssets:ListResourceNames',
        request_field='',
        request_type_name=u'DatapolDataAssetsListResourceNamesRequest',
        response_type_name=u'ListAssetsResponse',
        supports_download=False,
    )

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = u'operations'

    def __init__(self, client):
      super(DatapolV1alpha1.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      """Gets the latest state of a long-running operation.

      Args:
        request: (DatapolOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'datapol.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'DatapolOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class TaxonomyStoresDataTaxonomiesAnnotationsService(base_api.BaseApiService):
    """Service class for the taxonomyStores_dataTaxonomies_annotations resource."""

    _NAME = u'taxonomyStores_dataTaxonomies_annotations'

    def __init__(self, client):
      super(DatapolV1alpha1.TaxonomyStoresDataTaxonomiesAnnotationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates an annotation in a taxonomy.

      Args:
        request: (DatapolTaxonomyStoresDataTaxonomiesAnnotationsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Annotation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}/dataTaxonomies/{dataTaxonomiesId}/annotations',
        http_method=u'POST',
        method_id=u'datapol.taxonomyStores.dataTaxonomies.annotations.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha1/{+parent}/annotations',
        request_field=u'annotation',
        request_type_name=u'DatapolTaxonomyStoresDataTaxonomiesAnnotationsCreateRequest',
        response_type_name=u'Annotation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes an annotation. Also deletes all member annotations if the given.
annotation is a group annotation.

      Args:
        request: (DatapolTaxonomyStoresDataTaxonomiesAnnotationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}/dataTaxonomies/{dataTaxonomiesId}/annotations/{annotationsId}',
        http_method=u'DELETE',
        method_id=u'datapol.taxonomyStores.dataTaxonomies.annotations.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'DatapolTaxonomyStoresDataTaxonomiesAnnotationsDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets definition of an annotation.

      Args:
        request: (DatapolTaxonomyStoresDataTaxonomiesAnnotationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Annotation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}/dataTaxonomies/{dataTaxonomiesId}/annotations/{annotationsId}',
        http_method=u'GET',
        method_id=u'datapol.taxonomyStores.dataTaxonomies.annotations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'DatapolTaxonomyStoresDataTaxonomiesAnnotationsGetRequest',
        response_type_name=u'Annotation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists all annotations in a taxonomy.

      Args:
        request: (DatapolTaxonomyStoresDataTaxonomiesAnnotationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListAnnotationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}/dataTaxonomies/{dataTaxonomiesId}/annotations',
        http_method=u'GET',
        method_id=u'datapol.taxonomyStores.dataTaxonomies.annotations.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha1/{+parent}/annotations',
        request_field='',
        request_type_name=u'DatapolTaxonomyStoresDataTaxonomiesAnnotationsListRequest',
        response_type_name=u'ListAnnotationsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      """Updates an annotation. Currently only support updating descriptions.

      Args:
        request: (DatapolTaxonomyStoresDataTaxonomiesAnnotationsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Annotation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}/dataTaxonomies/{dataTaxonomiesId}/annotations/{annotationsId}',
        http_method=u'PATCH',
        method_id=u'datapol.taxonomyStores.dataTaxonomies.annotations.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1alpha1/{+name}',
        request_field=u'annotation',
        request_type_name=u'DatapolTaxonomyStoresDataTaxonomiesAnnotationsPatchRequest',
        response_type_name=u'Annotation',
        supports_download=False,
    )

  class TaxonomyStoresDataTaxonomiesService(base_api.BaseApiService):
    """Service class for the taxonomyStores_dataTaxonomies resource."""

    _NAME = u'taxonomyStores_dataTaxonomies'

    def __init__(self, client):
      super(DatapolV1alpha1.TaxonomyStoresDataTaxonomiesService, self).__init__(client)
      self._upload_configs = {
          }

    def Copy(self, request, global_params=None):
      """Copy an annotation to a given taxonomy. Copy will fail if there is an.
annotation with the same in the taxonomy.

      Args:
        request: (DatapolTaxonomyStoresDataTaxonomiesCopyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Annotation) The response message.
      """
      config = self.GetMethodConfig('Copy')
      return self._RunMethod(
          config, request, global_params=global_params)

    Copy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}/dataTaxonomies/{dataTaxonomiesId}:copy',
        http_method=u'POST',
        method_id=u'datapol.taxonomyStores.dataTaxonomies.copy',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha1/{+parent}:copy',
        request_field=u'copyAnnotationRequest',
        request_type_name=u'DatapolTaxonomyStoresDataTaxonomiesCopyRequest',
        response_type_name=u'Annotation',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      """Creates a new data taxonomy in a given taxonomy store.

      Args:
        request: (DatapolTaxonomyStoresDataTaxonomiesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DataTaxonomy) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}/dataTaxonomies',
        http_method=u'POST',
        method_id=u'datapol.taxonomyStores.dataTaxonomies.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha1/{+parent}/dataTaxonomies',
        request_field=u'dataTaxonomy',
        request_type_name=u'DatapolTaxonomyStoresDataTaxonomiesCreateRequest',
        response_type_name=u'DataTaxonomy',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes a taxonomy from a taxonomy store. This operation will also delete.
all annotations in this taxonomy.

      Args:
        request: (DatapolTaxonomyStoresDataTaxonomiesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}/dataTaxonomies/{dataTaxonomiesId}',
        http_method=u'DELETE',
        method_id=u'datapol.taxonomyStores.dataTaxonomies.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'DatapolTaxonomyStoresDataTaxonomiesDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Returns the taxonomy referred by name. Size of a taxonomy is at most 100KB.

      Args:
        request: (DatapolTaxonomyStoresDataTaxonomiesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DataTaxonomy) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}/dataTaxonomies/{dataTaxonomiesId}',
        http_method=u'GET',
        method_id=u'datapol.taxonomyStores.dataTaxonomies.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'DatapolTaxonomyStoresDataTaxonomiesGetRequest',
        response_type_name=u'DataTaxonomy',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      """GetIamPolicy method for the taxonomyStores_dataTaxonomies service.

      Args:
        request: (DatapolTaxonomyStoresDataTaxonomiesGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}/dataTaxonomies/{dataTaxonomiesId}:getIamPolicy',
        http_method=u'POST',
        method_id=u'datapol.taxonomyStores.dataTaxonomies.getIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1alpha1/{+resource}:getIamPolicy',
        request_field=u'getIamPolicyRequest',
        request_type_name=u'DatapolTaxonomyStoresDataTaxonomiesGetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists all taxonomies in a taxonomy store.

      Args:
        request: (DatapolTaxonomyStoresDataTaxonomiesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDataTaxonomiesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}/dataTaxonomies',
        http_method=u'GET',
        method_id=u'datapol.taxonomyStores.dataTaxonomies.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha1/{+parent}/dataTaxonomies',
        request_field='',
        request_type_name=u'DatapolTaxonomyStoresDataTaxonomiesListRequest',
        response_type_name=u'ListDataTaxonomiesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      """Updates a taxonomy. Currently only support updating descriptions.

      Args:
        request: (DatapolTaxonomyStoresDataTaxonomiesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DataTaxonomy) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}/dataTaxonomies/{dataTaxonomiesId}',
        http_method=u'PATCH',
        method_id=u'datapol.taxonomyStores.dataTaxonomies.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1alpha1/{+name}',
        request_field=u'dataTaxonomy',
        request_type_name=u'DatapolTaxonomyStoresDataTaxonomiesPatchRequest',
        response_type_name=u'DataTaxonomy',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      """SetIamPolicy method for the taxonomyStores_dataTaxonomies service.

      Args:
        request: (DatapolTaxonomyStoresDataTaxonomiesSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}/dataTaxonomies/{dataTaxonomiesId}:setIamPolicy',
        http_method=u'POST',
        method_id=u'datapol.taxonomyStores.dataTaxonomies.setIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1alpha1/{+resource}:setIamPolicy',
        request_field=u'setIamPolicyRequest',
        request_type_name=u'DatapolTaxonomyStoresDataTaxonomiesSetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

  class TaxonomyStoresTaxonomyReportsService(base_api.BaseApiService):
    """Service class for the taxonomyStores_taxonomyReports resource."""

    _NAME = u'taxonomyStores_taxonomyReports'

    def __init__(self, client):
      super(DatapolV1alpha1.TaxonomyStoresTaxonomyReportsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a taxonomy report.

      Args:
        request: (DatapolTaxonomyStoresTaxonomyReportsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TaxonomyReport) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}/taxonomyReports',
        http_method=u'POST',
        method_id=u'datapol.taxonomyStores.taxonomyReports.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha1/{+parent}/taxonomyReports',
        request_field=u'taxonomyReport',
        request_type_name=u'DatapolTaxonomyStoresTaxonomyReportsCreateRequest',
        response_type_name=u'TaxonomyReport',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes a taxonomy report.

      Args:
        request: (DatapolTaxonomyStoresTaxonomyReportsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}/taxonomyReports/{taxonomyReportsId}',
        http_method=u'DELETE',
        method_id=u'datapol.taxonomyStores.taxonomyReports.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'DatapolTaxonomyStoresTaxonomyReportsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets a taxonomy report.

      Args:
        request: (DatapolTaxonomyStoresTaxonomyReportsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TaxonomyReport) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}/taxonomyReports/{taxonomyReportsId}',
        http_method=u'GET',
        method_id=u'datapol.taxonomyStores.taxonomyReports.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'DatapolTaxonomyStoresTaxonomyReportsGetRequest',
        response_type_name=u'TaxonomyReport',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists all taxonomy reports for the taxonomy store.

      Args:
        request: (DatapolTaxonomyStoresTaxonomyReportsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListTaxonomyReportsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}/taxonomyReports',
        http_method=u'GET',
        method_id=u'datapol.taxonomyStores.taxonomyReports.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha1/{+parent}/taxonomyReports',
        request_field='',
        request_type_name=u'DatapolTaxonomyStoresTaxonomyReportsListRequest',
        response_type_name=u'ListTaxonomyReportsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      """Updates a taxonomy report.

      Args:
        request: (DatapolTaxonomyStoresTaxonomyReportsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TaxonomyReport) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}/taxonomyReports/{taxonomyReportsId}',
        http_method=u'PATCH',
        method_id=u'datapol.taxonomyStores.taxonomyReports.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1alpha1/{+name}',
        request_field=u'taxonomyReport',
        request_type_name=u'DatapolTaxonomyStoresTaxonomyReportsPatchRequest',
        response_type_name=u'TaxonomyReport',
        supports_download=False,
    )

  class TaxonomyStoresService(base_api.BaseApiService):
    """Service class for the taxonomyStores resource."""

    _NAME = u'taxonomyStores'

    def __init__(self, client):
      super(DatapolV1alpha1.TaxonomyStoresService, self).__init__(client)
      self._upload_configs = {
          }

    def Copy(self, request, global_params=None):
      """Copy a taxonomy to a given taxonomy store. Copy will fail if there is a.
taxonomy with the same display name in the taxonomy store.

      Args:
        request: (DatapolTaxonomyStoresCopyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DataTaxonomy) The response message.
      """
      config = self.GetMethodConfig('Copy')
      return self._RunMethod(
          config, request, global_params=global_params)

    Copy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}:copy',
        http_method=u'POST',
        method_id=u'datapol.taxonomyStores.copy',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha1/{+parent}:copy',
        request_field=u'copyDataTaxonomyRequest',
        request_type_name=u'DatapolTaxonomyStoresCopyRequest',
        response_type_name=u'DataTaxonomy',
        supports_download=False,
    )

    def GetCommon(self, request, global_params=None):
      """Get the read-only taxonomy store with predefined taxonomies. Taxonomies in.
this store can only be read or copied out.

      Args:
        request: (DatapolTaxonomyStoresGetCommonRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TaxonomyStore) The response message.
      """
      config = self.GetMethodConfig('GetCommon')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetCommon.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'datapol.taxonomyStores.getCommon',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path=u'v1alpha1/taxonomyStores:getCommon',
        request_field='',
        request_type_name=u'DatapolTaxonomyStoresGetCommonRequest',
        response_type_name=u'TaxonomyStore',
        supports_download=False,
    )

    def GetDefault(self, request, global_params=None):
      """Get the taxonomy store that can be used in the given project to create,.
modify, and use taxonomies.

      Args:
        request: (DatapolTaxonomyStoresGetDefaultRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TaxonomyStore) The response message.
      """
      config = self.GetMethodConfig('GetDefault')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetDefault.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'datapol.taxonomyStores.getDefault',
        ordered_params=[],
        path_params=[],
        query_params=[u'projectId'],
        relative_path=u'v1alpha1/taxonomyStores:getDefault',
        request_field='',
        request_type_name=u'DatapolTaxonomyStoresGetDefaultRequest',
        response_type_name=u'TaxonomyStore',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      """GetIamPolicy method for the taxonomyStores service.

      Args:
        request: (DatapolTaxonomyStoresGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}:getIamPolicy',
        http_method=u'POST',
        method_id=u'datapol.taxonomyStores.getIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1alpha1/{+resource}:getIamPolicy',
        request_field=u'getIamPolicyRequest',
        request_type_name=u'DatapolTaxonomyStoresGetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      """SetIamPolicy method for the taxonomyStores service.

      Args:
        request: (DatapolTaxonomyStoresSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/taxonomyStores/{taxonomyStoresId}:setIamPolicy',
        http_method=u'POST',
        method_id=u'datapol.taxonomyStores.setIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1alpha1/{+resource}:setIamPolicy',
        request_field=u'setIamPolicyRequest',
        request_type_name=u'DatapolTaxonomyStoresSetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )
