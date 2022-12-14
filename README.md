# Simple Plugin

## Description

This repo is to play with the plugin architecture which allows users to customize a program by adhering to a predefined interface.

## Structure

There are two components to a plugin:
1. Core System
2. Plugin

### 1. Core System

The "core system", or standalone program, is called my_app in this case and the user would likely not see. In this case the app simply prints something to the console (defined in main.py). In general, there would be code that in the application folder that details the core system, but in this case, the files in that directory are for loading a plugin. Bottom line, the code for the core system is entirely contained in main.py.


### 2. Plugin

The plugin is where the user can add their customizability. In this case, the customizability is simply allowing for additional printing to the console through defining a new function (which doesn't return anything and takes no parameters). This is an oversimplified example but another repo will be attached to show a more in depth example.

## Usage

To run this program simply move to the root directory for this folder and then execute:

```
python main.py
```

## Extending

As this is a plugin, here is how to add to the existing program:

1. Add a new py file inside the plugins directory
2. define a function which simply prints something (no parameters, no return)
3. register that function:
    1. import factory from my_app
    2. define a function called register which calls factory.register (two params: a string for your function name, and then your function)
4. execute the core system (main.py)

There is a sample plugin provided that you can follow called additional_call1.py.
If this does not work let me know!

