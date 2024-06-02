A collection of functions, services, and protofiles to assist with gRPC systems.

## Project Setup/Initialization
### Virtual environment setup
For this project, it is assumed that you are running every terminal command within a [virtual environment](https://docs.python.org/3/library/venv.html) (*venv*).  You can set one up by running:
```bash
python -m venv .venv  # initialize virtual environment
source .venv/bin/activate  # activate virtual environment
```

When your *venv* is activated, your command prompt will be prefixed with `(.venv)`.

### Dependencies
With your *venv* running, run `pip install -r requirements.txt` to install dependencies inside of it.


# Hotel Search API
There is a gRPC server for serving mock or random responses on an **insecure** channel at `localhost:50051`.  The basic idea is that mock request/response examples can be added to a JSON file to faciliate development.

## Mock examples
The request/response pairs are located in the `resources/hotel_search_mocks.json`. The data is a single JSON object of a key (see `hotel_search.utils/mock_lookup_key()`) to request/response values.  If the user makes a gRPC request that corresponds to a key in the mock file, the server should return the associated mock response.

## Random responses
Alternatively, the user can make a random request to get a random instance of a HotelSearchResponse, courtesy of the randomproto library.

## Running the server
Activate your *venv* and run the server (within your venv) with the following: `python -m hotel_search.server`.
You also have an option to pass in a port number to override the default of `50051`. e.g. `python -m hotel_search.server 2020`

This will start a server on `localhost:50051` that you can hit from your client (note that ssl is disabled on the connection).

A few examples of client calls can be found in the associated section of the `grpc_clients.ipynb` notebook.

## Regenerating protoc compiled classes
- Activate your *venv*
- Install dev dependencies - `pip install -r dev_requirements.txt`
- Call the protoc compiler for your files:
```bash
$ python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. --pyi_out=. protos/hotel_search/v1/*.proto
$ python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. --pyi_out=. protos/google/type/*.proto
```