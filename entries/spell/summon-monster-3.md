+++
id = "ref/spell/summon-monster-3"
kind = "spell"
title = "Summon Monster III"
aon = "SpellDisplay.aspx?ItemName=Summon%20Monster%203"
source_ids = ["core-rulebook", "monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_monster_3", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/summon-monster-1" },
]
[[sources]]
publication = "core-rulebook"
page = "352"

[fields]
kind = "spell"
school = "conjuration [see text]"
subschools = ["Summoning"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 round"
components = "V, S, F/DF (a tiny bag and a small candle)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one summoned creature" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration \[see text\]
Level: 1: Antipaladin, Arcanist, Bard, Cleric, Medium, Oracle, Psychic, Skald, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Warpriest, Witch, Wizard
Casting time: 1 round
Components: V, S, F/DF (a tiny bag and a small candle)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: one summoned creature
Subschool: Summoning
:::

### Summon Monster III

This spell functions like [summon monster I](ref/spell/summon-monster-1), except that you can summon
one creature from the 3rd-level list, 1d3 creatures of the same kind from the 2nd-level list, or
1d4+1 creatures of the same kind from the 1st-level list.

###### ^1^ {#footnote-1}

By a strict rules-as-written interpretation, regular casters can only apply the celestial or
fiendish templates, since this spell was written before the resolute and entropic templates existed.
_Bestiary 2_ introduced the resolute and entropic templates and said they could apply to summons,
but left no specifics. _Monster Summoner's Handbook_ added archetypes that could use the resolute
and entropic templates. However, Paizo's official open-content website cites _MSH_ and notes "summon
monster can be used to summon creatures with the entropic or resolute templates instead of the
celestial or fiendish template". In any event, only one template may be applied automatically to a
summoned creature: lawful good casters could choose celestial or resolute, but not both. Consult
your GM.

###### ^2^ {#footnote-2}

The original text was written before the entropic and resolute templates were created (see footnote
above), so the text generally refers to neutral on the good-evil axis only. However, a neutral good
caster could theoretically pick either resolute or entropic instead of the default celestial.
Consult your GM.
