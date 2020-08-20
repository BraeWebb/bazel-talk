load("@bazel_latex//packages:packages.bzl", "latex_package")
load("@bazel_latex//:latex.bzl", "latex_document")

latex_package(
    name = "textpos",
    srcs = [
        "@texlive_texmf__texmf-dist__tex__latex__textpos",
    ]
)

latex_document(
    name = "slides",
    srcs = [
        "slides/uqcs.sty",
        ":textpos",
        "//fonts",
        "//images",
        "@bazel_latex//packages:beamer",
        "@bazel_latex//packages:multicol",
        "@bazel_latex//packages:fontspec",
    ],
    main = "slides/main.tex",
)
