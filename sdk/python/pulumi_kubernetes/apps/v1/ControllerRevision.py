import pulumi
import pulumi.runtime

class ControllerRevision(pulumi.CustomResource):
    """
    ControllerRevision implements an immutable snapshot of state data. Clients are responsible for
    serializing and deserializing the objects that contain their internal state. Once a
    ControllerRevision has been successfully created, it can not be updated. The API Server will
    fail validation of all requests that attempt to mutate the Data field. ControllerRevisions may,
    however, be deleted. Note that, due to its use by both the DaemonSet and StatefulSet controllers
    for update and rollback, this object is beta. However, it may be subject to name and
    representation changes in future releases, and clients should not depend on its stability. It is
    primarily for internal use by controllers.
    """
    def __init__(self, __name__, __opts__=None, data=None, metadata=None, revision=None):
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'apps/v1'
        self.apiVersion = 'apps/v1'

        __props__['kind'] = 'ControllerRevision'
        self.kind = 'ControllerRevision'

        if not revision:
            raise TypeError('Missing required property revision')
        elif not isinstance(revision, int):
            raise TypeError('Expected property aliases to be a int')
        self.revision = revision
        """
        Revision indicates the revision of the state represented by Data.
        """
        __props__['revision'] = revision

        if data and not isinstance(data, dict):
            raise TypeError('Expected property aliases to be a dict')
        self.data = data
        """
        Data is the serialized representation of the state.
        """
        __props__['data'] = data

        if metadata and not isinstance(metadata, dict):
            raise TypeError('Expected property aliases to be a dict')
        self.metadata = metadata
        """
        Standard object's metadata. More info:
        https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata
        """
        __props__['metadata'] = metadata

        super(ControllerRevision, self).__init__(
            "kubernetes:apps/v1:ControllerRevision",
            __name__,
            __props__,
            __opts__)