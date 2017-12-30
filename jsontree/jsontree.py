"""JSON tree output plugin
"""

from __future__ import print_function

import optparse
import logging

import json

from pyang import plugin
from pyang import statements
from pyang import types
from pyang import error

def pyang_plugin_init():
    plugin.register_plugin(JSONTreePlugin())

class JSONTreePlugin(plugin.PyangPlugin):
    def add_output_format(self, fmts):
        fmts['jsontree'] = self

    def add_opts(self, optparser):
        optlist = [
            optparse.make_option('--jsontree-debug',
                                 dest='tree_debug',
                                 action="store_true",
                                 help='JSON Tree debug')
            ]

            # TODO: specify children label and name label

        group = optparser.add_option_group("JSON Tree-specific options")
        group.add_options(optlist)

    def setup_ctx(self, ctx):
        ctx.opts.stmts = None

    def setup_fmt(self, ctx):
        ctx.implicit_errors = False

    def emit(self, ctx, modules, fd):
        if ctx.opts.tree_debug:
            logging.basicConfig(level=logging.DEBUG)

        tree = produce_tree(modules[0])
        fd.write(json.dumps(tree, indent=2))

meta_stmt_keywords = ['organization', 'contact', 'description', 'reference']

def produce_tree(root_stmt):
    logging.debug("in produce_tree: %s %s", root_stmt.keyword, root_stmt.arg)
    result = { 'type': root_stmt.keyword, 'name': root_stmt.arg, 'children': [] }
    for meta in meta_stmt_keywords:
        found = root_stmt.search_one(meta)
        if found:
            result.update({meta: found.arg})

    for ss in root_stmt.substmts:
        logging.debug("Top: %s %s", ss.keyword, ss.arg)
        add = produce_data_def(ss)
        if add:
            result['children'].append(add)
        logging.debug("result is now: %s", json.dumps(result, indent=2))

    return result

def produce_data_def(stmt):
    logging.debug("in produce_data_def: %s %s", stmt.keyword, stmt.arg)
    result = {}
    if stmt.keyword in statements.data_definition_keywords:
        result = {'type': stmt.keyword, 'name': stmt.arg, 'children': []}
        for meta in meta_stmt_keywords:
            found = stmt.search_one(meta)
            if found:
                result.update({meta: found.arg})
        for ss in stmt.substmts:
            res = produce_data_def(ss)
            if res:
                result['children'].append(res)

    return result