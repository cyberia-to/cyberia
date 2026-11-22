---
tags: cyber, article
alias: project structure, repo layout, project conventions, repository structure, the standard repository, workspace
crystal-type: pattern
crystal-domain: cyber
---

# workspace — the standard repository

how a repository of cyberia is laid out, and what each group of its directories means for the product. the layout is read by people, by agents and by machines: the combine (apparatus `combine/`) decides from it how a change travels, and the [[release]] decides from it what a version carries. measured on 22 November 2026 over the 113 repositories of the home; the counts are in the last section.

## the layout

```
<repository>/
├── specs/            the contract: what the thing is, formats, invariants, acceptance
│   └── README.md     the index of the contract, with the status of every spec
├── rs/               the implementation in Rust — one directory per language
├── py/  js/  cw/     the implementation in another language, each under its language's name
├── cli/              the face on the command line: a thin binary over the implementation
├── tests/            checks that cross implementations; conformance vectors
├── examples/         programs a reader can run
├── docs/             the explanation: why and how, for a person who learns
│   └── explanation/  concepts; tutorials/ and guides/ beside it when they exist
├── roadmap/          the plan: one file per open question, with its status
├── audit/            the evidence: what was checked, when, at which revision, and what came of it
├── scripts/          the repository's own tools, in nushell or Python
├── .github/          the checks that run on a pull request
├── README.md         the door: what it is, how to build it, where to read on
├── AGENTS.md         the rules for every agent that works here
├── CHANGELOG.md      what each version carried, when the repository is in the release culture
├── LICENSE           the license
└── Cargo.toml        the manifest of the workspace
```

a repository carries the directories it needs. a directory it carries has the name and the meaning above.

## the six groups

every path of a repository belongs to one group. the group says what the path is for, how a change to it travels, and whether a release names it.

| group | the question it answers | directories and files | a change travels | in a release |
|---|---|---|---|---|
| contract | what must be true | `specs/`, `tests/` vectors, `conformance/`, `schema/` | by a pull request; a contract between repositories is the wide lane | yes |
| implementation | what runs | `rs/`, `py/`, `js/`, `cw/`, `src/`, `crates/`, `cli/`, `examples/`, `benches/`, a site's or an app's sources, manifests | by a pull request | yes |
| explanation | why and how | `docs/`, `README.md`, pages of a graph | by a pull request | yes |
| plan | what is meant next | `roadmap/`, `projects/`, `tasks/` | `roadmap/` by a pull request; `projects/` and `tasks/` directly, as the working state of a decision | `roadmap/` yes; the rest no |
| evidence | what was observed | `audit/` | directly: a receipt is written when the check is made | no |
| machinery | how the repository is built, checked and served | `scripts/`, `.github/`, `release/`, `deploy/`, `servers/`, `AGENTS.md` | by a pull request | yes |

working state has no group of its own in a product: a journal, collected series (`data/`), an agent's notes (`.claude/`) are written directly and no release names them. the rules a machine applies are `apparatus/combine/zones.toml`; this table is their meaning, and when the two disagree the table is corrected first and the rules follow.

the order of truth runs through the groups: the contract is written before the implementation; when code and a spec disagree the spec is settled first and the code follows; evidence is attached to the contract it checked; an explanation cites the contract and never restates it.

## implementations

one contract, many implementations. each language has its own directory at the root, named by the language: `rs/` for Rust, `py/` for Python, `js/` for JavaScript a browser runs, `cw/` for CosmWasm contracts. every implementation answers to the same `specs/` and passes the same vectors in `tests/`.

- `rs/` holds the library crate, with its own `Cargo.toml`; the root `Cargo.toml` is the workspace.
- `cli/` is a separate crate that depends on `rs/`: the command a person types. its name is the repository's name.
- `crates/` is for a repository that is a set of crates of equal rank — an application, a fork of a large project. each crate is named in the root manifest.
- `src/` at the root is Cargo's default for a repository that is one crate and will stay one. a repository that grows a second language or a command line moves to `rs/` and `cli/`.
- an application's faces follow the same rule one level down: `apps/`, `shell/`, `site/`, `landing/` are implementations, each of the product's own contract.

a new repository starts as `specs/`, `rs/`, `cli/`, `README.md`, `AGENTS.md`, `LICENSE`.

## the kinds of repository

| kind | what it is | what it carries beside the standard |
|---|---|---|
| component | a library of the stack with one contract | the full layout: `specs/ rs/ cli/ docs/ roadmap/ audit/` |
| product | an application or a site people open | faces as directories; `product/` or the product's page in the cyberia repository as its goal |
| graph | pages published as a site | pages at the root or in named sections; `subgraphs.toml`; pages are all it holds |
| operations | the machinery of the organisation | `servers/`, `processes/`, `combine/`, `release/`, `journal/` — named by what they operate |
| fork | another project's code under our name | the upstream layout is kept as it came; ours is added as `specs/`, `audit/`, `AGENTS.md` |

## the contract

`specs/` is the specification: complete, austere, ordered by the structure of the system. `specs/README.md` lists every spec with its status. a spec says what holds. a number that was measured goes to `audit/` with the command and the revision that produced it, and the spec links to it.

what was called `reference/` is `specs/`. ten repositories still carry the old name.

## the plan

`roadmap/` holds what is meant and not yet true: one file per open question, with a status in its frontmatter — `draft`, `accepted`, `rejected`, `implemented`, each meaning what [[documentation]] § design proposals says it means. an accepted proposal that is implemented moves its substance into `specs/` and keeps a line in the roadmap that says where it went. a rejected one stays, for its reasons. `proposals/` in a repository that has it is the same thing under an older name.

`projects/` and `tasks/` are the plan of the organisation and live in the cyberia repository and in apparatus: a project is a task with sub-tasks, a task is a unit of [[deliver]].

## the evidence

`audit/` holds audits, implementation status, benchmark results and release validation, in subdirectories by subsystem or by date. every report names its date, the revision it checked, the command that produced each number, and its limits. a report describes the check that was recorded: moving it revalidates nothing.

## the root

- `README.md` — the door. what the repository is in one paragraph, how to build and check it, links into `specs/` and `docs/`.
- `AGENTS.md` — the one instruction file for agents: the gates that must be green, the paths that need a discussion before they change, the sibling repositories it builds against. the file is named `AGENTS.md` in every repository.
- `CHANGELOG.md` — written by the release, one section per version, every change with the link to its pull request.
- `LICENSE` — the license, or a link to its canonical text.
- the manifest — `Cargo.toml` for the workspace; configuration of one target lives beside that target's code.

## across repositories

a repository names its siblings by relative path from the home, `../<repository>/rs`, and pins their revisions where a release needs them. a path in a page or a report is written with its repository: `tru/specs/rewards.md`. what one repository promises another is a contract and lives in the `specs/` of the one that promises.

## measured

over the 113 repositories of the home on 22 November 2026, by `git ls-tree` of each head; the command, the limits and the revision of every repository are in [[repository layout audit 2026-11-22]]:

| directory | repositories | | directory | repositories |
|---|---|---|---|---|
| `specs/` | 36 | | `rs/` | 21 |
| `audit/` | 30 | | `src/` | 21 |
| `docs/` | 29 | | `crates/` | 11 |
| `cli/` | 23 | | `roadmap/` | 19 |
| `scripts/` | 20 | | `tests/` | 14 |
| `.github/` | 37 | | `reference/` | 10 |

`README.md` stands in 103, `AGENTS.md` in 41, `CHANGELOG.md` in 13.

what does not yet fit the standard, each a unit of [[deliver]] and none of them changed by this page:

- `reference/` in ten repositories — apparatus, cyb, gaw, pearla, rs, tolya, trident, vitalina, xena, zenda — is the contract under its old name.
- `proposals/` in soft3 and foculus is `roadmap/` under its old name.
- soft3 holds its Rust in `crate/`; the standard name is `rs/`.
- 72 repositories have no `AGENTS.md`, 77 have no `specs/`; for a graph or a landing that is right, for a component it is a hole.
- `.claude/` is committed in 28 repositories; what in it is a plan belongs in `roadmap/`, what is a report belongs in `audit/`.
