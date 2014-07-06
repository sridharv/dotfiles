#!/usr/bin/python

import os
import subprocess
from urlparse import urlparse
import sys

modules = [
    'git://github.com/tpope/vim-fugitive.git',
    'git://github.com/tpope/vim-sensible.git',
    'git://github.com/tpope/vim-markdown.git',
    'git://github.com/aklt/plantuml-syntax.git',
    'git://github.com/ervandew/supertab.git',
    'git://github.com/godlygeek/tabular.git',
    'git://github.com/SirVer/ultisnips.git',
    'git://github.com/honza/vim-snippets.git',
    'git://github.com/pangloss/vim-javascript.git',
    'git://github.com/tpope/vim-git.git',
    'git://github.com/tpope/vim-surround.git',
    'git://github.com/tpope/vim-repeat.git',
    'git://github.com/vim-scripts/matchit.zip.git',
    'git://github.com/vim-scripts/tComment.git',
    'git://github.com/kien/ctrlp.vim.git',
    'git://github.com/kien/rainbow_parentheses.vim.git',
    'git://github.com/chilicuil/conque.git',
    'git://github.com/Lokaltog/vim-easymotion.git',
    'git://github.com/sjl/gundo.vim.git',
    'git://github.com/nathanaelkane/vim-indent-guides.git',
    'git://github.com/bling/vim-airline.git',
    'git://github.com/Townk/vim-autoclose.git',
    'git://github.com/altercation/vim-colors-solarized.git',
    'git://github.com/fatih/vim-go.git',
    'git://github.com/sridharv/vim-overrides.git',
    'git://github.com/avakhov/vim-yaml.git',
    'git://github.com/ingydotnet/yaml-vim.git',
    'git://github.com/tpope/vim-fireplace.git',
    'git://github.com/tpope/vim-classpath.git',
    'git://github.com/guns/vim-clojure-static.git',
    'git://github.com/vim-scripts/paredit.vim',
]

def module_parse(module):
    name, ext = os.path.splitext(os.path.basename(module))
    target_dir = os.path.join('.vim/bundle', name)
    if os.path.isdir(target_dir):
        subprocess.check_output(['git', 'shortlog', '-1', target_dir])
        exists = True
    else:
        exists = False

    command = 'add'
    if exists:
        command = 'pull'
    subtree = ['git', 'subtree', command, '--prefix', target_dir, module,
               'master', '--squash']
    return name, subtree, doc_url(module)

doc_file_template = """
<!DOCTYPE html>
<html class="no-js">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>Vim Plugins</title>

        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap-theme.min.css">
        <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
    </head>
    <body>
        <div class="jumbotron">
            <div class="container">
                <h3>Vim Plugins</h3>
            </div>
        </div>
        <div class="container">
            <ul class="nav nav-tabs nav-stacked">
                %s
            </ul>
        </div>

    </body>
</html>
"""

def doc_url(module):
    return module.replace('git://', 'https://')

def main():
    doc_file = os.path.join(os.path.dirname(sys.argv[0]), 'plugins.html')
    plugin_urls = []
    for module in modules:
        name, command, url = module_parse(module)
        plugin_urls.append('<li><a href="%s">%s</a></li>' % (url, name))
        print 'Processing', module, 'with', ' '.join(command)
        print subprocess.check_output(command)
        print

    f = open(doc_file, 'w')
    f.write(doc_file_template % '                \n'.join(plugin_urls))
    f.close()

main()
