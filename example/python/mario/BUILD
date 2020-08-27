py_library(
    name = "util",
    srcs = [
        "util.py",
    ],
)

py_binary(
    name = "mario",
    srcs = [
        "mario.py"
    ],
    deps = [
        ":util"
    ],
    data = [
        "level.txt",
    ],
)

py_test(
    name = "test_mario",
    srcs = [
        "test_mario.py"
    ],
    deps = [
        ":mario",
    ],
)