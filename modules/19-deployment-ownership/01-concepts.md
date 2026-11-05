# Lesson 19.1: Deployment and continuing service ownership

[Download the matching notebook](/downloads/19-01-concepts.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Study workspace](../../STUDY-WORKSPACE.md)

## A running endpoint is the beginning of operation

An HTTP service receives requests through defined routes and returns responses with status codes and structured bodies. FastAPI supplies routing and input validation; Uvicorn runs the application server. The local service exposes health, scoped case reads and simulated review decisions. The generated API documentation provides a small interface for inspecting the contract without requiring a separate dashboard.

A request crosses several boundaries: network transport, identity resolution, input validation, business permission, state transition and response delivery. A successful response means the exercised path completed according to its implementation. It does not mean that the evidence was correct or the wider customer problem was resolved.

## Configuration belongs outside the source code

The service entry point loads COURSE_SERVICE_TOKEN from the local .env file and maps it to a fixed fictional manager principal. This is a local teaching arrangement. Generate a long random token locally, keep it out of notebooks and use it only for this application. The test suite uses clearly labelled dummy tokens and never reads a real credential.

A production service normally needs a managed identity and secret lifecycle, including revocation, rotation and auditable access. Environment variables are a delivery mechanism, not a complete secret-management programme. A token should not be logged simply because a request failed.

## Persistence changes the deployment choice

The local application stores its SQLite database under outputs. Restarting on the same machine with that directory preserves state. An ephemeral container filesystem may disappear on replacement. Several independently scaled instances cannot assume they share the same local file. A deployment must therefore choose appropriate persistent storage and define concurrency, backup and restore behaviour.

A **migration** changes a database schema or data representation between software versions. A code rollback may not reverse a migration safely. Before a release, specify which versions can read the stored data and what recovery is possible after writes under the new schema. The teaching store creates its initial schema; it does not claim to implement production migrations.

## Decide what the host should do

A managed container host keeps a process running behind a network boundary. A serverless request handler changes process lifetime, startup and timeout assumptions. A managed agent runtime may add execution and identity services. Evaluate these against the actual workload rather than assuming a named platform is automatically a better design.

The course reading website is static and can be hosted on Netlify. That website supplies notes and downloads. It does not run the Python backend or keep case state. Deploying the reading site and deploying the teaching application are separate operations with different operating responsibilities.

## Release and recover deliberately

A release should identify the code version, dependency lock, model and instruction versions, database compatibility, test results and configuration requirements. Readiness checks should exercise necessary dependencies without exposing secrets. Liveness answers whether the process is responding; readiness answers whether it should receive work. A health endpoint returning ok is only as meaningful as its checks.

Use a small initial population and retain a route back to a known working configuration. A rollback can prevent new bad decisions while leaving earlier consequences to reconcile. Record which version handled each case so an incident can be scoped. Local HTTP tests and startup checks are provided here; cloud deployment, load capacity, backup restoration and real identity-provider integration require separate execution evidence.
