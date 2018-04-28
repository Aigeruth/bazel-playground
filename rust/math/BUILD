package(default_visibility = ["//visibility:public"])

load("@io_bazel_rules_rust//rust:rust.bzl", "rust_library")

rust_library(
    name = "math",
    srcs = glob(["src/*.rs"]),
    crate_type = "dylib",
)

cc_library(
    name = "math_c_wrapper",
    srcs = [":math"],
)
