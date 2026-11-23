#!/usr/bin/env python3
# Re-run the converters of the merged slices on the pre-image of each merged PR and compare with what was merged.
import subprocess, importlib.util, sys
spec=importlib.util.spec_from_file_location("sb","scripts/stat-blocks-166.py"); sb=importlib.util.module_from_spec(spec); spec.loader.exec_module(sb)
def git(*a): return subprocess.check_output(["git",*a],text=True)
merges=git("log","--first-parent","--merges","--format=%H %s","origin/main").splitlines()
want={"variant-siege":"siege","variant-shield":"shield","variant-recipe":"recipe","variant-tearaway":"tearaway","variant-intelligent":"intelligent","variant-ioun":"ioun","variant-spellbook":"spellbook","variant-figurine":"figurine","variant-cost":"cost","variant-trap":"trap","tech-construction":"techcons"}
total=0; diffs=0
for line in merges:
    sha,subject=line.split(" ",1)
    name=next((v for k,v in want.items() if k in subject),None)
    if not name: continue
    files=[f for f in git("diff","--name-only",sha+"^1",sha).splitlines() if f.startswith("entries/")]
    for f in files:
        pre=git("show",f"{sha}^1:{f}"); post=git("show",f"{sha}:{f}")
        status,detail,new=sb.plan_file(pre,name)
        total+=1
        if status!="converted" or new!=post:
            diffs+=1; print("DIFF",name,f,status,detail)
    print(name,len(files),"files replayed")
print("replayed",total,"files; differences:",diffs)
