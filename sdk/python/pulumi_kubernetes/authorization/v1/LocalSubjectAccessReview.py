# *** WARNING: this file was generated by the Pulumi Kubernetes codegen tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
from typing import Optional

import pulumi
import pulumi.runtime
from pulumi import Input, ResourceOptions

from ... import tables, version


class LocalSubjectAccessReview(pulumi.CustomResource):
    """
    LocalSubjectAccessReview checks whether or not a user or group can perform an action in a given
    namespace. Having a namespace scoped resource makes it much easier to grant namespace scoped
    policy that includes permissions checking.
    """

    apiVersion: pulumi.Output[str]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should
    convert recognized schemas to the latest internal value, and may reject unrecognized values.
    More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources
    """

    kind: pulumi.Output[str]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer
    this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
    info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds
    """

    metadata: pulumi.Output[dict]
    

    spec: pulumi.Output[dict]
    """
    Spec holds information about the request being evaluated.  spec.namespace must be equal to the
    namespace you made the request against.  If empty, it is defaulted.
    """

    status: pulumi.Output[dict]
    """
    Status is filled in by the server and indicates whether the request is allowed or not
    """

    def __init__(self, resource_name, opts=None, spec=None, metadata=None, __name__=None, __opts__=None):
        """
        Create a LocalSubjectAccessReview resource with the given unique name, arguments, and options.

        :param str resource_name: The _unique_ name of the resource.
        :param pulumi.ResourceOptions opts: A bag of options that control this resource's behavior.
        :param pulumi.Input[dict] spec: Spec holds information about the request being evaluated.  spec.namespace must be
               equal to the namespace you made the request against.  If empty, it is defaulted.
        :param pulumi.Input[dict] metadata: 
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'authorization.k8s.io/v1'
        __props__['kind'] = 'LocalSubjectAccessReview'
        if spec is None:
            raise TypeError('Missing required property spec')
        __props__['spec'] = spec
        __props__['metadata'] = metadata

        __props__['status'] = None

        if opts is None:
            opts = pulumi.ResourceOptions()
        if opts.version is None:
            opts.version = version.get_version()

        super(LocalSubjectAccessReview, self).__init__(
            "kubernetes:authorization.k8s.io/v1:LocalSubjectAccessReview",
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(name: str, id: Input[str], opts: Optional[ResourceOptions] = None):
        opts = ResourceOptions(id=id) if opts is None else opts.merge(ResourceOptions(id=id))
        return LocalSubjectAccessReview(name, opts)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
