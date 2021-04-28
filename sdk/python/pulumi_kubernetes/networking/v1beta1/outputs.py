# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ... import core as _core
from ... import meta as _meta

__all__ = [
    'HTTPIngressPath',
    'HTTPIngressRuleValue',
    'Ingress',
    'IngressBackend',
    'IngressRule',
    'IngressSpec',
    'IngressStatus',
    'IngressTLS',
]

@pulumi.output_type
class HTTPIngressPath(dict):
    """
    HTTPIngressPath associates a path regex with a backend. Incoming urls matching the path are forwarded to the backend.
    """
    def __init__(__self__, *,
                 backend: 'outputs.IngressBackend',
                 path: Optional[str] = None):
        """
        HTTPIngressPath associates a path regex with a backend. Incoming urls matching the path are forwarded to the backend.
        :param 'IngressBackendArgs' backend: Backend defines the referenced service endpoint to which the traffic will be forwarded to.
        :param str path: Path is an extended POSIX regex as defined by IEEE Std 1003.1, (i.e this follows the egrep/unix syntax, not the perl syntax) matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a '/'. If unspecified, the path defaults to a catch all sending traffic to the backend.
        """
        pulumi.set(__self__, "backend", backend)
        if path is not None:
            pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter
    def backend(self) -> 'outputs.IngressBackend':
        """
        Backend defines the referenced service endpoint to which the traffic will be forwarded to.
        """
        return pulumi.get(self, "backend")

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        """
        Path is an extended POSIX regex as defined by IEEE Std 1003.1, (i.e this follows the egrep/unix syntax, not the perl syntax) matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a '/'. If unspecified, the path defaults to a catch all sending traffic to the backend.
        """
        return pulumi.get(self, "path")


@pulumi.output_type
class HTTPIngressRuleValue(dict):
    """
    HTTPIngressRuleValue is a list of http selectors pointing to backends. In the example: http://<host>/<path>?<searchpart> -> backend where where parts of the url correspond to RFC 3986, this resource will be used to match against everything after the last '/' and before the first '?' or '#'.
    """
    def __init__(__self__, *,
                 paths: Sequence['outputs.HTTPIngressPath']):
        """
        HTTPIngressRuleValue is a list of http selectors pointing to backends. In the example: http://<host>/<path>?<searchpart> -> backend where where parts of the url correspond to RFC 3986, this resource will be used to match against everything after the last '/' and before the first '?' or '#'.
        :param Sequence['HTTPIngressPathArgs'] paths: A collection of paths that map requests to backends.
        """
        pulumi.set(__self__, "paths", paths)

    @property
    @pulumi.getter
    def paths(self) -> Sequence['outputs.HTTPIngressPath']:
        """
        A collection of paths that map requests to backends.
        """
        return pulumi.get(self, "paths")


@pulumi.output_type
class Ingress(dict):
    """
    Ingress is a collection of rules that allow inbound connections to reach the endpoints defined by a backend. An Ingress can be configured to give services externally-reachable urls, load balance traffic, terminate SSL, offer name based virtual hosting etc.

    This resource waits until its status is ready before registering success
    for create/update, and populating output properties from the current state of the resource.
    The following conditions are used to determine whether the resource creation has
    succeeded or failed:

    1.  Ingress object exists.
    2.  Endpoint objects exist with matching names for each Ingress path (except when Service
        type is ExternalName).
    3.  Ingress entry exists for '.status.loadBalancer.ingress'.

    If the Ingress has not reached a Ready state after 10 minutes, it will
    time out and mark the resource update as Failed. You can override the default timeout value
    by setting the 'customTimeouts' option on the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "apiVersion":
            suggest = "api_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in Ingress. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        Ingress.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        Ingress.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 api_version: Optional[str] = None,
                 kind: Optional[str] = None,
                 metadata: Optional['_meta.v1.outputs.ObjectMeta'] = None,
                 spec: Optional['outputs.IngressSpec'] = None,
                 status: Optional['outputs.IngressStatus'] = None):
        """
        Ingress is a collection of rules that allow inbound connections to reach the endpoints defined by a backend. An Ingress can be configured to give services externally-reachable urls, load balance traffic, terminate SSL, offer name based virtual hosting etc.

        This resource waits until its status is ready before registering success
        for create/update, and populating output properties from the current state of the resource.
        The following conditions are used to determine whether the resource creation has
        succeeded or failed:

        1.  Ingress object exists.
        2.  Endpoint objects exist with matching names for each Ingress path (except when Service
            type is ExternalName).
        3.  Ingress entry exists for '.status.loadBalancer.ingress'.

        If the Ingress has not reached a Ready state after 10 minutes, it will
        time out and mark the resource update as Failed. You can override the default timeout value
        by setting the 'customTimeouts' option on the resource.
        :param str api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param str kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param '_meta.v1.ObjectMetaArgs' metadata: Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        :param 'IngressSpecArgs' spec: Spec is the desired state of the Ingress. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
        :param 'IngressStatusArgs' status: Status is the current state of the Ingress. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
        """
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'networking.k8s.io/v1beta1')
        if kind is not None:
            pulumi.set(__self__, "kind", 'Ingress')
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if spec is not None:
            pulumi.set(__self__, "spec", spec)
        if status is not None:
            pulumi.set(__self__, "status", status)

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
        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def spec(self) -> Optional['outputs.IngressSpec']:
        """
        Spec is the desired state of the Ingress. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
        """
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter
    def status(self) -> Optional['outputs.IngressStatus']:
        """
        Status is the current state of the Ingress. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class IngressBackend(dict):
    """
    IngressBackend describes all endpoints for a given service and port.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "serviceName":
            suggest = "service_name"
        elif key == "servicePort":
            suggest = "service_port"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IngressBackend. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IngressBackend.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IngressBackend.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 service_name: str,
                 service_port: Any):
        """
        IngressBackend describes all endpoints for a given service and port.
        :param str service_name: Specifies the name of the referenced service.
        :param Union[int, str] service_port: Specifies the port of the referenced service.
        """
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "service_port", service_port)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        """
        Specifies the name of the referenced service.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter(name="servicePort")
    def service_port(self) -> Any:
        """
        Specifies the port of the referenced service.
        """
        return pulumi.get(self, "service_port")


@pulumi.output_type
class IngressRule(dict):
    """
    IngressRule represents the rules mapping the paths under a specified host to the related backend services. Incoming requests are first evaluated for a host match, then routed to the backend associated with the matching IngressRuleValue.
    """
    def __init__(__self__, *,
                 host: Optional[str] = None,
                 http: Optional['outputs.HTTPIngressRuleValue'] = None):
        """
        IngressRule represents the rules mapping the paths under a specified host to the related backend services. Incoming requests are first evaluated for a host match, then routed to the backend associated with the matching IngressRuleValue.
        :param str host: Host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the "host" part of the URI as defined in the RFC: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to the
               	  IP in the Spec of the parent Ingress.
               2. The `:` delimiter is not respected because ports are not allowed.
               	  Currently the port of an Ingress is implicitly :80 for http and
               	  :443 for https.
               Both these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue.
        """
        if host is not None:
            pulumi.set(__self__, "host", host)
        if http is not None:
            pulumi.set(__self__, "http", http)

    @property
    @pulumi.getter
    def host(self) -> Optional[str]:
        """
        Host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the "host" part of the URI as defined in the RFC: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to the
        	  IP in the Spec of the parent Ingress.
        2. The `:` delimiter is not respected because ports are not allowed.
        	  Currently the port of an Ingress is implicitly :80 for http and
        	  :443 for https.
        Both these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter
    def http(self) -> Optional['outputs.HTTPIngressRuleValue']:
        return pulumi.get(self, "http")


@pulumi.output_type
class IngressSpec(dict):
    """
    IngressSpec describes the Ingress the user wishes to exist.
    """
    def __init__(__self__, *,
                 backend: Optional['outputs.IngressBackend'] = None,
                 rules: Optional[Sequence['outputs.IngressRule']] = None,
                 tls: Optional[Sequence['outputs.IngressTLS']] = None):
        """
        IngressSpec describes the Ingress the user wishes to exist.
        :param 'IngressBackendArgs' backend: A default backend capable of servicing requests that don't match any rule. At least one of 'backend' or 'rules' must be specified. This field is optional to allow the loadbalancer controller or defaulting logic to specify a global default.
        :param Sequence['IngressRuleArgs'] rules: A list of host rules used to configure the Ingress. If unspecified, or no rule matches, all traffic is sent to the default backend.
        :param Sequence['IngressTLSArgs'] tls: TLS configuration. Currently the Ingress only supports a single TLS port, 443. If multiple members of this list specify different hosts, they will be multiplexed on the same port according to the hostname specified through the SNI TLS extension, if the ingress controller fulfilling the ingress supports SNI.
        """
        if backend is not None:
            pulumi.set(__self__, "backend", backend)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if tls is not None:
            pulumi.set(__self__, "tls", tls)

    @property
    @pulumi.getter
    def backend(self) -> Optional['outputs.IngressBackend']:
        """
        A default backend capable of servicing requests that don't match any rule. At least one of 'backend' or 'rules' must be specified. This field is optional to allow the loadbalancer controller or defaulting logic to specify a global default.
        """
        return pulumi.get(self, "backend")

    @property
    @pulumi.getter
    def rules(self) -> Optional[Sequence['outputs.IngressRule']]:
        """
        A list of host rules used to configure the Ingress. If unspecified, or no rule matches, all traffic is sent to the default backend.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def tls(self) -> Optional[Sequence['outputs.IngressTLS']]:
        """
        TLS configuration. Currently the Ingress only supports a single TLS port, 443. If multiple members of this list specify different hosts, they will be multiplexed on the same port according to the hostname specified through the SNI TLS extension, if the ingress controller fulfilling the ingress supports SNI.
        """
        return pulumi.get(self, "tls")


@pulumi.output_type
class IngressStatus(dict):
    """
    IngressStatus describe the current state of the Ingress.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "loadBalancer":
            suggest = "load_balancer"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IngressStatus. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IngressStatus.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IngressStatus.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 load_balancer: Optional['_core.v1.outputs.LoadBalancerStatus'] = None):
        """
        IngressStatus describe the current state of the Ingress.
        :param '_core.v1.LoadBalancerStatusArgs' load_balancer: LoadBalancer contains the current status of the load-balancer.
        """
        if load_balancer is not None:
            pulumi.set(__self__, "load_balancer", load_balancer)

    @property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> Optional['_core.v1.outputs.LoadBalancerStatus']:
        """
        LoadBalancer contains the current status of the load-balancer.
        """
        return pulumi.get(self, "load_balancer")


@pulumi.output_type
class IngressTLS(dict):
    """
    IngressTLS describes the transport layer security associated with an Ingress.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "secretName":
            suggest = "secret_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IngressTLS. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IngressTLS.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IngressTLS.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 hosts: Optional[Sequence[str]] = None,
                 secret_name: Optional[str] = None):
        """
        IngressTLS describes the transport layer security associated with an Ingress.
        :param Sequence[str] hosts: Hosts are a list of hosts included in the TLS certificate. The values in this list must match the name/s used in the tlsSecret. Defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress, if left unspecified.
        :param str secret_name: SecretName is the name of the secret used to terminate SSL traffic on 443. Field is left optional to allow SSL routing based on SNI hostname alone. If the SNI host in a listener conflicts with the "Host" header field used by an IngressRule, the SNI host is used for termination and value of the Host header is used for routing.
        """
        if hosts is not None:
            pulumi.set(__self__, "hosts", hosts)
        if secret_name is not None:
            pulumi.set(__self__, "secret_name", secret_name)

    @property
    @pulumi.getter
    def hosts(self) -> Optional[Sequence[str]]:
        """
        Hosts are a list of hosts included in the TLS certificate. The values in this list must match the name/s used in the tlsSecret. Defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress, if left unspecified.
        """
        return pulumi.get(self, "hosts")

    @property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> Optional[str]:
        """
        SecretName is the name of the secret used to terminate SSL traffic on 443. Field is left optional to allow SSL routing based on SNI hostname alone. If the SNI host in a listener conflicts with the "Host" header field used by an IngressRule, the SNI host is used for termination and value of the Host header is used for routing.
        """
        return pulumi.get(self, "secret_name")


