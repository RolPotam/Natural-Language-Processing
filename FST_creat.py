import os
import sys

## G (Closure [G union I]) create
os.system('fstcompile --isymbols=lex.txt --osymbols=lex.txt infile G1.fst')
os.system('fstcompile --isymbols=lex.txt --osymbols=lex.txt latin I.fst')
os.system('fstunion G1.fst I.fst G2.fst')
os.system('fstclosure G2.fst Gcl.fst')
## A1 Create
os.system('fstcompile --acceptor --isymbols=lex.txt gr_accept.txt Gr.fsa')
os.system('fstdeterminize Gr.fsa Gr_det.fsa')
os.system('fstminimize Gr_det.fsa A1.fsa')
## A2 Create
os.system('fstcompile --acceptor --isymbols=lex.txt en_accept.txt En.fsa')
os.system('fstdeterminize En.fsa En_det.fsa')
os.system('fstminimize En_det.fsa A2.fsa')

#
os.system('fstunion A1.fsa A2.fsa At.fst')
os.system('fstarcsort --sort_type=olabel At.fst As.fst')
os.system('fstarcsort --sort_type=ilabel Gcl.fst Gs.fst')
os.system('fstcompose Gs.fst As.fst Ts.fst')
os.system('fstrmepsilon Ts.fst Ts.fst')
os.system('fstarcsort --sort_type=olabel Ts.fst T.fst')

