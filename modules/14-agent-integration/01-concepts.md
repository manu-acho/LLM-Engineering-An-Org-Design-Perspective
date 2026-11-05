# Lesson 14.1: MCP connects capabilities, not business authority

[Download the matching notebook](/downloads/14-01-concepts.ipynb) · [Notebook setup](../../STUDY-WORKSPACE.md)

[Module route](README.md) · [Next lesson](02-code-workshop.md)

## Connecting an assistant to existing systems

Harbour's assistant needs order records, policy information and a place to prepare handoffs. Without a common interface, each agent framework may need custom code for every system. MCP, the **Model Context Protocol**, supplies a way for applications and capability servers to exchange defined requests and responses.

The organisational opportunity is reuse: a maintained interface can serve several applications. The responsibility is also reusable. Someone must own what each operation means, who may invoke it and how its results should be interpreted.

## Host, client and server

An MCP **host** is the AI application managing the interaction. A **client** handles communication with a particular server. A **server** exposes capabilities such as tools or resources. The model may propose using a capability, but the surrounding runtime and service perform the actual operation.

The [architecture overview](https://modelcontextprotocol.io/docs/learn/architecture) explains these roles. The course shows concrete SDK connections rather than requiring us to implement protocol messages by hand. When diagnosing a failure, distinguish the model's choice, the client's request, the server's operation and the underlying business system's response.

## Tools, resources and prompts

A **tool** is an operation that can be called with arguments. A balance lookup reads information; a transaction tool changes a record. Both can be exposed as tools, so “tool access” is not synonymous with harmless reading.

A **resource** exposes context identified by an address, such as a report for a particular account. A **prompt** can supply a reusable interaction template. Availability and selection rules vary by capability and application. None of these surfaces should be treated as a source of higher-priority instructions simply because it arrived through a protocol connection.

The course's accounts server exposes tools and account/strategy resources. This lets us compare looking up data, changing it and supplying background context through different interfaces.

## Discovery is not authorisation

**Discovery** tells a client which capabilities a server advertises. A **tool filter** can limit which are presented to an agent. That helps keep its available choices relevant. It does not replace the server's checks on the identity and scope of an actual caller.

If a caller can reach an operation by another path, hiding its name in a list does not enforce permission. For a business system, check authorisation at the boundary where the operation executes, using trusted identity and relevant record scope.

The [MCP HTTP authorisation specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) describes transport-level access. It does not decide Harbour's credit policy or prove that an authenticated service has authority for every record. The local exchange uses the SDK versions recorded in uv.lock; do not assume later protocol or SDK versions are interchangeable.

## Local processes and network services

With **stdio**, a client starts or connects to a local process and exchanges messages through standard input and output. That process inherits only the environment and permissions made available to it. The course also shows a streamable HTTP connection to a remote server.

With a remote service, the network, credentials, server availability and service ownership become explicit dependencies. “Local tool” does not automatically mean safe or authorised: a local process can still read files or send network requests if its implementation and permissions allow them.

An `async with` block in the source helps manage server lifetimes. A wider collection of servers may use an asynchronous exit stack so opened resources are cleaned up together. These are runtime responsibilities, distinct from whether an operation's business meaning is appropriate.

## Context engineering is a selection problem

**Context engineering** means arranging the instructions, records, tool descriptions and state available for a model's next step. The course combines account reports, strategy resources, research tools and memory. This gives the model more useful material, but also creates choices about what is current, authoritative and relevant.

More context is not a cure for incompatible sources. Preserve source identity, version and status. Treat retrieved text as evidence to assess, not as permission to change the task or reveal unrelated records. A stored memory may contain a previous interpretation rather than a verified fact.

## Observe the effect, not only the request

A tool-call trace can show that a request was made. A service receipt can show what the server acknowledged. Business evidence is needed to establish what changed and whether the intended recipient could use it. Add stable request and action identities where repeated calls could duplicate effects.

The course's trading-floor project uses account records and market information to make these interactions visible. It is a software example, not evidence of profitable trading or a production financial-control design. Our application returns to Harbour's service workflow.

**Check:** An agent can discover a tool called `change_assignment`. Which additional facts would establish that it may use it for this request? Include caller identity, case scope, approved purpose, current state, input validity and a trustworthy completion record.

## Continue the module

The [complete module route](README.md) continues into the technical mechanism, [source walkthrough](05-source-walkthrough.md) and [completed organisational design case](06-design-lab.md). Use those lessons to carry this introduction into a fuller implementation and business decision.

## Read the organisational connection

Discovering an available capability does not establish a mandate for its business use. The research chapter explains [permission and authority](../../reference/research/03-decisions.md#permission-and-authority).
