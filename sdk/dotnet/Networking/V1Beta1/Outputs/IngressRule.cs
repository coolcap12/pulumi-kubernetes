// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Outputs.Networking.V1Beta1
{

    [OutputType]
    public sealed class IngressRule
    {
        /// <summary>
        /// Host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the "host" part of the URI as defined in the RFC: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to the
        /// 	  IP in the Spec of the parent Ingress.
        /// 2. The `:` delimiter is not respected because ports are not allowed.
        /// 	  Currently the port of an Ingress is implicitly :80 for http and
        /// 	  :443 for https.
        /// Both these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue.
        /// </summary>
        public readonly string Host;
        public readonly Pulumi.Kubernetes.Types.Outputs.Networking.V1Beta1.HTTPIngressRuleValue Http;

        [OutputConstructor]
        private IngressRule(
            string host,

            Pulumi.Kubernetes.Types.Outputs.Networking.V1Beta1.HTTPIngressRuleValue http)
        {
            Host = host;
            Http = http;
        }
    }
}
