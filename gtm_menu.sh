#!/usr/bin/env zsh
# Maya HTT GTM Toolkit — Interactive CLI Menu
set -e
REPO_DIR="$(cd "$(dirname "${0}")" && pwd)"
cd "$REPO_DIR"

SCRIPTS=()
while IFS= read -r -d '' f; do
  SCRIPTS+=("$f")
done < <(find . -maxdepth 1 -name "*.py" ! -name "test_toolkit.py" -print0 | sort -z)

while true; do
  echo ""
  echo "=========================================="
  echo "   MAYA HTT GTM TOOLKIT — MAIN MENU"
  echo "=========================================="
  i=1
  for s in "${SCRIPTS[@]}"; do
    echo "  $i) $s"
    i=$((i+1))
  done
  echo "  q) Quit"
  echo ""
  read "choice?Select a script to run: "

  if [[ "$choice" == "q" ]]; then
    echo "Exiting."
    break
  fi

  if [[ "$choice" =~ '^[0-9]+$' ]] && (( choice >= 1 && choice <= ${#SCRIPTS[@]} )); then
    script="${SCRIPTS[$choice]}"
    echo ""
    echo "--- Running $script ---"
    python3 "$script"
    echo "--- Done ---"
  else
    echo "Invalid selection."
  fi
done
