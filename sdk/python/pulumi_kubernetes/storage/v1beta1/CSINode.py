# *** WARNING: this file was generated by the Pulumi Kubernetes codegen tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
from typing import Optional

import pulumi
import pulumi.runtime
from pulumi import Input, ResourceOptions

from ... import tables, version


class CSINode(pulumi.CustomResource):
    """
    CSINode holds information about all CSI drivers installed on a node. CSI drivers do not need to
    create the CSINode object directly. As long as they use the node-driver-registrar sidecar
    container, the kubelet will automatically populate the CSINode object for the CSI driver as part
    of kubelet plugin registration. CSINode has the same name as a node. If the object is missing,
    it means either there are no CSI Drivers available on the node, or the Kubelet version is low
    enough that it doesn't create this object. CSINode has an OwnerReference that points to the
    corresponding node object.
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
    """
    metadata.name must be the Kubernetes node name.
    """

    spec: pulumi.Output[dict]
    """
    spec is the specification of CSINode
    """

    def __init__(self, resource_name, opts=None, spec=None, metadata=None, __name__=None, __opts__=None):
        """
        Create a CSINode resource with the given unique name, arguments, and options.

        :param str resource_name: The _unique_ name of the resource.
        :param pulumi.ResourceOptions opts: A bag of options that control this resource's behavior.
        :param pulumi.Input[dict] spec: spec is the specification of CSINode
        :param pulumi.Input[dict] metadata: metadata.name must be the Kubernetes node name.
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

        __props__['apiVersion'] = 'storage.k8s.io/v1beta1'
        __props__['kind'] = 'CSINode'
        if spec is None:
            raise TypeError('Missing required property spec')
        __props__['spec'] = spec
        __props__['metadata'] = metadata

        __props__['status'] = None

        if opts is None:
            opts = pulumi.ResourceOptions()
        if opts.version is None:
            opts.version = version.get_version()

        super(CSINode, self).__init__(
            "kubernetes:storage.k8s.io/v1beta1:CSINode",
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(name: str, id: Input[str], opts: Optional[ResourceOptions] = None):
        opts = ResourceOptions(id=id) if opts is None else opts.merge(ResourceOptions(id=id))
        return CSINode(name, opts)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
