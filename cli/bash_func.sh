hgp() {
  history | grep "$1" | tail -n "${2:-5}"
}
