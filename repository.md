---
tags: cyber, article
alias: repository, product folder, the folder of a product, the standard repository, workspace, project structure, repo layout, project conventions, repository structure
crystal-type: pattern
crystal-domain: cyber
---

# repository — the folder of a product

a repository is the folder of one product, and it holds the whole product: its goal, its plan, its contract, its implementations, its faces, its operation and its evidence. the direction (the owner, 2026-11-22): every product has one repository, a product is never spread over several, and every repository is a product. the folder is read by people, by agents and by machines — the combine decides from it how a change travels, the [[release]] decides what a version carries, the cockpit of [[apparatus]] draws the product from it.

today the home holds 113 repositories for the 26 products of [[products]]; what that distance consists of is in § where it lives today, and the decision that closes it is [[d7 repository shape]].

## the folder

```
<product>/
│  the goal
├── README.md         the product's page: what it is, for whom, every claim with its dot
├── AGENTS.md         the rules for every agent that works here, and the gates that must be green
├── CHANGELOG.md      what each version carried, every change with the link to its pull request
├── LICENSE           the license
│
│  the plan
├── projects/         one page per project: a task with sub-tasks that serves the goal and closes
├── tasks/            one page per unit of deliver, and per decision put to the owner
├── roadmap/          one file per open question about the contract, with its status
│
│  the contract
├── specs/            what must be true: formats, invariants, acceptance; README.md is its index
├── tests/            the vectors every implementation passes
│
│  the implementations
├── rs/               the product in Rust: rs/Cargo.toml is the workspace, each part a crate inside it
├── py/  js/  cw/     the product in another language, each folder with its own manifest
│
│  the faces
├── cli/              the command a person types
├── app/              the application a person opens
├── site/             the product's page on its domain
├── docs/             the explanation: tutorials, guides, concepts
├── examples/         programs a reader can run
│
│  the operation
├── release/          how its versions are cut: the scale it rides, its pins, its gates
├── servers/          where it runs: hosts, units, configuration, the deploy
├── processes/        which triggers and performers run the processes on this product
├── access/           who may command it and who may read it
│
│  the evidence
├── audit/            what was checked, when, at which revision, and what came of it
├── journal/          one line per command and one per answer
├── data/             the series the product collects about itself
│
│  the machinery
├── scripts/          the product's own tools, in nushell or Python
└── .github/          the checks that run on a pull request
```

a product carries the folders it needs. a folder it carries has the name and the meaning above. the root belongs to the product and to no language: a manifest lives in the folder of its language.

## the eight groups

every path of the folder belongs to one group. the group says which question the path answers, how a change to it travels, and whether a release names it.

| group | the question | paths | a change travels | in a release |
|---|---|---|---|---|
| goal | what is this product and what does it promise | `README.md`, `AGENTS.md`, `CHANGELOG.md`, `LICENSE` | by a pull request; `AGENTS.md` is the wide lane | yes |
| plan | what is meant next and who decides | `projects/`, `tasks/`, `roadmap/` | `projects/` and `tasks/` directly, as the working state of a decision; `roadmap/` by a pull request | `roadmap/` yes |
| contract | what must be true | `specs/`, `tests/` vectors, `conformance/`, `schema/` | by a pull request, the wide lane | yes |
| implementation | what runs | `rs/`, `py/`, `js/`, `cw/` | by a pull request | yes |
| faces | what a person meets | `cli/`, `app/`, `site/`, `docs/`, `examples/` | by a pull request; `site/` is the wide lane | yes |
| operation | how it is released, served and commanded | `release/`, `servers/`, `processes/`, `access/` | by a pull request; `access/` and a lease by the owner's hand; a trigger's clock by the owner's signed command | yes |
| evidence | what was observed | `audit/`, `journal/`, `data/` | directly: a receipt is written when the check is made | no |
| machinery | how the folder is built and checked | `scripts/`, `.github/` | by a pull request; `.github/` is the wide lane | yes |

the rules a machine applies are `apparatus/combine/zones.toml`; this table is their meaning, and when the two disagree the table is corrected first and the rules follow.

the order of truth runs down the folder: the goal is accepted before the plan; the contract is written before the implementation; when code and a spec disagree the spec is settled first and the code follows; evidence is attached to the claim it checked, and a dot on the goal turns green only from a page of `audit/`.

## the goal

`README.md` is the product's page — the door on GitHub and the page of the product in the graph are one text. it says what the product is in one paragraph, for whom, and lists its claims, each with a dot: measured, target or mock ([[products]]). a product is delivered when every dot is green. below the claims: how to build and check it, and links into `specs/` and `docs/`.

`AGENTS.md` is the one instruction file for agents: the gates that must be green, the paths that need a discussion before they change. the file has this name in every product.

## the plan

- `projects/` — a project is a task with sub-tasks: it serves the goal and it closes. one page per project, with `status`, `owner`, `serves`, `part of` and `lane` in its front matter. the registry of all projects, in the owner's order of priority, is [[cyberia/projects]]; it is collected from the `projects/` of every product by `apparatus/scripts/projects_collect.py`.
- `tasks/` — a task is a unit of [[deliver]]: one change a person could review alone, with its lane and its "done when". a decision put to the owner is a task of the kind `review`, with what speaks for, what speaks against, and the verdict.
- `roadmap/` — what is meant about the contract and is still open: one file per question, with a status in its front matter — `draft`, `accepted`, `rejected`, `implemented`, each meaning what [[documentation]] § design proposals says it means. an implemented one moves its substance into `specs/` and keeps a line that says where it went.

## the contract

`specs/` is the specification: complete, austere, ordered by the structure of the system. `specs/README.md` lists every spec with its status. a spec says what holds. a number that was measured goes to `audit/` with the command and the revision that produced it, and the spec links to it. what one product promises another is a contract and lives in the `specs/` of the one that promises.

## the implementations

one contract, many implementations. each language owns one folder at the root, named by the language — `rs/` for Rust, `py/` for Python, `js/` for JavaScript a browser runs, `cw/` for CosmWasm contracts — and everything of that language is inside it, its manifest included. every implementation answers to the same `specs/` and passes the same vectors in `tests/`.

- `rs/Cargo.toml` is the Rust workspace of the product. each part of the product is a crate inside it, `rs/<part>/`, published from there under its own name. neural and lytics are built this way today.
- a product of one crate keeps that crate directly in `rs/`.
- a part is a folder of its product. what is a separate repository of a part today — strata and hemera of [[nox]], the 79 components of `soft3/release/components.toml` — becomes `rs/<part>/` of the product it composes.

## the faces

a face is what a person meets, and each is built from the implementations of its own product.

- `cli/` — the command. its name is the product's name; a Rust command is a crate with its own manifest that depends on `../rs`, as in bbg.
- `app/` — the application: desktop, mobile, the shell.
- `site/` — the page of the product on its own domain; the production build is made for the root of a host.
- `docs/` — the explanation, by [[documentation]]: `tutorials/`, `guides/`, `explanation/`.
- `examples/` — programs a reader can run.

## the operation

what apparatus needs to release, serve and run the product is declared in the product's own folder, and apparatus reads it from there.

- `release/` — the scale the product rides (the day, the week, the moon), the revisions it pins, the gates a version must pass, the volume it deploys.
- `servers/` — the hosts and the units the product runs as, their configuration, the deploy script; the domain and its records beside them.
- `processes/` — the bindings: which trigger starts which node of [[deliver]], [[release]], [[operate]], [[listen]], [[market]] on this product, and who performs it.
- `access/` — the addresses that may command the product and those that may read it. it changes by the owner's hand.

## the evidence

- `audit/` — audits, implementation status, benchmark results and release validation, by subsystem or by date. every report names its date, the revision it checked, the command behind each number, and its limits.
- `journal/` — the log of the work on the product: one line per command and one per answer, `journal/<date>.md`.
- `data/` — the series the product collects about itself: the daily fix, measurements, counters.

## where it lives today

the folder above is the target. measured on 22 November 2026 ([[repository layout audit 2026-11-22]] § the product's folders):

| part of the folder | where it is today |
|---|---|
| the goal | the table of [[products]] in the cyberia repository; `product/` in cyb alone |
| `projects/` | cyberia (16 pages, for every product) and apparatus (7); also cyberia-blog, kadek, midao |
| `tasks/` | apparatus (24), cyberia (5), cyber |
| `roadmap/` | 19 repositories; `proposals/` in soft3 and foculus is the same thing under its old name |
| `specs/` | 36 repositories; `reference/` in ten more is the contract under its old name |
| `rs/` | 21 repositories; 15 of them, and 37 more, keep a `Cargo.toml` at the root; `src/` at the root in 21, `crates/` in 11, `crate/` in soft3 |
| `cli/` | 23 repositories |
| `app/` | go-cyber, mail, omi; `apps/` and `shell/` in cyb |
| `site/` | soft3; `landing/` in cyb, cyber, trident; `sites/` in apparatus holds the sites of other products |
| `release/` | apparatus (`culture.toml`, the row of every product), soft3, cyber |
| `servers/`, the domains | apparatus, for every product; `deploy/` in cybernode and soft3 |
| `processes/` | apparatus `processes/bindings.toml`, for every product; the pages of the processes in cyberia |
| `access/` | apparatus |
| `journal/` | apparatus, one log for every product |
| `data/` | no repository |
| `audit/` | 30 repositories |

so the plan and the operation of every product live in two repositories — cyberia and apparatus — and the goal in a third. each line of the table is a unit of [[deliver]], and this page changes none of them. apparatus is itself a product, the operations of cyberia: what serves the organisation as a whole — the combine, the fleet, the cockpit — stays its own implementation, and what is one product's row in its files moves to that product's folder.

## across products

a product names another by relative path from the home, `../<product>/rs`, and pins its revision where a release needs it. a path in a page or a report is written with its product: `tru/specs/rewards.md`. another project's code that a product builds on is kept as it came, as a folder of the product that uses it.
