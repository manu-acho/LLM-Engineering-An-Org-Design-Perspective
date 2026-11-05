"""Inspect and test one deliberately restricted model-written routing function.

This is not a general Python sandbox. It accepts only a tiny expression subset
with no calls, imports, attribute access, loops or mutation.
"""

import ast

SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {"code": {"type": "string"}},
    "required": ["code"],
}
SPEC = """Write exactly one Python function route_case(case). Inputs have category, ordered, reported.
If reported is None, return needs_evidence. Otherwise invoice returns finance, damage returns review,
and a quantity mismatch returns investigate. All other cases return review.
Use only def, if, return, comparisons, boolean operators and dictionary subscripts.
No imports, calls, attributes, assignments, annotations, loops, global names or markdown fences."""


def inspect_code(code):
    if not isinstance(code, str) or len(code) > 4000:
        raise ValueError("Short source text required")
    tree = ast.parse(code)
    if len(tree.body) != 1 or not isinstance(tree.body[0], ast.FunctionDef):
        raise ValueError("Exactly one function required")
    function = tree.body[0]
    if (
        function.name != "route_case"
        or function.decorator_list
        or function.returns
        or function.type_comment
    ):
        raise ValueError("Unexpected function configuration")
    args = function.args
    if (
        len(args.args) != 1
        or args.args[0].arg != "case"
        or args.args[0].annotation
        or args.defaults
        or args.kw_defaults
        or args.kwonlyargs
        or args.posonlyargs
        or args.vararg
        or args.kwarg
    ):
        raise ValueError("Use one unannotated case parameter")
    allowed = (
        ast.Module,
        ast.FunctionDef,
        ast.arguments,
        ast.arg,
        ast.If,
        ast.Return,
        ast.Compare,
        ast.Eq,
        ast.NotEq,
        ast.Is,
        ast.IsNot,
        ast.BoolOp,
        ast.And,
        ast.Or,
        ast.Name,
        ast.Load,
        ast.Constant,
        ast.Subscript,
        ast.Expr,
    )
    nodes = list(ast.walk(tree))
    if len(nodes) > 160:
        raise ValueError("Function exceeds the teaching complexity limit")
    for node in nodes:
        if not isinstance(node, allowed):
            raise ValueError(f"Operation outside the exercise subset: {type(node).__name__}")
        if isinstance(node, ast.Name) and node.id != "case":
            raise ValueError("Unexpected name")
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and len(node.value) > 160:
            raise ValueError("Oversized constant")
    return tree


def compile_routing(code):
    tree = inspect_code(code)
    namespace = {}
    exec(compile(tree, "<reviewed-course-routing>", "exec"), {"__builtins__": {}}, namespace)
    return namespace["route_case"]


def acceptance(function):
    cases = [
        ({"category": "quantity", "ordered": 12, "reported": 10}, "investigate"),
        ({"category": "invoice", "ordered": 8, "reported": 8}, "finance"),
        ({"category": "damage", "ordered": 8, "reported": 8}, "review"),
        ({"category": "quantity", "ordered": 8, "reported": None}, "needs_evidence"),
    ]
    return [
        {
            "input": case,
            "expected": expected,
            "actual": function(dict(case)),
            "passed": function(dict(case)) == expected,
        }
        for case, expected in cases
    ]


def propose(gateway):
    result = gateway.generate(
        SPEC,
        instructions="Return the small function requested. Do not include a solution outside the stated subset.",
        schema=SCHEMA,
    )
    code = result.value["code"]
    function = compile_routing(code)
    return {
        "code": code,
        "checks": acceptance(function),
        "boundary": "Reviewed restricted function only; no repository edits or arbitrary generated-code execution",
    }
