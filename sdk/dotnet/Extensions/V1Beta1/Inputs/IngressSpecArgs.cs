// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Inputs.Extensions.V1Beta1
{

    /// <summary>
    /// IngressSpec describes the Ingress the user wishes to exist.
    /// </summary>
    public class IngressSpecArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A default backend capable of servicing requests that don't match any rule. At least one of 'backend' or 'rules' must be specified. This field is optional to allow the loadbalancer controller or defaulting logic to specify a global default.
        /// </summary>
        [Input("backend")]
        public Input<Pulumi.Kubernetes.Types.Inputs.Extensions.V1Beta1.IngressBackendArgs>? Backend { get; set; }

        [Input("rules")]
        private InputList<Pulumi.Kubernetes.Types.Inputs.Extensions.V1Beta1.IngressRuleArgs>? _rules;

        /// <summary>
        /// A list of host rules used to configure the Ingress. If unspecified, or no rule matches, all traffic is sent to the default backend.
        /// </summary>
        public InputList<Pulumi.Kubernetes.Types.Inputs.Extensions.V1Beta1.IngressRuleArgs> Rules
        {
            get => _rules ?? (_rules = new InputList<Pulumi.Kubernetes.Types.Inputs.Extensions.V1Beta1.IngressRuleArgs>());
            set => _rules = value;
        }

        [Input("tls")]
        private InputList<Pulumi.Kubernetes.Types.Inputs.Extensions.V1Beta1.IngressTLSArgs>? _tls;

        /// <summary>
        /// TLS configuration. Currently the Ingress only supports a single TLS port, 443. If multiple members of this list specify different hosts, they will be multiplexed on the same port according to the hostname specified through the SNI TLS extension, if the ingress controller fulfilling the ingress supports SNI.
        /// </summary>
        public InputList<Pulumi.Kubernetes.Types.Inputs.Extensions.V1Beta1.IngressTLSArgs> Tls
        {
            get => _tls ?? (_tls = new InputList<Pulumi.Kubernetes.Types.Inputs.Extensions.V1Beta1.IngressTLSArgs>());
            set => _tls = value;
        }

        public IngressSpecArgs()
        {
        }
    }
}
