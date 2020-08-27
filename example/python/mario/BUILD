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