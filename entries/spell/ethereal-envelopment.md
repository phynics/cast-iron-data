+++
id = "ref/spell/ethereal-envelopment"
kind = "spell"
title = "Ethereal Envelopment"
aon = "SpellDisplay.aspx?ItemName=Ethereal%20Envelopment"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ethereal_envelopment", path = "json/spells4.json" },
]
[[sources]]
publication = "occult-adventures"
page = "170"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Psychic", level = 7 },
  { class = "Spiritualist", level = 5 },
]
casting_time = "1 standard action"
components = "S, M (empty crystal box)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Spiritualist\
7: Psychic
Casting time: 1 standard action
Components: S, M (empty crystal box)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level (D)
Saving throw: Will negates, see text
Spell resistance: yes
Target: one creature
Subschool: Teleportation
:::

This spell is similar to ethereal envelope, but it allows you to shunt an unwilling creature to the
Ethereal Plane and seal it there within a cocoon of misty ethereal fibers. If the target fails its
save, it's forced into a cataleptic meditative state as if unconscious. However, each round at the
end of its turn, it can attempt a Will save to awaken itself from this meditation. Once the target
awakens, it is considered pinned, treating your caster level as your CMB and your CMD as 10 + your
caster level + your ability modifier for your primary spellcasting ability score. A successful
grapple combat maneuver check or Escape Artist check leaves the creature grappled rather than pinned
but doesn't allow it to escape. However, a trapped creature can attack the cocoon as described in
the ethereal envelope spell description.

If the creature breaks free of the ethereal envelopment or you dismiss the spell, the target is
returned to its prior location on the Material Plane, as described for ethereal envelope, but if the
target is conscious at the time, it doesn't spend a round asleep or staggered.
