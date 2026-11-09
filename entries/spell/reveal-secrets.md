+++
id = "ref/spell/reveal-secrets"
kind = "spell"
title = "Reveal Secrets"
source_ids = ["inner-sea-temples"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reveal_secrets", path = "json/spells8.json" },
]
[[sources]]
publication = "inner-sea-temples"
page = "63"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["language-dependant", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of alcoholic liquid)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Arcanist, Bard, Inquisitor, Mesmerist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a drop of alcoholic liquid)
Range: touch
Duration: 1 round
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
Subschool: Compulsion
Descriptors: language-dependant, mind-affecting
:::

When you cast this spell, you ask the target whether it has a secret about a specific topic that can
be described in 10 words or fewer. This can concern a person, place, or thing (such as a town's
mayor, the ring worn by a traveling merchant, or the bridge spanning a nearby river) or an easily
distinguished event (such as a historic battle or a recent rash of disappearances). If the target
knows a secret about the topic (information it believes isn't common knowledge and which it would
not normally tell you), it states it has a secret. The target doesn't mention anything about the
secret and doesn't remember telling you it has a secret. If the target succeeds at its saving throw,
it isn't compelled to reveal whether it knows a secret and is aware that you asked.
