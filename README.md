# dev-spaces_test, CASE 1: VSCODE_DEFAULT_WORKSPACE points on real workspace file

```yaml
schemaVersion: 2.1.0
metadata:
  name: openshift_test_case_1
components:
  - name: tools
    container:
      image: registry.redhat.io/devspaces/udi-rhel8
      env:
        - name: VSCODE_DEFAULT_WORKSPACE
          value: /projects/openshift-test_case_1/custom-workspace-file
```
