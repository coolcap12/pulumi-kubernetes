# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from . import outputs
from ... import core as _core
from ... import meta as _meta

__all__ = [
    'VolumeAttachment',
    'VolumeAttachmentSource',
    'VolumeAttachmentSpec',
    'VolumeAttachmentStatus',
    'VolumeError',
]

@pulumi.output_type
class VolumeAttachment(dict):
    """
    VolumeAttachment captures the intent to attach or detach the specified volume to/from the specified node.

    VolumeAttachment objects are non-namespaced.
    """
    def __init__(__self__, *,
                 spec: 'outputs.VolumeAttachmentSpec',
                 api_version: Optional[str] = None,
                 kind: Optional[str] = None,
                 metadata: Optional['_meta.v1.outputs.ObjectMeta'] = None,
                 status: Optional['outputs.VolumeAttachmentStatus'] = None):
        """
        VolumeAttachment captures the intent to attach or detach the specified volume to/from the specified node.

        VolumeAttachment objects are non-namespaced.
        :param 'VolumeAttachmentSpecArgs' spec: Specification of the desired attach/detach volume behavior. Populated by the Kubernetes system.
        :param str api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param str kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param '_meta.v1.ObjectMetaArgs' metadata: Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        :param 'VolumeAttachmentStatusArgs' status: Status of the VolumeAttachment request. Populated by the entity completing the attach or detach operation, i.e. the external-attacher.
        """
        pulumi.set(__self__, "spec", spec)
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'storage.k8s.io/v1alpha1')
        if kind is not None:
            pulumi.set(__self__, "kind", 'VolumeAttachment')
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def spec(self) -> 'outputs.VolumeAttachmentSpec':
        """
        Specification of the desired attach/detach volume behavior. Populated by the Kubernetes system.
        """
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[str]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def metadata(self) -> Optional['_meta.v1.outputs.ObjectMeta']:
        """
        Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def status(self) -> Optional['outputs.VolumeAttachmentStatus']:
        """
        Status of the VolumeAttachment request. Populated by the entity completing the attach or detach operation, i.e. the external-attacher.
        """
        return pulumi.get(self, "status")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class VolumeAttachmentSource(dict):
    """
    VolumeAttachmentSource represents a volume that should be attached. Right now only PersistenVolumes can be attached via external attacher, in future we may allow also inline volumes in pods. Exactly one member can be set.
    """
    def __init__(__self__, *,
                 inline_volume_spec: Optional['_core.v1.outputs.PersistentVolumeSpec'] = None,
                 persistent_volume_name: Optional[str] = None):
        """
        VolumeAttachmentSource represents a volume that should be attached. Right now only PersistenVolumes can be attached via external attacher, in future we may allow also inline volumes in pods. Exactly one member can be set.
        :param '_core.v1.PersistentVolumeSpecArgs' inline_volume_spec: inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod's inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod's inline VolumeSource to a PersistentVolumeSpec. This field is alpha-level and is only honored by servers that enabled the CSIMigration feature.
        :param str persistent_volume_name: Name of the persistent volume to attach.
        """
        if inline_volume_spec is not None:
            pulumi.set(__self__, "inline_volume_spec", inline_volume_spec)
        if persistent_volume_name is not None:
            pulumi.set(__self__, "persistent_volume_name", persistent_volume_name)

    @property
    @pulumi.getter(name="inlineVolumeSpec")
    def inline_volume_spec(self) -> Optional['_core.v1.outputs.PersistentVolumeSpec']:
        """
        inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod's inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod's inline VolumeSource to a PersistentVolumeSpec. This field is alpha-level and is only honored by servers that enabled the CSIMigration feature.
        """
        return pulumi.get(self, "inline_volume_spec")

    @property
    @pulumi.getter(name="persistentVolumeName")
    def persistent_volume_name(self) -> Optional[str]:
        """
        Name of the persistent volume to attach.
        """
        return pulumi.get(self, "persistent_volume_name")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class VolumeAttachmentSpec(dict):
    """
    VolumeAttachmentSpec is the specification of a VolumeAttachment request.
    """
    def __init__(__self__, *,
                 attacher: str,
                 node_name: str,
                 source: 'outputs.VolumeAttachmentSource'):
        """
        VolumeAttachmentSpec is the specification of a VolumeAttachment request.
        :param str attacher: Attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName().
        :param str node_name: The node that the volume should be attached to.
        :param 'VolumeAttachmentSourceArgs' source: Source represents the volume that should be attached.
        """
        pulumi.set(__self__, "attacher", attacher)
        pulumi.set(__self__, "node_name", node_name)
        pulumi.set(__self__, "source", source)

    @property
    @pulumi.getter
    def attacher(self) -> str:
        """
        Attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName().
        """
        return pulumi.get(self, "attacher")

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> str:
        """
        The node that the volume should be attached to.
        """
        return pulumi.get(self, "node_name")

    @property
    @pulumi.getter
    def source(self) -> 'outputs.VolumeAttachmentSource':
        """
        Source represents the volume that should be attached.
        """
        return pulumi.get(self, "source")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class VolumeAttachmentStatus(dict):
    """
    VolumeAttachmentStatus is the status of a VolumeAttachment request.
    """
    def __init__(__self__, *,
                 attached: bool,
                 attach_error: Optional['outputs.VolumeError'] = None,
                 attachment_metadata: Optional[Mapping[str, str]] = None,
                 detach_error: Optional['outputs.VolumeError'] = None):
        """
        VolumeAttachmentStatus is the status of a VolumeAttachment request.
        :param bool attached: Indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.
        :param 'VolumeErrorArgs' attach_error: The last error encountered during attach operation, if any. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.
        :param Mapping[str, str] attachment_metadata: Upon successful attach, this field is populated with any information returned by the attach operation that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.
        :param 'VolumeErrorArgs' detach_error: The last error encountered during detach operation, if any. This field must only be set by the entity completing the detach operation, i.e. the external-attacher.
        """
        pulumi.set(__self__, "attached", attached)
        if attach_error is not None:
            pulumi.set(__self__, "attach_error", attach_error)
        if attachment_metadata is not None:
            pulumi.set(__self__, "attachment_metadata", attachment_metadata)
        if detach_error is not None:
            pulumi.set(__self__, "detach_error", detach_error)

    @property
    @pulumi.getter
    def attached(self) -> bool:
        """
        Indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.
        """
        return pulumi.get(self, "attached")

    @property
    @pulumi.getter(name="attachError")
    def attach_error(self) -> Optional['outputs.VolumeError']:
        """
        The last error encountered during attach operation, if any. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.
        """
        return pulumi.get(self, "attach_error")

    @property
    @pulumi.getter(name="attachmentMetadata")
    def attachment_metadata(self) -> Optional[Mapping[str, str]]:
        """
        Upon successful attach, this field is populated with any information returned by the attach operation that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.
        """
        return pulumi.get(self, "attachment_metadata")

    @property
    @pulumi.getter(name="detachError")
    def detach_error(self) -> Optional['outputs.VolumeError']:
        """
        The last error encountered during detach operation, if any. This field must only be set by the entity completing the detach operation, i.e. the external-attacher.
        """
        return pulumi.get(self, "detach_error")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class VolumeError(dict):
    """
    VolumeError captures an error encountered during a volume operation.
    """
    def __init__(__self__, *,
                 message: Optional[str] = None,
                 time: Optional[str] = None):
        """
        VolumeError captures an error encountered during a volume operation.
        :param str message: String detailing the error encountered during Attach or Detach operation. This string maybe logged, so it should not contain sensitive information.
        :param str time: Time the error was encountered.
        """
        if message is not None:
            pulumi.set(__self__, "message", message)
        if time is not None:
            pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter
    def message(self) -> Optional[str]:
        """
        String detailing the error encountered during Attach or Detach operation. This string maybe logged, so it should not contain sensitive information.
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def time(self) -> Optional[str]:
        """
        Time the error was encountered.
        """
        return pulumi.get(self, "time")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

