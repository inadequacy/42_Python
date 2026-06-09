from ex1 import capabilities

heal_factory = capabilities.HealingCreatureFactory
transform_factory = capabilities.TransformCreatureFactory
heal_ability = capabilities.HealCapability
transform_ability = capabilities.TransformCapability

__all__ = ["heal_factory", "transform_factory", "heal_ability",
           "transform_ability"]
