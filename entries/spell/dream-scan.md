+++
id = "ref/spell/dream-scan"
kind = "spell"
title = "Dream Scan"
aon = "SpellDisplay.aspx?ItemName=Dream%20Scan"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dream_scan", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/dream" },
]
[[sources]]
publication = "occult-adventures"
page = "165"

[fields]
kind = "spell"
school = "divination"
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "unlimited"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "see text"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Medium\
5: Mesmerist, Psychic\
6: Arcanist, Bard, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: unlimited
Duration: see text
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Descriptors: mind-affecting
:::

This spell functions as [dream](ref/spell/dream), but rather than sending a message to a sleeping
target, you can instead read the target's thoughts. The target must be asleep for you to perform a
dream scan, though if the target isn't asleep, you can wait in a trance until your target falls
asleep. Once the target is asleep, you can concentrate in order to read its surface thoughts as if
using detect thoughts. You can continue concentrating for up to 1 minute per caster level.

Instead of reading surface thoughts, you can choose to scan the target's dreams and subconscious
mind for the answers to questions. For every minute you spend concentrating, you can obtain the
answer to one question, though the answers might be brief, cryptic, or repetitive. The target is
entitled to a new Will save to end the dream scan each time you ask it a question. Otherwise, the
creature can attempt a Bluff check with a DC equal to 11 + your Sense Motive modifier. If it fails
its Bluff check, you gain the information you desire. If it succeeds at its check, you gain no
information. If it succeeds at its check by 5 or more, you misinterpret the target's dreams-you draw
a false conclusion of the target's choice and believe that wrong answer to be true.

Unlike with dream, you can't cast this spell on another creature to have it serve as your messenger.
