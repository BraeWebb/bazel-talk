# Bazel Talk
> Slides and other material used for a talk delivered to UQCS on the Bazel build system

## Slides
The slides can be built with Bazel using
```bash
bazel build //slides
```

This will build the latex slides and place them in the `bazel-bin` directory as `bazel-bin/slides/slides.pdf`.

## Script
Some vague instructions for me to follow for the live demos in the talk can be built as a PDF document using
```bash
bazel build //script
```
Stored in `bazel-bin/script/script.pdf`.

## ML Rule
The Standard ML rule has been added and a sample program can be run with
```bash
bazel run //example/ml:regex
```

It currently only works on linux and I have no intention of providing any additional support.
