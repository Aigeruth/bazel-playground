load(
  "@io_bazel_rules_python//python:python.bzl",
  "py_binary", "py_library", "py_test",
)
load("@python_deps//:requirements.bzl", "requirement")


py_binary(
    name = "my_api",
    srcs = glob(["*.py"]),
    deps = [
	requirement("Flask"),
    ],
    main = "__main__.py",
)
