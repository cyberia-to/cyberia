---
tags: cyber, cyberia, process, skill
alias: video production, video, the video skill, clip, film
crystal-type: skill
crystal-domain: cyberia
status: proposed
---

# video production

a skill of [[market]], inside its node 2, make: how the story of a release becomes a film that a person watches to the end and understands. the owner, 2026-11-19: video production is added as a separate skill of the market process.

it is a skill of its own because a film fails in ways a page does not: it has time, sound and a first three seconds, and one wrong number in it cannot be corrected by an edit of a page — the film is cut again. the unit is one film. a film that speaks is green when a viewer who has seen nothing else says back the story's one sentence; a loop, which carries no sentence, is green when that viewer names the product or the one feeling the loop left.

trigger: a story accepted in node 1 of [[market]] that names a film among its artifacts; a figure a door of a product waits for; a moment on the calendar. a trigger that brings no story of [[market]] names the product and the one thing the film must leave, and node 1 writes that sentence here: for a loop it is the name or the feeling the motion leaves, never a claim.

## the films

| film | length | where it plays | what it must do |
|---|---|---|---|
| loop | 4–12 s, silent, seamless | a door's figure, a card, a post | be the product's face: one motion that repeats with no cut |
| teaser | 15–30 s | x.com, the channels, the top of a deck | make one claim and name where to go |
| explainer | 60–90 s | the blog, a product's page, a talk | carry one idea from nothing to understood |
| demo | as long as the act | docs, a release note | show the real product doing one thing, unedited in its substance |

each is cut in two frames, wide (16:9) and tall (9:16), from one script.

## the graph

| node | role | makes | green when |
|---|---|---|---|
| 1 script · worker + critic | seer writes, keeper grades | the film as a table of shots: time, picture, words on screen, words spoken, the claim each shot carries | every number and every promise in it is a marked claim of the product page; a film that speaks fits its length read aloud, a silent film's shot clock sums to it |
| 2 shoot · workers | runner, one body per shot | the pictures: recordings of the real product, scenes drawn by code, generated footage, each a file with its source | a recording names its commit and replays; a scene renders from its source to the same frames; generated footage is marked as art |
| 3 cut · worker | runner | the film: pictures on the script's clock, words, sound, captions, a poster | the harness passes: length, frame, size, loudness, captions, no dead frame, the first three seconds carry the hook |
| 4 watch · worker | sensor plays the viewer, in its own context | what a fresh viewer understood: what was said back, where attention fell | what is said back means the film's sentence — the story's sentence for a film that speaks, the product's name or the feeling for a loop; no shot is named as unclear |
| 5 hand over · gate | counter | the film, its poster, captions and receipt to node 3 of [[market]], send | the receipt holds every check; the public voice passes the owner there, as every artifact does |

## the three kinds of picture

a film is honest by what each picture is, and the script says which.

- a recording is evidence. it is the real product at a named commit, captured from the screen, sped up or cropped and nothing more. a number seen in it is a number the product showed.
- a scene is an explanation. it is drawn by code — the same code as the product's pages where it can be: [[nox]]'s reducer on nox.band is a scene already. it may simplify, and it says what it simplifies.
- generated footage is art. it carries mood and no claim; nothing in it is offered as a fact.

a mock of something not built is none of the three. it is not made.

## the harness

checks a program runs on the cut film, written before the film is:

| check | passes when |
|---|---|
| length | inside the film's kind |
| frame | 1920×1080 and 1080×1920, 30 or 60 frames a second, H.264 high profile in MP4 — the one codec every browser plays |
| size | per cut: a loop under 1 MB for every 4 s of its length, a teaser under 8 MB, an explainer under 25 MB |
| the hook | the product's name or the claim is on screen inside the first three seconds |
| claims | every number on screen and every sentence spoken maps to a row of the script, and that row to a marked claim |
| captions | every spoken word is on screen and in a caption file; the film is understood with the sound off |
| sound | −14 LUFS integrated, within 1 LU, true peak under −1 dBTP — the platforms' level; no clipping; silence is chosen, never left |
| stillness | no frame repeats for more than a second unless the script says so |
| the loop | the motion continues across the loop point: the frame that would follow the last is the first, and the first frame is not repeated at the end |
| the door | a loop plays muted, inline and without a click on a phone, with a poster before it loads |

## how it is made

by files, in the product's repository under `landing/video/<film>/`, so that the film is rebuilt, never retouched:

| file | what |
|---|---|
| `script.md` | the table of shots, each row with its claim |
| `shots/` | the sources: a scene's page, a recording's steps and commit, the prompt and seed of generated footage |
| `render` | one program: opens each source in the house's headless browser, takes its frames, joins them with the words and the sound by ffmpeg |
| `out/` | the film in both frames, the poster, the captions |
| `audit/video-<film>.md` | the receipt: the harness's numbers, the commit, what the viewer said back |

no node, as everywhere: the browser, python and ffmpeg. a voice is the owner's, or a synthetic one named as such in the receipt.

## return edges

- short: a check of the harness that fails returns the film to cut; a shot that does not replay returns to shoot.
- long: a sentence said back wrong returns to script — the story was not carried, and a better cut will not carry it. three returns of one film mean the story is wrong, and it goes back to node 1 of [[market]].
- from the world: what [[market]]'s count shows — who watched to the end, who came — goes to the seer as a constraint on the next script.

## lanes

a film on a preview path is contained. a film sent in the state's name is wide and passes the owner at [[market]]'s send. a film that replaces a product's face — a door's figure — is irreversible in the public's memory and passes the owner.

## the measure

the share of viewers who reach the end; the arrivals a film brings, from [[lytics]]; its cost — the tokens and the minutes it took — against those arrivals.

## the first films

- a loop for each door of the stack that has only its motif in the frame: [[joy]], [[cybergraph]], [[neural]], [[cy]], [[cybernode]].
- a teaser of [[nox]] cut from its reducer: any order, one answer.
- a teaser per release candidate, cut from the release's own receipts.
