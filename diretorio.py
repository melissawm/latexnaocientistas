# -*- coding: utf-8 -*-
#import subprocess
import os
import sys

def write_texfile(dirname):
    # Criar a listagem do diretorio
    os.system('ls '+dirname+' > '+os.path.join(dirname,'ls.output'))
    # Ler o arquivo gerado pelo ls
    output = open(os.path.join(dirname,'ls.output'),'r')
    # Escrever o resultado em uma tabela em um arquivo .tex
    results = open(os.path.join(dirname,'ls.tex'),'w')
    print >>results, '%& -output-directory=',dirname
    # Codigo LaTeX
    print >>results, '\\documentclass{article}'
    print >>results, '\\usepackage[utf8]{inputenc}'
    print >>results, '\\usepackage{verbatim}'
    print >>results, '\\usepackage{longtable}'
    print >>results, '\\begin{document}'
    print >>results, '\\section*{Conteúdo do diretório ',dirname,'}'
    print >>results, '\\begin{center}'
    print >>results, '\\begin{longtable}{|l|}\\hline'
    print >>results, '\\hline Nome do arquivo \\\\ \\hline \\endfirsthead'
    for line in output:
        print >>results, '\\verb+',line[:-1],'+\\\\ '
    print >>results,'\\hline'
    print >>results,'\\end{longtable}'
    print >>results,'\\end{center}'
    print >>results,'\\end{document}'
    results.close()
    output.close()
    # Compilar e mostrar o pdf resultante.
    try:
        os.system('pdflatex '+os.path.join(dirname,'ls.tex'))
    except OSError:
        print('LaTeX not installed.')
    os.system('pdflatex '+os.path.join(dirname,'ls.tex'))
    os.system('mv ls.pdf '+os.path.join(dirname,'ls.pdf'))
    os.system('xdg-open '+os.path.join(dirname,'ls.pdf &'))

if __name__ == '__main__':
    dirname = sys.argv[1]
    write_texfile(dirname)
