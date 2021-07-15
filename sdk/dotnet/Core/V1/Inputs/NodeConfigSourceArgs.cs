// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Inputs.Core.V1
{

    /// <summary>
    /// NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil. This API is deprecated since 1.22
    /// </summary>
    public class NodeConfigSourceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ConfigMap is a reference to a Node's ConfigMap
        /// </summary>
        [Input("configMap")]
        public Input<Pulumi.Kubernetes.Types.Inputs.Core.V1.ConfigMapNodeConfigSourceArgs>? ConfigMap { get; set; }

        public NodeConfigSourceArgs()
        {
        }
    }
}
