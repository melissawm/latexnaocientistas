import os
import sys

def write_texfile(dados):
    
    # Escrever o resultado em um arquivo .tex
    results = open('chart.tex','w')
    print >>results, '\\documentclass{article}'
    print >>results, '\\usepackage{calc}'
    print >>results, '\\usepackage{ifthen}'
    print >>results, '\\usepackage{tikz}'
    print >>results, '\\usepackage{txfonts}'
    print >>results, '\\begin{document}'
    print >>results, '\\newcommand{\\slice}[5]{\\pgfmathparse{0.5*#1+0.5*#2}\\let\\midangle\\pgfmathresult '
    print >>results, '% slice'
    print >>results, '\\draw[thick,fill=blue!#5!white] (0,0) -- (#1:1) arc (#1:#2:1) -- cycle;'
    print >>results, '% outer label'
    print >>results, '\\node[label=\\midangle:#4] at (\\midangle:1) {};'
    print >>results, '% inner label'
    print >>results, '\\pgfmathparse{min((#2-#1-10)/110*(-0.3),0)} \\let\\temp\\pgfmathresult \\pgfmathparse{max(\\temp,-0.5) + 0.8} \\let\\innerpos\\pgfmathresult \\node[rectangle, fill=white] at (\\midangle:\\innerpos) {#3};}'
    print >>results, '\\begin{tikzpicture}[scale=3]'
    print >>results, '\\newcounter{a}'
    print >>results, '\\newcounter{b}'
    print >>results, '\\foreach \\p/\\t in {'
    frase = []
    for k,v in dados.iteritems():
        frase.append(str(v)+'/'+k)
    print >>results, ','.join(frase)
    print >>results, '} {'
    print >>results, '\\setcounter{a}{\\value{b}} \\addtocounter{b}{\\p} \\slice{\\thea/100*360} {\\theb/100*360} {\\p\\%}{\\t}{\\theb}'
    print >>results, '}'
    print >>results, '\\end{tikzpicture}'
    print >>results, '\\end{document}'
    results.close()
    # Compilar e mostrar o pdf resultante.
    try:
        os.system('pdflatex chart.tex')
    except OSError:
        print('LaTeX not installed.')
    os.system('xdg-open chart.pdf &')

if __name__ == '__main__':
    dados = {'Ubuntu':30, 'Debian':15, 'Fedora':6, 'Slackware':6, 'Gentoo':5, 'OpenSUSE': 7, 'Chakra':5, 'Outras': 26}
    write_texfile(dados)
