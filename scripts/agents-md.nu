#!/usr/bin/env nu
# SessionStart hook: give Claude Code the AGENTS.md files of the working directory and its
# parents, nearest last — the way it would read CLAUDE.md. The repositories keep ONLY AGENTS.md
# (the owner, 2026-10-27); the binary looks for CLAUDE.md, so this is the mechanism.
# ~/cyber/AGENTS.md itself arrives through ~/.claude/CLAUDE.md (one @import line), because a
# hook's context is cut to a preview above ~10,000 chars (measured 2026-10-27: 9,000 arrives,
# 12,000 does not); the repo files travel here in full when they fit, else as a read order.
const HOME_DOCTRINE = "/Users/master/cyber/AGENTS.md"
const LIMIT = 9000
def main [] {
    let input = (try { ^cat | from json } catch { {} })
    let cwd = ($input.cwd? | default $env.PWD | path expand)
    mut dirs = []
    mut d = $cwd
    loop {
        $dirs = ($dirs | prepend $d)
        let parent = ($d | path dirname)
        if $parent == $d { break }
        $d = $parent
    }
    let found = ($dirs | each {|dir|
        let f = ($dir | path join "AGENTS.md")
        if ($f | path exists) and $f != $HOME_DOCTRINE { $f } else { null }
    } | compact)
    if ($found | is-empty) { return }
    let texts = ($found | each {|f| {path: $f, text: (open --raw $f)} })
    let total = ($texts | each {|t| $t.text | str length } | math sum)
    let ctx = if $total <= $LIMIT {
        let body = ($texts | each {|t| $"# instructions from ($t.path)\n\n($t.text)" } | str join "\n\n---\n\n")
        $"Project instructions \(AGENTS.md of this repository, loaded at session start in place of CLAUDE.md; they apply together with ~/cyber/AGENTS.md\):\n\n($body)"
    } else {
        let list = ($texts | each {|t| $"- ($t.path) \(($t.text | str length) chars\)" } | str join "\n")
        $"Project instructions: this repository's AGENTS.md is too long to inline \(($total) chars\). Before any other action, Read these files in this order and obey them as you would CLAUDE.md:\n($list)"
    }
    {hookSpecificOutput: {hookEventName: "SessionStart", additionalContext: $ctx}} | to json --raw
}
