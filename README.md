# GraphQL JSON to SDL Converter

This Python script converts a GraphQL JSON schema to Schema Definition Language (SDL). It's designed to help developers who need to generate SDL from GraphQL introspection results for use with e.g. Apollo GraphQL!

Full GraphQL introspection Query attached in text file (NOTE: Often GraphQL endpoints expect Variables to be declared as an empty { } alongside the query - tested using POSTMAN): 

<img width="700" alt="Screenshot 2023-11-21 at 16 45 51" src="https://github.com/SMGLOBAL-ops/GraphQL-Schema-JSON-TO-SDL/assets/68763259/b55bb26d-7199-4aa5-9c22-84c8a7e98dba">



## Prerequisites

- Python 3
- `graphql-core` package

## Installation

Clone the repository

## Install the required package:

pip install graphql-core

## Usage

Place your GraphQL JSON schema file in the root directory of the project.
Modify the script so it points correctly to the `schema.json` file you want to convert to SDL, as well as where you want the output SDL file (.graphql) to go.

Run the script:

python3 graphqlschema-json-to-sdl.py
