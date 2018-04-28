workspace(name = "test_playground")

git_repository(
    name = "io_bazel_rules_python",
    remote = "https://github.com/bazelbuild/rules_python.git",
    commit = "8b5d0683a7d878b28fffe464779c8a53659fc645",
)

load("@io_bazel_rules_python//python:pip.bzl", "pip_repositories", "pip_import")
pip_repositories()
pip_import(
   name = "python_deps",
   requirements = "//third_party/python:requirements.txt",
)

load("@python_deps//:requirements.bzl", "pip_install")
pip_install()

http_archive(
    name = "io_bazel_rules_rust",
    sha256 = "615639cfd5459fec4b8a5751112be808ab25ba647c4c1953d29bb554ef865da7",
    strip_prefix = "rules_rust-0.0.6",
    urls = [
        "http://bazel-mirror.storage.googleapis.com/github.com/bazelbuild/rules_rust/archive/0.0.6.tar.gz",
        "https://github.com/bazelbuild/rules_rust/archive/0.0.6.tar.gz",
    ],
)
load("@io_bazel_rules_rust//rust:repositories.bzl", "rust_repositories")
rust_repositories()
