java_library(
    name = "node_lib",
    srcs = [
        "Node.java"
    ],
)

java_binary(
    name = "tree_serializer",
    srcs = glob([
        "*.java",
    ]),
    deps = [":node_lib"],
    main_class = "SerializeTree"
)
