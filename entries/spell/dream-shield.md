+++
id = "ref/spell/dream-shield"
kind = "spell"
title = "Dream Shield"
source_ids = ["occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dream_shield", path = "json/spells13.json" },
]
[[sources]]
publication = "occult-origins"
page = "28"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (hollow glass ball or dreamcatcher)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Alchemist, Bard, Investigator, Medium, Mesmerist, Shaman, Skald\
3: Psychic\
4: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (hollow glass ball or dreamcatcher)
Range: touch
Duration: 1 hour/level
Saving throw: Will negates (harmless)
Spell resistance: no
Target: creature touched
:::

You ward the target's mind against intrusion and influence while she is unconscious. While sleeping,
the target is protected against divinations such as nondetection and gains
[spell resistance](ref/rule/spell-resistance) equal to 10 + your caster level against mind-affecting
effects. In addition, the subject immediately receives another saving throw (if one was allowed to
begin with) against any spell or effect that would possess or exercise direct mental control over
her. This functions in all respects like the second property of
[protection from evil](ref/spell/protection-from-evil) but it applies regardless of the alignment of
the creature or object that created the possession or mental influence effect.

If the target is awake, instead of the previous effects, the dream shield provides a +4 bonus on
saving throws against sleep effects. The spell's other effects are suppressed while the target is
awake. If the target falls asleep or is otherwise rendered unconscious, the other effects of the
dream shield resume. Every 10 minutes spent awake consumes 1 hour of the dream shield's duration.
