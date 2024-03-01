# dev-spaces_test, CASE 2: VSCODE_DEFAULT_WORKSPACE is not defined, but there is .code-workspace file in the repository root
```yaml
schemaVersion: 2.1.0
metadata:
  name: openshift_test_case_2
components:
  - name: tools
    container:
      image: registry.redhat.io/devspaces/udi-rhel8
      env:
        - name: VSCODE_DEFAULT_WORKSPACE
          value: /projects/dev-spaces-test/custom-workspace-file
```
