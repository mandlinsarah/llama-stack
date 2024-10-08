# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import argparse

from .distribution import DistributionParser
from .download import Download
from .model import ModelParser


class LlamaCLIParser:
    """Defines CLI parser for Llama CLI"""

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="llama",
            description="Welcome to the Llama CLI",
            add_help=True,
        )

        # Default command is to print help
        self.parser.set_defaults(func=lambda args: self.parser.print_help())

        subparsers = self.parser.add_subparsers(title="subcommands")

        # Add sub-commands
        Download.create(subparsers)
        ModelParser.create(subparsers)
        DistributionParser.create(subparsers)

        # Import sub-commands from agentic_system if they exist
        try:
            from llama_agentic_system.cli.subcommand_modules import SUBCOMMAND_MODULES

            for module in SUBCOMMAND_MODULES:
                module.create(subparsers)

        except ImportError:
            pass

    def parse_args(self) -> argparse.Namespace:
        return self.parser.parse_args()

    def run(self, args: argparse.Namespace) -> None:
        args.func(args)


def main():
    parser = LlamaCLIParser()
    args = parser.parse_args()
    parser.run(args)


if __name__ == "__main__":
    main()
