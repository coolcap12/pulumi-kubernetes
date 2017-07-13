// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";

export class Account extends lumi.NamedResource implements AccountArgs {
    public readonly cloudwatchRoleArn?: string;
    public readonly throttleSettings?: { burstLimit?: number, rateLimit?: number }[];

    constructor(name: string, args: AccountArgs) {
        super(name);
        this.cloudwatchRoleArn = args.cloudwatchRoleArn;
        this.throttleSettings = args.throttleSettings;
    }
}

export interface AccountArgs {
    readonly cloudwatchRoleArn?: string;
    readonly throttleSettings?: { burstLimit?: number, rateLimit?: number }[];
}
