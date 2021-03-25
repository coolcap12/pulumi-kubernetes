// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "kubernetes:core/v1:Binding":
		r, err = NewBinding(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:ConfigMap":
		r, err = NewConfigMap(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:ConfigMapList":
		r, err = NewConfigMapList(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:Endpoints":
		r, err = NewEndpoints(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:EndpointsList":
		r, err = NewEndpointsList(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:EphemeralContainers":
		r, err = NewEphemeralContainers(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:Event":
		r, err = NewEvent(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:EventList":
		r, err = NewEventList(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:LimitRange":
		r, err = NewLimitRange(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:LimitRangeList":
		r, err = NewLimitRangeList(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:Namespace":
		r, err = NewNamespace(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:NamespaceList":
		r, err = NewNamespaceList(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:Node":
		r, err = NewNode(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:NodeList":
		r, err = NewNodeList(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:PersistentVolume":
		r, err = NewPersistentVolume(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:PersistentVolumeClaim":
		r, err = NewPersistentVolumeClaim(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:PersistentVolumeClaimList":
		r, err = NewPersistentVolumeClaimList(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:PersistentVolumeList":
		r, err = NewPersistentVolumeList(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:Pod":
		r, err = NewPod(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:PodList":
		r, err = NewPodList(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:PodTemplate":
		r, err = NewPodTemplate(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:PodTemplateList":
		r, err = NewPodTemplateList(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:ReplicationController":
		r, err = NewReplicationController(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:ReplicationControllerList":
		r, err = NewReplicationControllerList(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:ResourceQuota":
		r, err = NewResourceQuota(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:ResourceQuotaList":
		r, err = NewResourceQuotaList(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:Secret":
		r, err = NewSecret(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:SecretList":
		r, err = NewSecretList(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:Service":
		r, err = NewService(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:ServiceAccount":
		r, err = NewServiceAccount(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:ServiceAccountList":
		r, err = NewServiceAccountList(ctx, name, nil, pulumi.URN_(urn))
	case "kubernetes:core/v1:ServiceList":
		r, err = NewServiceList(ctx, name, nil, pulumi.URN_(urn))
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	return
}

func init() {
	version, err := kubernetes.PkgVersion()
	if err != nil {
		fmt.Println("failed to determine package version. defaulting to v1: %v", err)
	}
	pulumi.RegisterResourceModule(
		"kubernetes",
		"core/v1",
		&module{version},
	)
}
