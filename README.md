# dev-spaces_test, CASE 3: VSCODE_DEFAULT_WORKSPACE point on nonexistent file.

```yaml
schemaVersion: 2.1.0
metadata:
  name: openshift_test_case_3
components:
  - name: tools
    container:
      image: registry.redhat.io/devspaces/udi-rhel8
      env:
        - name: VSCODE_DEFAULT_WORKSPACE
          value: .
```
