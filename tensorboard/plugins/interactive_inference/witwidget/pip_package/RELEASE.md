# To release a new version of witwidget on PyPI:

1. Update tensorboard/plugins/interactive_inference/witwidget/version.py (set release version, remove 'dev')
2. `bazel run tensorboard/plugins/interactive_inference/witwidget/pip_package:build_pip_package`
3. Commit the version.py change.
