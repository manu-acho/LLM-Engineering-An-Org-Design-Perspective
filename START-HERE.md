# Start here: a standalone learning route

[Course home](README.md) · [Module 1](modules/01-standalone-foundations/README.md)

## Begin with the business question

A customer reports a shortage. A program can assemble the available records; a model can generate words; someone still needs to determine what happened and what action is justified. Module 1 opens these contributions one at a time.

The completed pilot can be studied without Ed Donner's courses, notebooks or datasets. Its examples are original, use fictional data and make no network calls. The rest of the curriculum is clearly marked as planned.

## Choose a route

For concepts and business design, read Lessons 1.1, 1.3, 1.5, 1.6 and 1.7. The examples and worked answers provide the necessary context even without running code. Read Lesson 1.2 to become familiar with what a program is doing, and Lesson 1.4 when examining implementation decisions.

For implementation, follow all seven lessons in order. Predict an output, run the example, compare the result and change one input. The aim is to understand the pattern and its limits, not simply produce a successful run.

## Files, folders and the terminal

A **file** contains saved text or code. A **folder** groups files. The **terminal** accepts commands that start programs and reports their output. A **working directory** is the folder from which a command runs. `cd` changes that directory. Paths identify files or folders.

A **Python interpreter** reads and executes Python code. A `.py` file is a text file containing that code. The pilot is written for Python 3.10 or later and is checked on the interpreter version recorded in the lab guide. It needs no additional packages. Python can be obtained from the [official Python site](https://www.python.org/downloads/).

On macOS or Linux, check the interpreter with:

```sh
python3 --version
```

On Windows, the Python launcher commonly uses:

```powershell
py -3 --version
```

If the command is not found, install Python and reopen the terminal. Running the command reports which interpreter is available; it does not install it. The code is intended to be portable, but this pilot's recorded execution check is on macOS, not a claim of a Windows runtime test.

## Get the two lab files

Download [foundations_lab.py](/downloads/foundations_lab.py) and [test_foundations.py](/downloads/test_foundations.py) into one folder. Keep the exact filenames, including `.py`. The examples include their own small training sentences and fictional case, so no separate data download is required.

Open a terminal in that folder. On macOS or Linux:

```sh
python3 foundations_lab.py model
python3 foundations_lab.py brief
python3 foundations_lab.py request
python3 -m unittest -v test_foundations.py
```

On Windows, replace `python3` with `py -3`. The first three commands print JSON, structured text whose named fields preserve the distinction between quantities, sources and unresolved questions. The last command runs the checks. Detailed outputs and troubleshooting are in [the lab guide](LAB-GUIDE.md).

## What runs, and what does not

The `model` example trains and runs a tiny statistical language model. It is a real count-based model, not a modern neural LLM. The `brief` example is ordinary deterministic code. The `request` example constructs messages but sends nothing to a model provider. It needs no key and cannot incur inference charges.

The distinction matters: correct evidence preparation is not proof of model behaviour, and a fluent continuation is not verification of a business record. The lessons explain both mechanisms before connecting them.
