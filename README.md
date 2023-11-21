# GraphQL JSON to SDL Converter

This Python script converts a GraphQL JSON schema to Schema Definition Language (SDL). It's designed to help developers who need to generate SDL from GraphQL introspection results for use with e.g. Apollo GraphQL!

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
