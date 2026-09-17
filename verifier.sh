#!/usr/bin/env bash
set -e
echo $(date) >> preuve-garde-fou.txt
echo "======================================================" >> preuve-garde-fou.txt
echo "================================================== RUFF TEST ==================================================" >> preuve-garde-fou.txt
ruff format --check . >> preuve-garde-fou.txt
ruff check .  >> preuve-garde-fou.txt
echo "================================================== RANDON TEST =================================================="
radon cc -s -a --total-average . >> preuve-garde-fou.txt
echo "================================================== XENON TEST ==================================================" >> preuve-garde-fou.txt
xenon --max-absolute B --max-modules A --max-average A . >> preuve-garde-fou.txt
echo "================================================== VULTURE TEST ==================================================" >> preuve-garde-fou.txt
vulture . --min-confidence 80 >> preuve-garde-fou.txt
echo "================================================== PYTEST TEST ==================================================" >> preuve-garde-fou.txt
pytest --cov=. --cov-branch --cov-report=term-missing >> preuve-garde-fou.txt
echo "================================================== FIN ==================================================" >> preuve-garde-fou.txt
