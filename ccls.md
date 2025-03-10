% ccls(1) | ccls LSP server

NAME
====

ccls - C, C++ and Objective-C language server

SYNOPSYS
========

ccls [options]

Emacs or Neovim.

DESCRIPTION
===========

ccls is a Language Server conforming to the LSP protocol.

It indexes C, C++ and Objective-C projects and provides code completion,
definition, references, cross references, formatting, call hierarchies,
inheritance hierarchies, member hierarchies, symbol renaming, document symbols,
hover information, code diagnostics, code actions, semantic highlighting,
preprocessor skipped regions and semantic navigation to source code editors,
such as Emacs, Vim, Neovim, Sublime, Monaco, Atom or Visual Studio Code.

OPTIONS
=======

`-h, --help`

: Display available options.

`--help-hidden`

: Display more options that are hidden by default.

`--version`

: Show the version of the program

`--index=<root>`

: standalone mode: index a project and exit

`--init=string`

: extra initialization options in JSON format

`--log-file=<file>`

: sends stderr messages to the given file

`--log-file-append`

: appends to log file.

`--test-index[=<string]`

: run index tests

`-v <int>`

: verbosity, from -3 (fatal) to 2 (verbose)

BUGS
====

To report bugs please visit https://github.com/MaskRay/ccls/issues

SEE ALSO
========

* ccls at GitHub https://github.com/MaskRay/ccls
* The ccls wiki https://github.com/MaskRay/ccls/wiki
* The ccls FAQ https://github.com/MaskRay/ccls/wiki/FAQ
* ccls customization https://github.com/MaskRay/ccls/wiki/Customization

COPYRIGHT
=========

(C) 2017-2018 the ccls Authors

