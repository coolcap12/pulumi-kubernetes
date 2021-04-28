// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Inputs.Storage.V1Beta1
{

    /// <summary>
    /// VolumeAttachmentSource represents a volume that should be attached. Right now only PersistenVolumes can be attached via external attacher, in future we may allow also inline volumes in pods. Exactly one member can be set.
    /// </summary>
    public class VolumeAttachmentSourceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod's inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod's inline VolumeSource to a PersistentVolumeSpec. This field is alpha-level and is only honored by servers that enabled the CSIMigration feature.
        /// </summary>
        [Input("inlineVolumeSpec")]
        public Input<Pulumi.Kubernetes.Types.Inputs.Core.V1.PersistentVolumeSpecArgs>? InlineVolumeSpec { get; set; }

        /// <summary>
        /// Name of the persistent volume to attach.
        /// </summary>
        [Input("persistentVolumeName")]
        public Input<string>? PersistentVolumeName { get; set; }

        public VolumeAttachmentSourceArgs()
        {
        }
    }
}
