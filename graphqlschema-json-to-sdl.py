import json
from graphql import build_client_schema, print_schema

# Load the JSON schema from a file
with open('replace_with_pathway_to/schema.json', 'r') as file:
    schema_json = json.load(file)

# Extract the 'data' key
introspection_query_result = schema_json['data']

# Convert to GraphQLSchema
client_schema = build_client_schema(introspection_query_result)

# Convert to SDL
sdl = print_schema(client_schema)

# Save the SDL to a file
with open('replace_with_output_pathway_desired/schema.graphql', 'w') as sdl_file:
    sdl_file.write(sdl)
