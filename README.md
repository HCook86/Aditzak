# Aditzak

A library to analyze and build verbs in Euskera

## Installation

Using pip:

    pip install Aditzak

## Usage

Basic example:

    
    from Aditzak import build, analyze

    build({"Aditza":None, "Kasua":"NOR-NORK", "Modua":"Ondorioa","Denbora":"Iragana", "Nor":"ni", "Nori":None, "Nork":"hark"})
    
    analyze("dizkidate")
