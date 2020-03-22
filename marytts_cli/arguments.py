#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Argument parsing of the MaryTTS command-line client

This module contains the setup function for the argument parser of the
command-line client.
"""

import argparse

def setup_argparser():
    """Setup argument parser"""
    # The max_help_position parameter isn't part of the official public API of
    # argparse and could disappear in future versions of it. It is used here to
    # suppress unwanted line breaks when help information is printed until a
    # better solution is found.
    formatter = lambda prog: argparse.HelpFormatter(prog, max_help_position=33)
    parser = argparse.ArgumentParser(
        prog='marytts-cli',
        description=str(
            'A command-line client for the HTTP server '
            'of the MaryTTS Text-To-Speech System.',
        ),
        formatter_class=formatter,
    )
    parser.add_argument(
        '-a',
        '--audio',
        type=str,
        metavar='AUDIO',
        help='set format of MaryTTS audio output',
    )
    parser.add_argument(
        '-i',
        '--input',
        type=str,
        metavar='TYPE',
        help='set type of MaryTTS input',
    )
    parser.add_argument(
        '-l',
        '--locale',
        type=str,
        metavar='LOCALE',
        help='set identifier of Locale',
    )
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        metavar='TYPE',
        help='set type of MaryTTS output',
    )
    parser.add_argument(
        '-t',
        '--timeout',
        type=str,
        metavar='SECONDS',
        help='set request timeout',
    )
    parser.add_argument(
        '-u',
        '--url',
        type=str,
        metavar='URL',
        help='set request URL',
    )
    parser.add_argument(
        '-v',
        '--voice',
        type=str,
        metavar='VOICE',
        help='set name of MaryTTS voice',
    )
    return parser
