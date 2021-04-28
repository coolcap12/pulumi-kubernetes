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
    /// IngressBackend describes all endpoints for a given service and port.
    /// </summary>
    public class IngressBackendArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies the name of the referenced service.
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        /// <summary>
        /// Specifies the port of the referenced service.
        /// </summary>
        [Input("servicePort", required: true)]
        public InputUnion<int, string> ServicePort { get; set; } = null!;

        public IngressBackendArgs()
        {
        }
    }
}
