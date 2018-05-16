// Copyright 2016-2018, Pulumi Corporation.  All rights reserved.

package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"

	"github.com/pulumi/pulumi-kubernetes/pkg/gen"
)

func main() {
	if len(os.Args) < 4 {
		log.Fatal("Usage: gen <swagger-file> <template-dir> <out-dir>")
	}

	swagger, err := ioutil.ReadFile(os.Args[1])
	if err != nil {
		panic(err)
	}

	data := map[string]interface{}{}
	err = json.Unmarshal(swagger, &data)
	if err != nil {
		panic(err)
	}

	templateDir := os.Args[2]
	inputAPIts, ouputAPIts, providerts, packagejson, err := gen.NodeJSClient(data, templateDir)
	if err != nil {
		panic(err)
	}

	outdir := os.Args[3]
	err = os.MkdirAll(outdir, 0700)
	if err != nil {
		panic(err)
	}

	typesDir := fmt.Sprintf("%s/types", outdir)
	err = os.MkdirAll(typesDir, 0700)
	if err != nil {
		panic(err)
	}

	err = ioutil.WriteFile(fmt.Sprintf("%s/input.ts", typesDir), []byte(inputAPIts), 0777)
	if err != nil {
		panic(err)
	}

	err = ioutil.WriteFile(fmt.Sprintf("%s/output.ts", typesDir), []byte(ouputAPIts), 0777)
	if err != nil {
		panic(err)
	}

	err = ioutil.WriteFile(fmt.Sprintf("%s/provider.ts", outdir), []byte(providerts), 0777)
	if err != nil {
		panic(err)
	}

	err = ioutil.WriteFile(fmt.Sprintf("%s/package.json", outdir), []byte(packagejson), 0777)
	if err != nil {
		panic(err)
	}
	fmt.Printf("%s/package.json\n", outdir)
	fmt.Println(err)
}
